# SDK setup

Inspect runtime, package manager, manifest, lock and existing configuration. Verify the
official registry package, version, ownership and artifact digest before installing.
The bundled [support guidance](support.md) describes candidate qualification, not live registry
availability. Check the selected package in its official registry; a published
package alone does not qualify this skill. If unavailable, report the gate; never
fall back silently to a branch, editable install, unrelated package or sibling checkout.
An explicitly supplied reviewed wheel/source revision may be used for candidate qualification.
Record its immutable input and hash and label the result candidate-only.

Use normal package tools to update declarations and locks with the selected exact version.
Choose only relevant extras: LangChain is included in the Python candidate; deepagents,
langchain-durable, deepagents-durable, mcp and checkpoints-postgres are separate choices.
Check runtime requirements for the selected workflow using [support guidance](support.md).
For managed Python, match the installed SDK's complete framework tuple, not only
its Python version. The SDK's runtime range and the cookbook's documented range
are separate. TypeScript remains a private candidate targeting Node 24; emitted
JavaScript/declarations and an installed-tarball check do not qualify a public
registry package.

Check dependency resolution, installed version/origin, and imports in the project runtime.
For an install-only request, report those results and finish here.

When the user asks to connect an application, set OPENEIGHT_ENDPOINT, OPENEIGHT_AGENT_NAME and OPENEIGHT_API_KEY through existing
secret configuration. Do not print values or overwrite env files with templates.
Do not infer an endpoint or administrative authority. Remote endpoints require HTTPS.
Explain Console Agent/key creation or policy configuration to an authorized human;
no machine credential grants human Console read or administration rights.

For an authorized integrated check, verify application startup and perform a bounded identity/publication diagnostic using the selected client.
Keep installation, authentication, publication, readiness and persistence evidence separate.
