# Maintaining OpenEight skills

## Editing the skill

Maintain the installable bundle under `skills/openeight/`. The public OpenEight
SDK and cookbook own their APIs and recipes. Link to the relevant release when
the docs already explain a task. Add skill guidance where the assistant has a
decision to make, such as choosing an integration or handing control to a user.

Use the description in `SKILL.md` to say when the skill applies. Route individual
tasks to the relevant reference where the assistant chooses its next step.
Extend an existing reference when the same reader needs the new guidance.
Keep SDK distributions and recipe source in their upstream repository.

## Console handoffs

Machine keys belong in private configuration. Leave Agent key creation, policy
acceptance, and refund approval to the authorized Console user. For example,
Assist supplies the policy tests during onboarding. Ask the user to review the
proposed rule once, then check tool readiness after acceptance. The refund itself
requires a separate human decision.

## Reviewing and releasing changes

Read each changed instruction in the context where the assistant will encounter
it. Check that the intended prompt reaches the right reference and that nearby
tasks still work independently. An SDK installation alone should never trigger
a cookbook download or a Console approval.

Run `python scripts/validate.py` for metadata and bundled links. Exercise changed
runnable examples using the [testing guide](TESTING.md). Record results and
skipped checks in the PR. Keep test transcripts, recordings, secrets, and private
paths out of the repository.

Keep the bundled Apache-2.0 license and attribution notice in sync with the root
copies. Preserve third-party notices as described in [CONTRIBUTING.md](CONTRIBUTING.md).
Before merging SDK-dependent guidance to the installation branch, verify the
published packages and review the final merge tree under the [release guide](RELEASING.md).
Obtain authorization for remote creation, pushes, tags, publication, and live or
paid runs.
