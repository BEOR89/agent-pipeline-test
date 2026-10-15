import asyncio
import pytest
from app import add, subtract, multiply, divide, power, square, cube, modulo, noop_async_smoke

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

def test_noop_async_smoke():
    assert asyncio.run(noop_async_smoke()) == 'ok'


# --- System One shadow-routing pilot ---

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
