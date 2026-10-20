import asyncio
import pytest
from app import add, subtract, multiply, divide, power, square, cube, modulo, is_even, is_odd, is_positive, is_negative, is_zero, is_nonzero, is_nonnegative, is_nonpositive, is_one, is_two, is_three, noop_async_smoke

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-4, -6) == 2
    assert subtract(10.5, 0.5) == 10.0

def test_multiply_positive_integers():
    assert multiply(4, 3) == 12

def test_multiply_negative_and_positive_integers():
    assert multiply(-2, 5) == -10

def test_multiply_float_and_integer():
    assert multiply(2.5, 4) == 10.0

def test_divide():
    assert divide(8, 2) == 4
    assert divide(5, 2) == 2.5
    assert divide(-9, 3) == -3
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 3) == -8

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0

def test_cube():
    assert cube(2) == 8
    assert cube(-3) == -27
    assert cube(0) == 0

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(14, 7) == 0
    assert modulo(-10, 3) == 2
    assert modulo(10.5, 4) == 2.5

def test_is_even_even_integer():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(-6) is True

def test_is_even_odd_integer():
    assert is_even(3) is False
    assert is_even(-5) is False
    assert is_even(1) is False

def test_is_even_rejects_non_integer_inputs():
    for bad in [2.5, "4", True, None]:
        with pytest.raises(TypeError):
            is_even(bad)


def test_is_odd_odd_integer():
    assert is_odd(1) is True
    assert is_odd(3) is True
    assert is_odd(41) is True
    assert is_odd(10**6 + 1) is True


def test_is_odd_negative_odd_integer():
    assert is_odd(-1) is True
    assert is_odd(-5) is True
    assert is_odd(-(10**6 + 1)) is True


def test_is_odd_even_integer():
    assert is_odd(0) is False
    assert is_odd(2) is False
    assert is_odd(-4) is False
    assert is_odd(10**6) is False


def test_is_odd_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_odd(_MyInt(3)) is True
    assert is_odd(_MyInt(-7)) is True
    assert is_odd(_MyInt(4)) is False


def test_is_odd_rejects_non_integer_inputs():
    for bad in [2.5, "3", True, False, None]:
        with pytest.raises(TypeError):
            is_odd(bad)


def test_is_positive_positive_integer():
    assert is_positive(1) is True
    assert is_positive(7) is True
    assert is_positive(10**6) is True


def test_is_positive_zero_is_not_positive():
    assert is_positive(0) is False


def test_is_positive_negative_integer():
    assert is_positive(-1) is False
    assert is_positive(-42) is False


def test_is_positive_rejects_non_integer_inputs():
    for bad in [2.5, "4", True, False, None]:
        with pytest.raises(TypeError):
            is_positive(bad)

def test_is_negative_negative_integer():
    assert is_negative(-1) is True
    assert is_negative(-42) is True
    assert is_negative(-(10**6)) is True


def test_is_negative_zero_is_not_negative():
    assert is_negative(0) is False


def test_is_positive_is_not_negative():
    assert is_negative(1) is False
    assert is_negative(7) is False
    assert is_negative(10**6) is False


def test_is_negative_rejects_non_integer_inputs():
    for bad in [2.5, "4", True, False, None]:
        with pytest.raises(TypeError):
            is_negative(bad)


def test_is_zero_zero_integer():
    assert is_zero(0) is True


def test_is_zero_nonzero_integer():
    assert is_zero(1) is False
    assert is_zero(-1) is False
    assert is_zero(42) is False
    assert is_zero(10**6) is False


def test_is_zero_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_zero(_MyInt(0)) is True
    assert is_zero(_MyInt(7)) is False


def test_is_zero_rejects_non_integer_inputs():
    for bad in [2.5, "0", True, False, None]:
        with pytest.raises(TypeError):
            is_zero(bad)


def test_is_nonzero_nonzero_integer():
    assert is_nonzero(1) is True
    assert is_nonzero(-1) is True
    assert is_nonzero(42) is True
    assert is_nonzero(10**6) is True


def test_is_nonzero_zero_is_not_nonzero():
    assert is_nonzero(0) is False


def test_is_nonzero_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_nonzero(_MyInt(0)) is False
    assert is_nonzero(_MyInt(7)) is True


def test_is_nonzero_rejects_non_integer_inputs():
    for bad in [2.5, "1", True, False, None]:
        with pytest.raises(TypeError):
            is_nonzero(bad)


def test_is_nonnegative_nonnegative_integer():
    assert is_nonnegative(0) is True
    assert is_nonnegative(1) is True
    assert is_nonnegative(42) is True
    assert is_nonnegative(10**6) is True


def test_is_nonnegative_negative_integer():
    assert is_nonnegative(-1) is False
    assert is_nonnegative(-42) is False
    assert is_nonnegative(-(10**6)) is False


def test_is_nonnegative_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_nonnegative(_MyInt(0)) is True
    assert is_nonnegative(_MyInt(7)) is True
    assert is_nonnegative(_MyInt(-3)) is False


def test_is_nonnegative_rejects_non_integer_inputs():
    for bad in [2.5, "1", True, False, None]:
        with pytest.raises(TypeError):
            is_nonnegative(bad)


def test_is_nonpositive_negative_and_zero():
    assert is_nonpositive(0) is True
    assert is_nonpositive(-1) is True
    assert is_nonpositive(-42) is True
    assert is_nonpositive(-(10**6)) is True


def test_is_nonpositive_positive_integer():
    assert is_nonpositive(1) is False
    assert is_nonpositive(7) is False
    assert is_nonpositive(10**6) is False


def test_is_nonpositive_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_nonpositive(_MyInt(0)) is True
    assert is_nonpositive(_MyInt(-3)) is True
    assert is_nonpositive(_MyInt(42)) is False


def test_is_nonpositive_rejects_non_integer_inputs():
    for bad in [2.5, "0", True, False, None]:
        with pytest.raises(TypeError):
            is_nonpositive(bad)


def test_is_one_one_integer():
    assert is_one(1) is True


def test_is_one_non_one_integer():
    assert is_one(0) is False
    assert is_one(-1) is False
    assert is_one(2) is False
    assert is_one(42) is False
    assert is_one(10**6) is False


def test_is_one_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_one(_MyInt(1)) is True
    assert is_one(_MyInt(0)) is False
    assert is_one(_MyInt(2)) is False


def test_is_one_rejects_non_integer_inputs():
    for bad in [2.5, "1", True, False, None]:
        with pytest.raises(TypeError):
            is_one(bad)


def test_is_two_two_integer():
    assert is_two(2) is True


def test_is_two_non_two_integer():
    assert is_two(0) is False
    assert is_two(1) is False
    assert is_two(3) is False
    assert is_two(42) is False
    assert is_two(10**6) is False


def test_is_two_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_two(_MyInt(2)) is True
    assert is_two(_MyInt(1)) is False
    assert is_two(_MyInt(3)) is False


def test_is_two_rejects_non_integer_inputs():
    for bad in [2.5, "2", True, False, None]:
        with pytest.raises(TypeError):
            is_two(bad)


def test_is_three_three_integer():
    assert is_three(3) is True


def test_is_three_non_three_integer():
    assert is_three(0) is False
    assert is_three(1) is False
    assert is_three(2) is False
    assert is_three(42) is False
    assert is_three(10**6) is False


def test_is_three_accepts_integer_subclass():
    class _MyInt(int):
        pass

    assert is_three(_MyInt(3)) is True
    assert is_three(_MyInt(1)) is False
    assert is_three(_MyInt(2)) is False


def test_is_three_rejects_non_integer_inputs():
    for bad in [2.5, "3", True, False, None]:
        with pytest.raises(TypeError):
            is_three(bad)


def test_noop_async_smoke():
    assert asyncio.run(noop_async_smoke()) == 'ok'


# --- System One shadow-routing pilot ---

import app
from app import primary_add, system_one_add, shadow_route, route_operation

def test_shadow_route_disabled_does_not_invoke_shadow():
    calls = []

    def spy_shadow(a, b):
        calls.append((a, b))
        return 999

    value, report = shadow_route(primary_add, spy_shadow, 2, 3)
    assert value == 5
    assert calls == []
    assert report.shadow_enabled is False
    assert report.shadow_value is None
    assert report.shadow_error is None
    assert report.divergent is False
    assert report.primary_value == 5

def test_shadow_route_divergent_shadow_does_not_change_value():
    def wrong_shadow(a, b):
        return 42

    value, report = shadow_route(primary_add, wrong_shadow, 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.divergent is True
    assert report.shadow_value == 42
    assert report.shadow_error is None

def test_shadow_route_raising_shadow_is_captured():
    def raising_shadow(a, b):
        raise ValueError("boom")

    value, report = shadow_route(primary_add, raising_shadow, 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.shadow_error == "ValueError: boom"
    assert report.shadow_value is None
    assert report.divergent is False

def test_shadow_route_parity_shadow():
    value, report = shadow_route(primary_add, system_one_add, 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.shadow_value == 5
    assert report.divergent is False
    assert report.shadow_error is None

@pytest.mark.parametrize("op, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 3, 2),
    ("multiply", 4, 3, 12),
    ("divide", 8, 2, 4),
    ("power", 2, 3, 8),
    ("modulo", 10, 3, 1),
])
def test_route_operation_shadow_enabled_parity(op, a, b, expected):
    value, report = route_operation(op, a, b, shadow_enabled=True)
    assert value == expected
    assert report.divergent is False
    assert report.shadow_error is None

@pytest.mark.parametrize("op, a, b, expected", [
    ("subtract", 5, 3, 2),
    ("multiply", 4, 3, 12),
    ("divide", 8, 2, 4),
    ("power", 2, 3, 8),
    ("modulo", 10, 3, 1),
])
def test_route_operation_ops_without_candidate_shadow_themselves(op, a, b, expected):
    value, report = route_operation(op, a, b, shadow_enabled=True)
    assert value == expected
    assert report.primary_handler == op
    assert report.shadow_handler == op
    assert report.shadow_value == expected

def test_route_operation_add_uses_system_one_shadow():
    value, report = route_operation("add", 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.primary_handler == "add"
    assert report.shadow_handler == "system_one_add"
    assert report.shadow_value == 5
    assert report.divergent is False
    assert report.shadow_error is None

def test_route_operation_divergent_shadow_returns_primary(monkeypatch):
    def divergent_shadow(a, b):
        return 42

    monkeypatch.setitem(app.SYSTEM_ONE_OPS, "add", divergent_shadow)
    value, report = route_operation("add", 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.primary_value == 5
    assert report.divergent is True
    assert report.shadow_value == 42
    assert report.shadow_error is None

def test_route_operation_add_shadow_disabled_reports_system_one_handler():
    value, report = route_operation("add", 2, 3)
    assert value == 5
    assert report.shadow_handler == "system_one_add"
    assert report.shadow_value is None

def test_route_operation_raising_shadow_returns_primary(monkeypatch):
    def raising_shadow(a, b):
        raise RuntimeError("shadow down")

    monkeypatch.setitem(app.SYSTEM_ONE_OPS, "add", raising_shadow)
    value, report = route_operation("add", 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.primary_value == 5
    assert report.shadow_error == "RuntimeError: shadow down"
    assert report.shadow_value is None
    assert report.divergent is False

class _Incomparable:
    """Value whose comparisons raise; addition yields another instance."""

    def __add__(self, other):
        return _Incomparable()

    def __eq__(self, other):
        raise TypeError("cannot compare")

    def __ne__(self, other):
        raise TypeError("cannot compare")

    __hash__ = object.__hash__

def test_shadow_route_comparison_error_is_captured():
    primary_value = _Incomparable()
    shadow_value = _Incomparable()
    value, report = shadow_route(lambda a, b: primary_value,
                                 lambda a, b: shadow_value,
                                 1, 2, shadow_enabled=True)
    assert value is primary_value
    assert report.primary_value is primary_value
    assert report.shadow_value is shadow_value
    assert report.shadow_error == "comparison failed: TypeError: cannot compare"
    assert report.divergent is False

class _Unbooleanable:
    def __bool__(self):
        raise ValueError("ambiguous truth value")

class _AmbiguousCompare:
    def __ne__(self, other):
        return _Unbooleanable()

    __hash__ = object.__hash__

def test_shadow_route_ambiguous_comparison_result_is_captured():
    value, report = shadow_route(lambda a, b: 5,
                                 lambda a, b: _AmbiguousCompare(),
                                 2, 3, shadow_enabled=True)
    assert value == 5
    assert report.shadow_error == "comparison failed: ValueError: ambiguous truth value"
    assert report.divergent is False

def test_route_operation_add_comparison_error_returns_primary():
    value, report = route_operation("add", _Incomparable(), _Incomparable(),
                                    shadow_enabled=True)
    assert isinstance(value, _Incomparable)
    assert report.primary_value is value
    assert report.shadow_handler == "system_one_add"
    assert isinstance(report.shadow_value, _Incomparable)
    assert report.shadow_error == "comparison failed: TypeError: cannot compare"
    assert report.divergent is False

def test_route_operation_shadow_disabled():
    value, report = route_operation("multiply", 4, 3)
    assert value == 12
    assert report.shadow_enabled is False
    assert report.shadow_value is None
    assert report.shadow_error is None
    assert report.divergent is False

def test_route_operation_unknown_op():
    with pytest.raises(ValueError):
        route_operation("sqrt", 4, 2)

def test_route_operation_primary_error_propagates():
    with pytest.raises(ZeroDivisionError):
        route_operation("divide", 1, 0)

def test_primary_and_system_one_add_parity():
    for a, b in [(2, 3), (-1, 1), (0, 0), (2.5, 0.5)]:
        assert primary_add(a, b) == system_one_add(a, b)
