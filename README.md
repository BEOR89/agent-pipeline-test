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

## is_four

`is_four(value)` returns `True` only for the integer four (integer
subclasses included) and `False` for any other integer. It raises
`TypeError` for booleans and non-integer inputs.

```python
from app import is_four

is_four(4)    # -> True
is_four(42)   # -> False
is_four(-7)   # -> False
is_four(True) # raises TypeError
```

## is_five

`is_five(value)` returns `True` only for the integer five (integer
subclasses included) and `False` for any other integer. It raises
`TypeError` for booleans and non-integer inputs.

```python
from app import is_five

is_five(5)    # -> True
is_five(42)   # -> False
is_five(-7)   # -> False
is_five(True) # raises TypeError
```

## is_six

`is_six(value)` returns `True` only for the integer six (integer
subclasses included) and `False` for any other integer. It raises
`TypeError` for booleans and non-integer inputs.

```python
from app import is_six

is_six(6)    # -> True
is_six(42)   # -> False
is_six(-7)   # -> False
is_six(True) # raises TypeError
```
