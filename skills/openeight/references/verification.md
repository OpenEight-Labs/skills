# Verification and failures

Verify the requested workflow. Record each result separately; installation,
authentication, delivery, and persistence are different claims. Machine keys do
not grant Console reads. Confirm persistence through authorized scoped reads or
explicit human Console acceptance.

## Shared checks

Check dependency resolution/imports, application startup, configuration, and
resource cleanup. For an authorized integrated run, confirm identity for the
intended Agent and check telemetry delivery/flush. Verify persisted Run/Event
data when the task calls for it. The first-refund walkthrough ends when the
original run produces the expected simulated receipt. Keep
flush/shutdown failures visible; a successful close alone does not prove storage.
For setup-only requests, stop at the requested setup boundary and identify any
integration checks still pending.

## Governed tool execution

Verify tool publication acknowledgement and readiness for the exact ToolVersion
before exercising governed dispatch. Publication is not readiness; readiness is
not per-attempt authorization. Freeze final arguments after middleware and check
authorization before each governed effect. Use fake business providers to confirm
that an initial allow reaches the handler once with the expected arguments, while
deny, pending approval, dry-run, and unavailable authorization reach it zero times.

If testing approval resume, wait for the authorized human to approve the exact
Decision, then use the release's exact-request replay flow. Approval state alone
is insufficient. For direct clients, require matching identities, a replay marker,
and the documented `approval_required` or `allow` verdict after approval; the
stored verdict need not change. Verify the resumed effect occurs once. Managed
integrations own this protocol; do not add a second replay or dispatch loop.

## Observation only

Verify the selected observation adapter or exporter, intended Agent identity,
telemetry delivery, and persistence. Report explicitly that policy is not enforced.
OTLP export needs no Tool Catalog registration, policy readiness, or Decide call.
Do not introduce those as onboarding prerequisites. For managed SDK observation,
check catalog publication where the adapter emits it, without requiring policy
readiness or Decisions. Never switch a governed integration to observation to
bypass failed authorization.

## Failures and handoff

Missing/revoked credentials and wrong scope stop live retries with sanitized errors
and concrete human steps. Catalog conflicts stop reconciliation; do not delete
tools, rename Agents, weaken schemas, or change policy. Keep SDK retries bounded
and do not add loops. Explain unsupported dependencies while preserving lockfiles.
Repeat setup preserves secrets, identity, durable state, and unrelated changes.

Report exact files changed, checks, and candidate/public input versions. Distinguish
simulations, local example checks, live runs, and human Console acceptance. Mark
unavailable checks as pending with their next action; mark checks outside the
selected workflow as not applicable rather than failed or pending.
