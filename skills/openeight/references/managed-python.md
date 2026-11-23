# Managed Python integration

Use the SDK-owned constructor where the application already constructs a supported
LangChain or Deep Agents agent. Read the target release's compatibility registry;
Python version support alone does not qualify the installed framework tuple.

For LangChain, change the constructor import and add explicit `OpenEightConfig`:

```python
import os

from openeight import OpenEightConfig
from openeight.langchain import create_agent


async def check_onboarding(model, tools, application_middleware):
    async with create_agent(
        model=model,
        tools=tools,
        middleware=application_middleware,
        openeight=OpenEightConfig(
            endpoint=os.environ["OPENEIGHT_ENDPOINT"],
            credential=os.environ["OPENEIGHT_API_KEY"],
            agent_name=os.environ["OPENEIGHT_AGENT_NAME"],
        ),
    ) as agent:
        await agent.aflush()
        catalog = agent.catalog_snapshot()
        if not catalog.facts or not catalog.publication_complete:
            return False
        status = await agent.areadiness()
        return not status.unpublished and status.readiness.fully_policy_ready
```

Use this check for a governed agent with tools. If it returns false, inspect
publication results and exact ToolVersion readiness to guide the next Console
step. After the check passes and the integrated run is authorized, invoke with
`await agent.ainvoke(request)` inside an active context. In a server, keep the
owner in the application lifespan and reuse it across requests. For synchronous applications,
use `with create_agent(...) as agent` and `agent.invoke(request)`. Never call the
blocking API from an active event loop. Preserve supported application options and
model/provider credentials; the SDK does not select a model.

Deep Agents uses `from openeight.deepagents import create_deep_agent` with the
same `openeight=OpenEightConfig(...)` and context ownership. Preserve supported backend,
skills, middleware, and declarative subagent options. Its generated filesystem and
delegation tools also enter the catalog. Use `catalog_snapshot().bindings` to
relate native names/child paths to catalog identities; do not rename these tools
or change catalog naming modes to simplify onboarding.

Do not attach middleware to an already compiled graph, instrument it with an
invented wrapper, or add manual `register_tools()` to the managed path. If the
application uses unsupported graph/history APIs, structured output, provider-side
tools, remote/compiled children, or dynamic topology, inspect the exact release
contract and explain the gap before restructuring the application. Preserve
existing durable/checkpoint behavior. Enabling SDK durable execution is a separate
storage/recovery decision, not a routine constructor substitution.

Applications own supplied models, business resources, stores, and savers. Borrowed
resources must outlive the SDK context. Resources needing the SDK's owner loop use
the documented `ManagedResources` factory; do not combine it with directly supplied
stores/savers. Enter after fork; maintain one execution mode per owner. Preserve
stream cleanup, cancellation, and orderly shutdown rather than returning a closed
agent from a temporary context.

## Observation choice

When observation is requested, use the selected adapter's separate `observe`
constructor, with `openeight=OpenEightConfig(...)` after checking its installed signature. It adds observation without Decide. It must never be a
fallback for blocked governed execution.

## Publication and execution checks

Construction performs no network I/O. Context entry validates the graph and starts
bounded background tool-fact publication; MCP discovery can contact external
sources. It does not call a model/tool on its own. Entry returning is not a receipt.

For an async owner, use `await agent.aflush()` and inspect
`agent.catalog_snapshot()`, including `publication_complete`, acknowledged
registration results, and bindings. For sync use `agent.flush()` and the same
snapshot. Inspect `agent.delivery_status()` for delivery failures/loss. Avoid
dumping the whole snapshot, which includes application schemas. An empty tool
catalog sends no registration request and creates no Agent completion receipt;
verify identity through an actual acknowledged request/read instead.

Use `await agent.areadiness()` or synchronous `agent.readiness()` to diagnose
current tool readiness. Publication reports facts; humans configure write-policy
inputs and activate policy coverage. Governed dispatch refreshes contracts, and
writes cross Decide with the final arguments. Missing readiness, denial, pending
approval, dry run, or unavailable authorization must not execute a handler. Default
blocks can appear as safe tool feedback, so inspect handler-call evidence rather
than relying on an exception or model response.

The candidate defaults to inline approval polling with a one-hour timeout when no
approval configuration is supplied. Inspect that behavior before invocation and
explain its operational effect; obtain the consequential waiting/resume choice.
Do not silently change approval timeouts or resolve approvals. Optional telemetry capture remains `none`; required governance
inputs and native recovery data have their own contracts.

Effects inside callbacks, custom graph nodes, backend code, and provider execution
outside the actual governed handler remain application-owned. State these limits
when reporting coverage. MCP credentials remain separate from OpenEight keys;
preserve explicit sources and their principal/deployment binding identities.
