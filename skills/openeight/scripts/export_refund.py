"""Export the governed refund project from an official OpenEight release."""

import argparse
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory


REMOTE = "https://github.com/OpenEight-Labs/openeight.git"
PATHS = (
    "cookbook/cookbook.py",
    "cookbook/recipes.toml",
    "cookbook/.gitignore",
    "cookbook/LICENSE",
    "cookbook/NOTICE",
    "cookbook/guides/setup.md",
    "cookbook/patterns/governed-refund",
    "cookbook/tests/__init__.py",
    "cookbook/tests/support",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="destination project directory")
    parser.add_argument("--revision", default="cookbook-v0.0.1", help="release tag or full commit ID")
    args = parser.parse_args()
    revision = args.revision
    ref = revision if re.fullmatch(r"[0-9a-fA-F]{40}", revision) else f"refs/tags/{revision}"
    if ref != revision:
        subprocess.run(["git", "check-ref-format", ref], check=True)

    project = args.project.resolve()
    target = project / "cookbook"
    if target.exists() or target.is_symlink():
        parser.exit(1, f"{target} already exists. Reuse the project or choose a fresh directory.\n")
    project.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=project, prefix=".refund-export-") as temporary:
        staging = Path(temporary)

        def git(*args, **kwargs):
            return subprocess.run(["git", *args], cwd=staging, check=True, text=True, **kwargs)

        git("init", "--quiet")
        git("remote", "add", "origin", REMOTE)
        git("config", "remote.origin.promisor", "true")
        git("config", "remote.origin.partialclonefilter", "blob:none")
        git("sparse-checkout", "set", "--no-cone", "--stdin",
            input="".join(f"/{path}\n" for path in PATHS))
        git("fetch", "--quiet", "--depth=1", "--no-tags", "--filter=blob:none", "origin", ref)
        commit = git("rev-parse", "FETCH_HEAD^{commit}", capture_output=True).stdout.strip()
        git("checkout", "--quiet", "--detach", commit)
        for path in PATHS:
            if not (staging / path).exists():
                parser.exit(1, f"Missing {path} at {revision}.\n")
        (staging / "cookbook").rename(target)
    print(f"Exported {target} from {revision} ({commit})")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
