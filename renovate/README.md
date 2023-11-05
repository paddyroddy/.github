# Renovate

To enable `Renovate` in a given repository, one must install and enable the
[GitHub application](https://github.com/apps/renovate).
One must then make a `.renovaterc.json5` file in the repository, of the following
form.
Note, the two `/` is intentional.

```json5
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",
  extends: ["github>paddyroddy/.github//renovate/default-config.json5"],
}
```

One can then view the logs here <https://developer.mend.io/>.

## Automerging

To benefit from the automerging capabilities of the default config it is
_highly_ recommended having `required` status checks that run on anything that
`Renovate` updates.
In `GitHub Actions` this can be performed with the following at the top of the
relevant workflows, which will run `Renovate` on pull requests or branches.

```yaml
on:
  push:
    branches:
      - main
      - "renovate/**"
  pull_request:
```

The following `GitHub` settings are required.

- `Allow auto-merge`

### Branch Protection Rules

The following branch rules to the base branch are also recommended.

- `Require status checks to pass before merging` ✅
  - `Require branches to be up to date before merging` ✅
    - List all status checks that should be mandatory here

If the repository requires pull requests, then one must also configure the
following.

- `Allow specified actors to bypass required pull requests` ✅
  - Add `renovate` here

### Rulesets

Alternatively, if using rulesets you can modify and import the following two
rulesets.

The first one enables the `Restrict deletions`, `Block force pushes` settings,
as well as requiring a series of named status checks to pass.
No one is able to bypass these rules.
Make sure to add all status checks that you require.

```json
{
  "id": 1,
  "name": "Status Checks",
  "target": "branch",
  "source_type": "Repository",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": ["~DEFAULT_BRANCH"]
    }
  },
  "rules": [
    {
      "type": "deletion"
    },
    {
      "type": "non_fast_forward"
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "required_status_checks": [
          {
            "context": "linting",
            "integration_id": 15368
          }
        ],
        "strict_required_status_checks_policy": true
      }
    }
  ],
  "bypass_actors": []
}
```

The second one requires pull requests with at least `1` reviewer, but the
`actor_id` (which refers to `renovate`) is able to skip this for when automerge
(on branch) is enabled for the relevant dependency.

```json
{
  "id": 2,
  "name": "Pull Requests",
  "target": "branch",
  "source_type": "Repository",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": ["~DEFAULT_BRANCH"]
    }
  },
  "rules": [
    {
      "type": "pull_request",
      "parameters": {
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "dismiss_stale_reviews_on_push": false,
        "required_approving_review_count": 1,
        "required_review_thread_resolution": false
      }
    }
  ],
  "bypass_actors": [
    {
      "actor_id": 2740,
      "actor_type": "Integration",
      "bypass_mode": "always"
    }
  ]
}
```
