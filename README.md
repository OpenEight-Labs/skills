# OpenEight Skills

Agent skills for coding assistants working with OpenEight. Use them to govern tool calls, observe agent runs, or try an integration in a working example.

## Skills

| Skill | Description |
| --- | --- |
| [openeight](skills/openeight/SKILL.md) | Set up the OpenEight SDK, connect an existing agent to governance or observation, run a cookbook example, or check an integration. |

## Installation

### Skills CLI

From your project directory, run:

```bash
npx skills add OpenEight-Labs/skills --skill openeight
```

Choose your coding assistant when prompted.

### Manual installation with Git

From your project directory, clone the release into a sibling folder. For a fresh Codex project installation, copy the complete skill into `.agents/skills/`:

```bash
git clone --branch v0.1.0 --depth 1 https://github.com/OpenEight-Labs/skills.git ../openeight-skills
mkdir -p .agents/skills
cp -R ../openeight-skills/skills/openeight .agents/skills/
```

For Claude Code, use `.claude/skills/` in the last two commands. You can remove the clone after copying the skill.

See the [compatibility guide](skills/openeight/references/support.md) for SDK versions and runtime requirements.

## Prerequisites

You can install the SDK or try a local cookbook sample before connecting to OpenEight. To connect a running agent, select or create your Agent in the [OpenEight Console](https://app.openeight.ai). Set the following variables using your exact Agent name and its machine API key.

```bash
export OPENEIGHT_ENDPOINT='https://app.openeight.ai'
export OPENEIGHT_AGENT_NAME='<your-agent-name>'
export OPENEIGHT_API_KEY='<your-agent-machine-key>'
```

Keep keys in your agent’s private configuration and out of chat. For a recipe that calls a model, you’ll also need credentials for your chosen model provider. You review policies and decide approval requests in the Console.

## Usage

With the skill installed, open your agent’s folder and describe what you want to do. For a new demo agent, start in an empty folder.

| Task | Example prompt |
| --- | --- |
| Install the SDK | Install the OpenEight SDK for this agent and verify the installation. |
| Govern tool calls | Connect this agent to OpenEight so its tool calls follow our policies. Keep my framework and model configuration. |
| Observe runs | Send this application’s existing OpenTelemetry spans to OpenEight for observation. |
| Try a local example | Run the Customer Support cookbook agent locally. |
| Walk through an approval | Build a refund agent and walk me through approving its first refund in OpenEight |
| Check an integration | Check this OpenEight integration and explain what still needs setup. |

## Contributing

To submit a change, follow the [contribution guide](CONTRIBUTING.md).

## Feedback & Requests

To report a problem, share your prompt, your coding assistant, and what went wrong. To request a skill, describe the task you’d like it to handle. For sensitive reports, follow the [security reporting guide](SECURITY.md).
