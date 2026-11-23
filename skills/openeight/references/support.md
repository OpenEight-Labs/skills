# Support and compatibility

Codex installed the published Python SDK and guided a hosted refund walkthrough
through Console approval to a simulated receipt. The revised policy handoff was
checked separately in Codex using a simulated onboarding state. Claude Code
behavioral testing is deferred. Anonymous installation is pending public release.

The candidate references target Python `openeight` 0.0.1 and TypeScript
`@openeight/sdk` 0.0.1. Distinguish the runtime of the selected artifact from the
runtime used to verify a particular example:

| Workflow | Runtime guidance |
| --- | --- |
| Python SDK | Current source metadata permits Python `>=3.11,<3.16`, and its managed framework registry includes standard CPython 3.15. Check the installed artifact's metadata and exact framework tuple before using that range. |
| Cookbook | The launcher help and setup guidance document Python 3.11–3.14. Use that documented range for recipes; the launcher's minimum-version check alone is not evidence of 3.15 compatibility. |
| TypeScript SDK | Node 24 is the candidate target. Public package acceptance remains pending. |

The recorded Python framework inputs are LangChain 1.4.3, langchain-core 1.6.7,
and Deep Agents 0.7.23. These are not a complete dependency matrix or proof that
every runtime and workflow has passed release acceptance. Source admission of
Python 3.15 does not extend an earlier 3.11–3.14 example check to that runtime.

Before changing an application, inspect its installed SDK version, public
signatures, and that release's compatibility documentation. Preserve existing
locks and select only the integration and extras the task needs. If the installed
version differs, inspect its contract and state what remains unverified rather
than assuming these examples apply or silently upgrading.

For example checks, use an explicitly selected installed SDK and its compatible
framework dependencies. Record their versions and test results in the PR or CI
artifacts. A local example check does not establish live backend behavior or
assistant onboarding quality; report those checks separately.
