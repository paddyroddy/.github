# Dropbox

This action can be used in the following manner:

```yaml
jobs:
  dropbox:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    steps:
      - uses: paddyroddy/.github/actions/dropbox@vx
        env:
          CONFIGFILE_VERSION: ${{ secrets.CONFIGFILE_VERSION }}
          OAUTH_APP_KEY: ${{ secrets.OAUTH_APP_KEY }}
          OAUTH_APP_SECRET: ${{ secrets.OAUTH_APP_SECRET }}
          OAUTH_REFRESH_TOKEN: ${{ secrets.OAUTH_REFRESH_TOKEN }}
        with:
          configfile-version: ${{ env.CONFIGFILE_VERSION }}
          files-to-upload: $(find . -maxdepth 1 -name '*.pdf' -print)
          oauth-app-key: ${{ env.OAUTH_APP_KEY }}
          oauth-app-secret: ${{ env.OAUTH_APP_SECRET }}
          oauth-refresh-token: ${{ env.OAUTH_REFRESH_TOKEN }}
```

where `x` is the `major` version of the action.
