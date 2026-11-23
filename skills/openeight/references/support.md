# Support and compatibility

These references cover Python `openeight` 0.0.1 and the TypeScript
`@openeight/sdk` 0.0.1 candidate.

| Workflow | Runtime guidance |
| --- | --- |
| Python SDK | The SDK declares Python `>=3.11,<3.16`. For managed integrations, check the release's compatibility registry for the exact Python and framework versions. |
| Cookbook | Use Python 3.11–3.14 for cookbook recipes. |
| TypeScript SDK | The candidate targets Node.js 24. Check package availability before installation. |

The managed Python examples target LangChain 1.4.3, langchain-core 1.6.7,
and Deep Agents 0.7.23. Check the application's installed SDK version, public
signatures, and framework dependencies before applying an example. Preserve
existing dependency locks and install only the extras the integration uses.
