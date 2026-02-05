# Dropbox

This action can be used in the following manner:

```yaml
jobs:
  dropbox:
    runs-on: ubuntu-slim
    steps:
      - uses: paddyroddy/.github/actions/dropbox@vx
        with:
          configfile-version: ${{ secrets.CONFIGFILE_VERSION }}
          files-to-upload: $(find . -maxdepth 1 -name '*.pdf' -print)
          oauth-app-key: ${{ secrets.OAUTH_APP_KEY }}
          oauth-app-secret: ${{ secrets.OAUTH_APP_SECRET }}
          oauth-refresh-token: ${{ secrets.OAUTH_REFRESH_TOKEN }}
```

where `x` is the `major` version of the action.
