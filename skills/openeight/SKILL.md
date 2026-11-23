---
name: openeight
description: Connect an existing agent to OpenEight governance or observation, set up its SDK against an existing endpoint, create a governed refund demo project, run a chosen OpenEight cookbook agent, or check an existing integration.
---

# OpenEight

Help the user reach a verified OpenEight integration with the smallest supported
change. Preserve their chosen agent, framework, model, and application state.
This skill covers client onboarding; server deployment, AWS administration, and
audit CLI setup are outside its scope.

## Inspect and choose a path

Start with the application's dependencies, configuration, agent construction, and
tool execution. Infer what the code already tells you; ask only for missing choices
that affect the integration. Distinguish a new integration from an existing one
that needs checking, and preserve the user's choice of governance or observation.
If that choice is unclear, explain the effect on tool execution before proceeding.

Read the bundled [support guidance](references/support.md) before choosing SDK
instructions. This is candidate guidance: it does not establish a qualified public
release or installation route. Check installed versions and public signatures;
do not silently upgrade packages or treat unknown versions as supported.

Read only the references needed for the task:

| Task | Reference |
| --- | --- |
| Set up dependencies and connection configuration | [SDK setup](references/setup.md) |
| Connect or check an existing application | [Inspection and adapter selection](references/existing-agent.md) |
| Create a governed refund project, walk through a first refund, or run a chosen recipe | [Cookbook workflow](references/cookbook.md) |
| Verify an integration or diagnose a failed run | [Verification and failures](references/verification.md) |

Fetch cookbook only for a recipe request. Existing-app integration uses the SDK
and bundled references, without private server or developer checkouts.

For an interactive walkthrough, perform the available project steps, then pause at
the first action that needs the user. Ask for that action and resume on their reply.

## Connect the application

Use the selected framework or dispatch integration and preserve existing resource
ownership, lockfiles, secrets, checkpoints, and unrelated edits. For an existing
integration, inspect and repair the relevant seam rather than adding a second wrapper.

Use an explicit endpoint, Agent name, and externally supplied machine credential
through the application's secret configuration. Never ask for secrets in chat,
print credential values, or overwrite an existing env file with a template.
Preserve TLS and optional content-capture defaults; do not print raw tool/model
content or full catalog schemas.

When Console setup is missing, explain the specific step the authorized human
needs to take and what will be checked afterward. Do not create policies, activate
bindings, change trust, mint keys, or resolve human approvals to make onboarding
pass. Machine credentials do not grant human Console read or administration rights.
Continue independent code and local verification work while that step is pending.

## Verify and hand off

Read [verification](references/verification.md) before an integrated run. Inspect
reachable effects and obtain the required authorization before invoking live
models, discovering tools with side effects, or running against a live backend.
Use a bounded run with a controlled destination; do not retry indefinitely.

Verify each relevant stage: dependency setup, identity, tool publication, readiness,
per-attempt authorization, handler execution, telemetry delivery, and persisted
Run/Event data. Publication acknowledgement is not readiness, and readiness is not
per-attempt authorization. Denied, pending, dry-run, and unavailable authorization
must reach zero business handlers. Never switch to observation after a governance
failure or rename identities to hide conflicts.

For the first-refund walkthrough, finish at the verified simulated receipt.
When persistence verification is in scope, use authorized scoped reads or identify the exact human
Console check still needed. Fix failures within the requested scope and repeat
the affected checks. Stop live retries on credential/scope failures or catalog
conflicts and give the concrete recovery step.

Report the files changed, exact input versions, checks performed, and remaining
human steps. Distinguish local simulations, candidate qualification, live runs,
and persisted evidence. For observation, state that policy is not enforced. For
setup-only work, finish at the requested setup boundary without claiming a verified
integrated run.
