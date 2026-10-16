# Agent Pipeline Test

Small repository used to validate the Hermes multi-agent development pipeline.

## is_zero

`is_zero(value)` returns `True` only for the integer zero (integer subclasses
included) and `False` for any other integer. It raises `TypeError` for
booleans and non-integer inputs.

```python
from app import is_zero

is_zero(0)    # -> True
is_zero(42)   # -> False
is_zero(-7)   # -> False
is_zero(True) # raises TypeError
```
