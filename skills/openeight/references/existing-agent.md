# Integrate an existing app

Inspect construction, sync/async execution, streams, tool dispatch, shutdown, MCP,
subagents, checkpointers, durable storage and existing test seams. Preserve meaningful
application tests and provider/model configuration. Choose the smallest supported seam:

- Supported LangChain/Deep Agents constructors: [managed Python](managed-python.md).
- Application-owned Python dispatch: [direct Python](direct-python.md).
- Node machine client with application-owned dispatch: [TypeScript](typescript.md).
- Existing span export for observation only: [OTEL](otel.md).

Use the installed version's public signatures and compatibility declaration. Do not invent
an AsyncClient, compiled graph wrapper, topology support or administrative client.
Unsupported topology/dependency conflicts need a concrete explanation and proposed changes
for review. Do not silently migrate frameworks, redesign storage or add duplicate wrappers.
Run existing regression tests plus meaningful allow/block/lifecycle checks at the actual
external effect boundary. Explain callback/provider/custom-node effects outside that seam.
Rollback only owned dependency/integration edits and verify the original app still runs.
