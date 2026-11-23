# TypeScript machine integration

Use Node 24 and the [distribution status](setup.md).
The SDK provides machine primitives; it does not intercept existing framework tool
calls. Adapt the application's actual dispatch boundary and retain its lifecycle.

```ts
import { MachineClient } from "@openeight/sdk";

function required(name: string): string {
  const value = process.env[name];
  if (!value) throw new Error(`Missing ${name}`);
  return value;
}

const client = new MachineClient({
  baseUrl: required("OPENEIGHT_ENDPOINT"),
  apiKey: required("OPENEIGHT_API_KEY"),
  agentName: required("OPENEIGHT_AGENT_NAME"),
});

try {
  const readiness = await client.getToolReadiness([]);
  // Inspect readiness without logging schemas, inputs, or credentials.
} finally {
  await client.close();
}
```

This diagnoses the authenticated current catalog; it does not govern a tool call.
For a persistent application, own the client in its startup/shutdown lifecycle.
Use `MachineClient` for agent traffic; this public SDK has no human-session client.

Read the [machine-client walkthrough and approval replay rules](https://github.com/OpenEight-Labs/openeight/blob/main/sdk/typescript/README.md#machine-client)
and [public exports](https://github.com/OpenEight-Labs/openeight/blob/main/sdk/typescript/src/index.ts)
before wiring dispatch. Select the tag or immutable commit corresponding to the
installed artifact; these `main` links are discovery entry points, not version
pins. Cross-check the examples against the installed package declarations. If the
matching contract is unavailable, report that gap rather than inventing a wrapper.

Report actual schemas using `ToolRegistration` and `registerTools`; retain
acknowledged identities and conditional-update semantics.
Fetch exact current readiness, collect final arguments with `collectSelectedValues`,
prepare a Run identity and Decision with the documented `prepareRunIdentity`,
`governedRun`, and `prepareDecision` APIs. An initial valid `allow` from `decide`
authorizes that attempt. Pending/denied/dry-run/unavailable authorization executes
no handler.

After `approval_required`, wait for `approved` on that exact Decision, then replay
the unchanged prepared request with the same machine actor. Require matching
identities, `replayed=true`, and verdict `approval_required` or `allow`. Approval
does not change the stored verdict; a state read alone does not authorize execution.
Other states/verdicts and replay failures refuse execution.

Preserve the prepared Decision envelope across identical retries and linked Events;
do not blindly repeat external effects. Record truthful executed-tool Events, flush
acknowledged delivery, and close the Run/client. Verify allow and block behavior
with stubbed external services and check persisted telemetry through authorized
reads. Missing policy configuration remains a human Console step. Report any
execution paths outside this boundary.
