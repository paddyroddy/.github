# Safe-Settings

[Safe-Settings](https://github.com/github/safe-settings) is a way to manage
policy-as-code and apply repository settings across the account. A
[GitHub App](https://github.com/apps/paddyroddy-safe-settings) has been set up
which the [GitHub Action](../.github/workflows/safe-settings.yaml) uses to apply
the settings on a cron schedule.

## Configuration Files

There are four types of settings that can be applied:

- [Deployment](https://raw.githubusercontent.com/github/safe-settings/refs/heads/main-enterprise/docs/sample-settings/sample-deployment-settings.yml)
  which defines deployment and runtime settings.
- [Account](https://raw.githubusercontent.com/github/safe-settings/refs/heads/main-enterprise/docs/sample-settings/settings.yml)
  which can be used to define account-level settings.
- [Repository](https://raw.githubusercontent.com/github/safe-settings/refs/heads/main-enterprise/docs/sample-settings/repo.yml)
  which can be used to define repo-level settings.
- [Suborganisation](https://raw.githubusercontent.com/github/safe-settings/refs/heads/main-enterprise/docs/sample-settings/suborg.yml)
  which can be used to define suborganisation-level settings.

Beyond these example configurations one can read more about potential settings
to apply in the
[documentation](https://github.com/github/safe-settings/tree/main-enterprise/docs/github-settings).
The precedence order for configuration is `repository` > `suborganisation` >
`account`.

## The Settings in This Repository

### Deployment

The [deployment settings](deployment.yaml) are used to exclude archived
repositories from the Safe-Settings app. This is because these repositories are
read-only and hence cannot be modified. Rather than having the GitHub Action
fail on these repositories, they are excluded from the run.

### Account

The [account settings](account.yaml) are used to define general repository
settings for all repositories across the account. These settings are applied to
all repositories unless the precedence order is overridden by the
suborganisation settings (or repository settings).

### Suborganisation

The [suborganisation settings](suborgs/rulesets.yaml) are being used to define
[rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
for all repositories across the account. The `rulesets` available in the account
settings are defined for the account itself rather than individual repositories,
so they cannot be set via account settings. This hack is done through

```yaml
suborgrepos:
  - "*"
```

at the top of the file. Further explanation can be found in the
[Safe-Settings issues](https://github.com/github/safe-settings/issues/553#issuecomment-2552578978).
