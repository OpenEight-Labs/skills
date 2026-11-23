# Existing OpenTelemetry export

Use this path for an application that already emits spans and wants observation.
It does not install SDK enforcement or authorize tool calls. If the user requires
governance, explain that an integration at tool dispatch is also required.

Preserve the application's tracer provider, instrumentation, sampling, and other
export destinations. Configure an OTLP/HTTP protobuf exporter for the explicitly
supplied OpenEight endpoint's `/v1/traces` route. Check the exporter's distinction
between a base endpoint that appends `/v1/traces` and a complete traces endpoint;
do not append the path twice. Keep credentials in environment/secret configuration.

The request headers are:

```text
Authorization: ApiKey <workspace-scoped-secret>
X-OpenEight-Agent-Name: <intended-agent-name>
X-OpenEight-Agent-Integration: otel
Content-Type: application/x-protobuf
```

Translate these into the exporter's documented header configuration and escaping;
header syntax differs between SDKs. Never put a real key in a committed config or
command history. Do not add `X-Organization-ID`. `X-Workspace-ID` is optional for
raw OTLP exporters and may only match the key-derived scope; omitting it avoids
an unnecessary selector.

Agent identity resolves/enrolls on authenticated ingestion. Unpinned keys can enroll
only untrusted Agents; promoted Agents need their own pinned key. Tool Catalog
registration and governance readiness are not prerequisites for OTLP observation.
Do not manufacture tool schemas or synthetic business activity to make Console
setup appear complete.

Flush and shut down the exporter for short-lived processes. A successful local
flush alone does not prove server persistence. Use a safe existing test invocation
and authorized scoped Run/Event reads or Console access to confirm persisted data
for the intended Agent. Report the result as observation only, with the actual
record identifiers and any unavailable read/Console acceptance step.
