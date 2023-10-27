# Dropbox

This action can be used in the following manner:

```yaml
jobs:
  chktex:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/dropbox@vx.y.z
        with:
          files-to-upload: "example.pdf"
```

where `x.y.z` is the `major.minor.patch` version of the action.
