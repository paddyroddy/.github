# Dropbox

This action can be used in the following manner:

```yaml
jobs:
  dropbox:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/dropbox@vx.y.z
        with:
          configfile-version: ${{ secrets.CONFIGFILE_VERSION }}
          files-to-upload: example.pdf
          oauth-app-key: ${{ secrets.OAUTH_APP_KEY }}
          oauth-app-secret: ${{ secrets.OAUTH_APP_SECRET }}
          oauth-refresh-token: ${{ secrets.OAUTH_REFRESH_TOKEN }}
```

where `x.y.z` is the `major.minor.patch` version of the action.