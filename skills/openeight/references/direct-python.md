# Custom Python tool dispatch

The synchronous `Client` supplies primitives, not automatic framework interception.
Use this path when application code owns the actual tool dispatch and can enforce
the returned authorization before every relevant side effect. There is no core
`AsyncClient`; do not invent async methods or block an async application's event
loop. Follow the application's supported offloading/lifecycle pattern if needed.

```python
from openeight import Client


def inspect_current_readiness():
    with Client.from_env() as client:
        return client.get_tool_readiness([])
```

This is an authenticated current-catalog diagnostic, not a complete integration
or permission to execute. The empty selector asks for this Agent's current catalog.
Direct construction instead takes `Client(base_url, api_key=..., agent_name=...)`.

Start with the [direct-client API reference](https://openeight.ai/docs/reference/direct-sdk?language=python&integration=direct&execution=sync)
for registration, readiness, and dispatch. Read the SDK's
[request preparation and recovery guide](https://github.com/OpenEight-Labs/openeight/blob/main/sdk/python/docs/direct-recovery.md)
for retry identity and approval replay, and its
[public exports](https://github.com/OpenEight-Labs/openeight/blob/main/sdk/python/openeight/__init__.py)
for the available types.

These links are discovery entry points, not version pins. For GitHub references,
select the tag or immutable commit corresponding to the installed artifact instead
of assuming `main` matches. Cross-check the walkthrough against that revision and
the installed signatures for `ToolRegistration`, `Client.register_tools`,
`Client.governed_run`, `Client.decide_prepared`, and `GovernedRun.submit_event`.
If matching API details are unavailable, complete configuration and inspection,
state the missing reference, and do not fabricate a Decision payload or wrapper.

Implement these boundaries using that release's supported APIs:

1. Report actual tool name, description, and input schema through `register_tools`.
   This reports facts only. Take Tool/ToolVersion identities from acknowledged
   results. First discovery omits compare-and-swap conditions; a changed existing
   schema uses the last acknowledged Tool/current-version pair. Preserve those
   conditions on identical transport retries; stop on a catalog conflict.
2. Inspect current readiness and obtain the configured contract and selectors.
   Pending schemas do not authorize execution. Do not fabricate IDs, classify a
   write as a read, or generate policy bindings through machine credentials.
3. Own a logical execution with the supported Run lifecycle. Freeze the actual
   final tool arguments after application middleware. For governed writes, request
   Decide using the exact configured inputs. An initial valid allow authorizes
   that attempt; approval-required results follow the separate replay flow below. Readiness is never a substitute for a Decision. Do not reuse
   an allow for different arguments or blindly retry a side effect.
4. Pending approval executes nothing. If approval support is requested, wait for
   `approved` on the exact Decision, then replay the unchanged prepared request
   with the same machine actor. Require matching identities, `replayed=True`, and
   verdict `approval_required` or `allow`; approval does not change the stored
   verdict. Approval state alone is not execution authority. Denied, dry-run,
   rejected, expired, or failed authorization executes nothing. Keep observation
   explicit and never use it to bypass a blocked governed call.
5. Record truthful executed-tool telemetry with the supported Event/Run
   APIs. Flush tool Events before Run completion, inspect delivery errors, and
   close owned resources. Do not emit a successful tool Event for a blocked call
   or claim an external effect solely from an allow Decision.

Test the actual handler boundary with an external-service stub: an allow reaches
it once with the expected arguments, and deny/pending/unavailable authorization
never reaches it. Check existing retry paths and middleware for bypasses. A Client
instance alone governs no calls; report execution paths that remain outside it.
