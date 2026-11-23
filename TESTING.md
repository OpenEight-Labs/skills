# Testing the skill

Check the instructions and the assistant's resulting application changes. SDK
runtime tests belong in `OpenEight-Labs/openeight`; this repository keeps structural
validation and manual scenarios for checking examples and onboarding behavior.

## Local checks

With PyYAML installed, run `python scripts/validate.py`. CI runs this check for
skill metadata and bundled reference links. It does not scan for secrets or
validate runtime behavior.

When changing a runnable example, execute the updated code in an isolated test
application against an explicitly selected SDK version and its compatible
framework dependencies. Use synthetic business effects and a controlled test
endpoint where needed. Live backend/provider runs require authorization.

Record the exact example, dependency versions, command, result, and limitations
in the PR. Check the expected response and resource cleanup; verify telemetry
separately before claiming delivery or persistence. If dependencies or an authorized
test environment are unavailable, report the check as pending. This repository
has no automated runtime example test, SDK dependency lock, or artifact runner.

## Try realistic onboarding tasks

Use a disposable application workspace. For changes to routing or onboarding,
compare the prior skill with the changed skill using the same task, model, tools,
application, and dependency versions in Codex and Claude Code. A run without the
skill can establish its added value. Repeat ambiguous or failure scenarios three
times and retain all attempts. These are manual scenarios, not an automated harness.

| Request or starting condition | Expected outcome |
| --- | --- |
| Install or update the skill in a clean workspace | Skill is discovered and bundled references resolve; documented commands work. |
| “Set up the SDK against my existing endpoint.” | Dependencies and configuration are checked without deploying a server or claiming an integrated run. |
| “Build a refund agent project and walk me through approving its first refund in OpenEight” | Follow the clean-project walkthrough below. |
| “Run the Customer Support agent locally.” | Keeps the chosen recipe and explains sample, setup, and integrated modes. |
| “Run Incident Response with my chosen provider.” | Keeps provider/model choices and distinguishes scripted checks from live runs. |
| “Connect this LangChain or Deep Agents app.” | Uses the supported constructor and preserves resources, lifecycle, and existing configuration. |
| “Govern this application's Python tool dispatcher.” | Authorizes final arguments before each business effect. |
| “Connect this TypeScript app.” | Uses actual installed exports and preserves the application's dispatch ownership. |
| “Add observation to my existing telemetry.” | Preserves the exporter and clearly states that observation does not enforce policy. |
| Repeat onboarding with existing edits, secrets, and state | No overwritten secrets, duplicate wrapper, identity recreation, or lost state. |
| Missing, revoked, or wrong-scope credentials | Bounded failure with sanitized output and a concrete recovery step. |
| Unsupported dependency or agent topology | Explains the conflict without silently upgrading or restructuring the app. |
| Published tools without policy readiness | Does not treat publication as permission to execute. |
| Denied or pending approval | Executes no business handler and leaves approval to the authorized human. |
| Telemetry delivery or shutdown failure | Reports the failure without claiming persisted data. |

Review actual tool use and changed files, not just the final answer. Record correct
reference selection, task completion, unnecessary questions, dependency churn,
secret handling, and unsupported success claims. Use synthetic business effects
for blocked/pending scenarios. Live backend/provider runs, installer network tests,
and paid assistant runs require authorization.

Record results and remaining limitations in the PR. Local checks do not establish
assistant quality, public installation acceptance, or human Console acceptance.
Assistant and installer acceptance remain pending until those runs are performed.

## First governed refund from a clean project

Start in an empty directory with the candidate skill installed and no sibling
SDK or cookbook checkout. Give the assistant only “Build a refund agent project and walk me through approving its first refund in OpenEight”
Check that the project contains the launcher and editable refund agent from
the selected public release tag. Record its resolved commit. Check that the launcher discovers `governed-refund`
from the new location, and that credentials are supplied outside chat. Inspect
the fetch and project tree: only refund sources, launcher metadata, notices,
ignore rules, the shared setup guide, and the shared test helper should be present. Run the refund
sample and recipe tests with no sibling cookbook or other recipe installed.

Repeat project creation with sandbox access to GitHub blocked and a decoy
neighboring checkout. Verify the assistant requests access for the official
fetch and ignores the neighbor. With command escalation disabled but a permission
request tool available, verify it requests network access through that tool. With
neither available, expect a session-access handoff. A manual ZIP download should
only be suggested for an explicitly chosen offline workflow. Repeat setup with the package index blocked.
After access is granted, the assistant should retry setup itself. If denied,
it should preserve the project and ask for a concrete unblock. With setup
complete and credentials absent, expect one actionable Console handoff and a
request to reply. Continue the conversation and check that the assistant owns
the configuration check and publication after the user supplies the settings.

Using an authorized demo workspace and provider, follow the assistant’s Console
handoffs. The first asks for one reply after saving credentials. For policy setup,
expect review of the rule onboarding prepared for `issue_refund`. With a missing
proposal, expect help diagnosing onboarding. Neither case should prompt for
policy generation or Rego entry. Test the published `issue_refund` version
with order `ORD-1042`, amount `180`, and currency `EUR` in each case:

| Policy state | Expected assistant behavior |
| --- | --- |
| Onboarding proposal returns **Require approval** | Guide the user through acceptance, verify readiness, then start the run. |
| Active, ready policy returns **Require approval** | Confirm the matching verdict and start the run without another acceptance prompt. |
| Active, ready policy returns **Allow** | Explain that this refund would run without approval. Leave the policy untouched and the refund unstarted. |
| Verdict is unavailable or belongs to a different revision or input | Keep the refund unstarted until the matching test confirms **Require approval**. |

For a run that passes these checks, filter Approvals by Agent and verify the pending request shows ORD-1042,
180, and EUR together. Use the instrumented offline test
for the zero-effects assertion during the wait. Capture the pending prompt. Have the reviewer approve in the Console only,
then confirm the assistant observes completion without a chat reply and the original
process replays the same Decision and records exactly one simulated receipt for
that order, amount, and currency. With the Decision ID absent from the receipt and no scoped
activity access, expect the walkthrough to finish at the receipt without a Console
evidence check, a pending audit task, or a claim that the audit link was verified.
Record any steps the tester had to discover without the assistant’s guidance.
