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

## is_nonzero

`is_nonzero(value)` returns `True` for any nonzero integer (integer
subclasses included) and `False` only for the integer zero. It raises
`TypeError` for booleans and non-integer inputs.

```python
from app import is_nonzero

is_nonzero(0)    # -> False
is_nonzero(42)   # -> True
is_nonzero(-7)   # -> True
is_nonzero(True) # raises TypeError
```

## is_nonnegative

`is_nonnegative(value)` returns `True` for any integer greater than or
equal to zero (integer subclasses included) and `False` for negative
integers. It raises `TypeError` for booleans and non-integer inputs.

```python
from app import is_nonnegative

is_nonnegative(0)   # -> True
is_nonnegative(42)  # -> True
is_nonnegative(-7)  # -> False
is_nonnegative(True) # raises TypeError
```

## is_two

`is_two(value)` returns `True` only for the integer two (integer
subclasses included) and `False` for any other integer. It raises
`TypeError` for booleans and non-integer inputs.

```python
from app import is_two

is_two(2)    # -> True
is_two(42)   # -> False
is_two(-7)   # -> False
is_two(True) # raises TypeError
```

## is_three

`is_three(value)` returns `True` only for the integer three (integer
subclasses included) and `False` for any other integer. It raises
`TypeError` for booleans and non-integer inputs.

```python
from app import is_three

is_three(3)    # -> True
is_three(42)   # -> False
is_three(-7)   # -> False
is_three(True) # raises TypeError
```
