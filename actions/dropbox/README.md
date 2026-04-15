# Dropbox

This action can be used in the following manner:

```yaml
jobs:
  dropbox:
    runs-on: ubuntu-slim
    steps:
      - uses: paddyroddy/.github/actions/dropbox@vx
        with:
          # yamllint disable rule:line-length
          configfile-version: ${{ secrets.CONFIGFILE_VERSION }} # zizmor: ignore[secrets-outside-env]
          files-to-upload: $(find . -maxdepth 1 -name '*.pdf' -print)
          oauth-app-key: ${{ secrets.OAUTH_APP_KEY }} # zizmor: ignore[secrets-outside-env]
          oauth-app-secret: ${{ secrets.OAUTH_APP_SECRET }} # zizmor: ignore[secrets-outside-env]
          oauth-refresh-token: ${{ secrets.OAUTH_REFRESH_TOKEN }} # zizmor: ignore[secrets-outside-env]
          # yamllint enable rule:line-length
```

where `x` is the `major` version of the action.
