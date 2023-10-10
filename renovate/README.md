# Renovate

To enable `Renovate` in a given repository, one must install and enable the
[GitHub application](https://github.com/apps/renovate).
One must then make a `.renovaterc.json` file in the repository, of the following
form.
Note, the two `/` is intentional.

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["github>paddyroddy/.github//renovate/default-config.json"]
}
```

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

The following branch rules to the base branch are also recommended.

- `Require status checks to pass before merging` ✅
  - `Require branches to be up to date before merging` ✅
    - List all status checks that should be mandatory here

If the repository requires pull requests, then one must also configure the
following.

- `Allow specified actors to bypass required pull requests` ✅
  - Add `renovate` here
