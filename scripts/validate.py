"""Check skill metadata and local Markdown links within the installed bundle."""
import re
from pathlib import Path

import yaml

SKILL = Path(__file__).resolve().parents[1] / "skills/openeight"
text = (SKILL / "SKILL.md").read_text()
match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
if not match:
    raise SystemExit("SKILL.md must start with YAML frontmatter")
metadata = yaml.safe_load(match[1])
if not isinstance(metadata, dict) or metadata.get("name") != SKILL.name:
    raise SystemExit("Skill name must match its directory")
description = metadata.get("description")
if not isinstance(description, str) or not description.strip():
    raise SystemExit("Skill description must be a nonempty string")

for page in SKILL.rglob("*.md"):
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", page.read_text()):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (page.parent / target.split("#")[0]).resolve()
        if not resolved.is_relative_to(SKILL.resolve()) or not resolved.is_file():
            raise SystemExit(f"Invalid bundled link in {page.relative_to(SKILL)}: {target}")

print("Validated skill metadata and bundled Markdown links")
