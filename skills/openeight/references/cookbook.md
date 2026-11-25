# Run the requested recipe

For a new first-refund project, export the refund project using the bundled helper below from the official
`https://github.com/OpenEight-Labs/openeight.git` repository at the cookbook release pinned by the helper. Honor an explicit revision supplied by the user. For other
recipes use their selected immutable revision. Inspect the requested project
only. A neighboring checkout or cached release tag is not a fallback source.
An explicitly supplied candidate can be used and identified as such.

Run export and dependency setup as separate operations. If Git or pip reports a
sandbox DNS or registry failure, use the client's permission tool for that
operation. In Codex, look for `request_permissions` when command escalation is
disabled. If available, request network access scoped to the turn and rerun the
same command after a grant. Where command escalation is supported, submit that
command with `sandbox_permissions="require_escalated"` and its justification.
Respect a denial. If the client has no usable permission mechanism, identify the
blocked host and ask the user to enable network access for the CLI session, then
resume the export or install yourself. Suggest a user-supplied artifact only
when the user chooses an offline workflow. A successful tag lookup through a
connector does not download the project.

Check pip’s earlier index or connection diagnostics before treating a final “no
matching distribution” as an unavailable build dependency. Preserve partial work
for the retry.

Read the catalog and selected recipe README. Use a working Python 3.11–3.14
interpreter to launch setup from the cookbook root; setup creates the recipe
environment. Verify dependency installation before checking connection settings.

Use `python cookbook.py list` only if selection is missing; `list --all` also shows patterns.
The business agents are customer-support and incident-response. Retain the user's choice.
Use `python cookbook.py sample NAME` for a local simulation. Use the launcher's
`setup NAME`, `check NAME`, `test NAME` and `run NAME -- ...` as the recipe documents.
Do not create a second dependency installer or duplicate the launcher logic.

Before setup, inspect existing environments, state paths and owned processes. Preserve
existing env/private files and pending durable work on its original revision/runtime.
Launcher check validates configuration and environment presence; it does not authenticate
or prove readiness. Samples/refund receipts simulate effects and are not real payments.
Incident Response scripted acceptance is separate from provider mode. Request explicit
provider/model credentials only for the selected provider mode. Customer Support model
requirements come from the catalog; do not switch recipes to avoid them.

Before integrated invocation, inspect reachable tools, verify exact publication and readiness,
and use a controlled destination. Use instrumented tests for denial/pending handler counts and report
telemetry delivery/persistence separately. A live provider or backend run requires its
own authorization; configuration and samples do not satisfy those acceptance gates.

## First governed refund

For a new refund agent project or first governed refund, select the LangChain
`governed-refund` pattern. For project creation, export the refund project into the requested
empty directory, preserving their layout under `cookbook/`. If the current folder contains an application,
create the new project in a fresh child directory. Keep the launcher, catalog,
and recipe in their original relative locations. For a repeat walkthrough,
reuse the existing demo. Show the user the editable agent in
`patterns/governed-refund/langchain_agent.py` relative to the cookbook root
and give them the launcher command from that root.

Run the bundled [refund export helper](../scripts/export_refund.py) with a working
Python interpreter. Resolve the script relative to this installed skill and pass the
destination project directory, for example
`python3 "$skill_dir/scripts/export_refund.py" "$project_dir"` with both paths resolved.
Use
`--revision TAG_OR_FULL_COMMIT` for an explicit override. The helper stages the
sparse checkout, including its lazy blob downloads, within one network operation
and prints the resolved commit. Reuse an existing demo on repeat visits.

The export includes the launcher, refund pattern, shared test helper, and
`cookbook/guides/setup.md`. Use that guide for provider adapter installation
and environment precedence. Keep package installation a separate operation.

Use the pattern’s README for setup and its `docs/operations.md` for the demo
policy semantics. Use the Console handoffs below for guided setup.

Drive this as a conversation. Run setup yourself before asking for credentials.
A keyless sample is optional and does not complete this request. At each human
handoff, give the next action and its destination. Ask for a reply only when
you cannot observe completion. Continue when the result is available.
Only give a full manual runbook when the user requests one.

1. Help the user configure the demo endpoint, Agent name, machine key, and
   explicit model/provider credentials through the recipe’s secret configuration.
   In one handoff, link to the Console (production: https://app.openeight.ai),
   direct them to their workspace’s LangChain Agent setup, and give the actual
   private env file path and five field names. Ask for one reply after saving
   the settings. Keep keys out of chat and read the provider from the configured
   model when checking its adapter.
2. Check the configuration and publish the tool schemas yourself. Verify tool
   classifications where available. Guide the user to correct them only if needed
   (lookup_order is Read, issue_refund is Write).
   Check readiness for the published tool version. If the refund policy still
   needs acceptance, guide the user to the proposed rule for `issue_refund` in
   Agent onboarding. Onboarding creates the proposal. If it has not appeared,
   help resolve the onboarding status before continuing. Keep policy generation
   and Rego entry out of the handoff.
   Ask the user to review the proposed rule and choose **Accept** if it requires
   approval for the demo’s €180 refund and they agree. Assist supplies the test
   cases and the Console enables binding only after they pass. Leave testing to
   that workflow. If acceptance is blocked, use the reason shown in the Console.
   After acceptance, check readiness for the published tool version yourself.
   For an existing active policy, use its rule to establish whether this refund
   requires approval and skip acceptance. If the rule allows the refund outright
   or its coverage is unclear, pause before starting the run. Never use a live
   refund to probe the policy.
3. From the cookbook root run
   `python cookbook.py run governed-refund -- run ORD-1042` and keep the process
   alive. Guide the user to **Approvals**, filter by their Agent, and open the
   pending refund. Identify the tool as `issue_refund` and ask them to verify
   ORD-1042, 180, and EUR in the recorded inputs. If a field is missing or the request is
   ambiguous, leave it pending. Explain that approval lets the demo issue one
   simulated receipt. Let the user approve or reject in the Console and monitor
   the waiting process without requiring a second approval in chat.
4. After approval, read the original process output and verify exactly one
   simulated EUR 180 receipt for ORD-1042. Report the order, amount and receipt
   ID and end the walkthrough. Keep any actual execution or delivery failure
   visible. A separate audit request can use authorized scoped activity to
   correlate the execution Event with the approved Decision. The success output
   alone does not establish that link.
   Report zero effects while pending only from an instrumented test
   that observed it. Rejection, expiry, or timeout ends this attempt. Starting
   the command again creates a new demonstration.
