def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """Returns product of two numbers."""
    return a * b

def divide(a, b):
    """Returns quotient of two numbers (raises ZeroDivisionError if divisor is zero)."""
    return a / b

def power(a, b):
    """Returns a raised to the power of b"""
    return a ** b

def square(a):
    """Returns the square of a number."""
    return a ** 2

def cube(a):
    """Returns the cube of a number."""
    return a ** 3

def modulo(a, b):
    return a % b


def is_even(value):
    """Returns True if value is an even integer, False if odd.

    Raises TypeError for non-integer inputs. bool is explicitly rejected even
    though it is a subclass of int.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_even accepts integer inputs only")
    return value % 2 == 0


def is_odd(value):
    """Returns True if value is an odd integer, False if even.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_odd accepts integer inputs only")
    return value % 2 == 1


def is_positive(value):
    """Returns True if value is an integer greater than zero, False otherwise.

    Raises TypeError for non-integer inputs. bool is explicitly rejected even
    though it is a subclass of int.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_positive accepts integer inputs only")
    return value > 0


def is_negative(value):
    """Returns True if value is an integer less than zero, False otherwise.

    Raises TypeError for non-integer inputs. bool is explicitly rejected even
    though it is a subclass of int.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_negative accepts integer inputs only")
    return value < 0


def is_zero(value):
    """Returns True if value is the integer zero, False for any other integer.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_zero accepts integer inputs only")
    return value == 0


def is_nonzero(value):
    """Returns True for any nonzero integer, False only for the integer zero.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_nonzero accepts integer inputs only")
    return value != 0


def is_nonnegative(value):
    """Returns True for any integer greater than or equal to zero, False for negative integers.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_nonnegative accepts integer inputs only")
    return value >= 0


def is_nonpositive(value):
    """Returns True for any integer less than or equal to zero, False for positive integers.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_nonpositive accepts integer inputs only")
    return value <= 0


def is_one(value):
    """Returns True if value is the integer one, False for any other integer.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_one accepts integer inputs only")
    return value == 1


def is_two(value):
    """Returns True if value is the integer two, False for any other integer.

    Integer subclasses are accepted. bool is explicitly rejected even though
    it is a subclass of int; other non-integer inputs raise TypeError.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("is_two accepts integer inputs only")
    return value == 2


async def noop_async_smoke():
    return 'ok'


# ---------------------------------------------------------------------------
# System One shadow-routing pilot
#
# A "system one" shadow handler runs alongside the primary handler on the same
# inputs. Its output is captured in a ShadowReport and NEVER changes the value
# returned to the caller. The shadow is dormant unless shadow_enabled=True is
# passed explicitly per call.
# ---------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class ShadowReport:
    """Outcome of one shadow-routed call."""
    primary_handler: str
    shadow_handler: str
    shadow_enabled: bool
    primary_value: Any
    shadow_value: Optional[Any]
    shadow_error: Optional[str]
    divergent: bool

def primary_add(a, b):
    """Current primary handler for the pilot pair."""
    return add(a, b)

def system_one_add(a, b):
    """System One candidate for add.

    Intentionally identical to primary_add at pilot start (parity baseline).
    Future work replaces this implementation; divergences are tracked via
    ShadowReport.
    """
    return add(a, b)

def shadow_route(primary, shadow, a, b, *, shadow_enabled=False):
    """Returns (primary_value, ShadowReport).

    The primary result is always returned unchanged; primary exceptions
    propagate. The shadow is only invoked when shadow_enabled is True, and
    any exception it raises is captured in the report. An exception raised
    while comparing the shadow value to the primary value is also captured
    (prefixed with "comparison failed: "); divergent stays False in that case.
    """
    primary_value = primary(a, b)
    shadow_value = None
    shadow_error = None
    divergent = False
    if shadow_enabled:
        try:
            shadow_value = shadow(a, b)
        except Exception as exc:
            shadow_error = f"{type(exc).__name__}: {exc}"
        else:
            try:
                divergent = bool(shadow_value != primary_value)
            except Exception as exc:
                shadow_error = f"comparison failed: {type(exc).__name__}: {exc}"
    report = ShadowReport(
        primary_handler=getattr(primary, "__name__", repr(primary)),
        shadow_handler=getattr(shadow, "__name__", repr(shadow)),
        shadow_enabled=shadow_enabled,
        primary_value=primary_value,
        shadow_value=shadow_value,
        shadow_error=shadow_error,
        divergent=divergent,
    )
    return primary_value, report

BINARY_OPS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "modulo": modulo,
}

# Shadow handlers per op. Ops without a System One candidate shadow themselves
# (parity baseline); "add" is shadowed by its System One candidate.
SYSTEM_ONE_OPS = {**BINARY_OPS, "add": system_one_add}

def route_operation(op, a, b, *, shadow_enabled=False):
    """Routes op to its primary handler, optionally shadowed by System One.

    Returns (value, ShadowReport); value is always the primary handler's result.
    """
    if op not in BINARY_OPS:
        valid = ", ".join(sorted(BINARY_OPS))
        raise ValueError(f"Unknown operation {op!r}; valid ops: {valid}")
    return shadow_route(BINARY_OPS[op], SYSTEM_ONE_OPS[op], a, b,
                        shadow_enabled=shadow_enabled)
