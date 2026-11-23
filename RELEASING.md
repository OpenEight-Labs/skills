# Releasing the skill

Release instructions that have been tested against the SDK versions they describe.
Record verification in the pull request and release notes; this repository does
not maintain a separate release manifest or evidence schema.

## Verify the change

Run `python scripts/validate.py` and manually verify changed runnable examples as described
in [TESTING.md](TESTING.md). For SDK contract changes, link the SDK change
and record the exact artifact version, source revision, digest, and dependency
lock used. Local example results do not qualify a public installation.

For routing or workflow changes, compare assistant behavior with the baseline in
Codex and Claude Code using the scenarios in `TESTING.md`. Record the versions, results,
and skipped checks. Review changed instructions, tooling, and release changes
independently, including credential handling and human governance boundaries.

## Check the installation before publishing

Keep SDK-dependent instructions off the default installation branch until exact
published-package acceptance passes. Before the first qualified release, that
branch contains no entry skill. Test with published registry artifacts in a clean
workspace, without editable installs or sibling source checkouts. Fetch cookbook
separately at a recorded immutable revision only when testing a recipe workflow.

Verify skill discovery, bundled links, and the documented install, update, and
immutable-reference routes. Check the final merge tree against what was tested.
Advertise installation commands only after those checks pass. Record the skill
revision, package inputs, assistant results, and remaining limitations in the PR
and release notes; retain detailed logs as CI artifacts or private evidence.

Verify maintainer contacts and repository protections before public release.
Publication, installer network tests, and live or paid runs require authorization;
local checks do not authorize them. Keep installation, live execution, and human
Console acceptance distinct when describing release readiness.

## Rollback

Restore working guidance through a reviewed new revision; do not move release
tags. Verify how installed skill copies update or are removed. Do not implicitly
revert user code, application state, or external effects.
