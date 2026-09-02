# Utsikten

Small utilities that do not depend on FastAPI response helpers.

## Version tags

`format_version_tag` validates that a tag is a simple `X.Y.Z` string:

```python
from tunsberg.utsikten import format_version_tag

format_version_tag('1.2.3')  # returns "1.2.3"
format_version_tag('v1.2.3')  # raises ValueError
```

Use this when preparing releases so Git tags and `tunsberg.__version__` stay aligned.
