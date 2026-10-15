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
    any exception it raises is captured in the report.
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
            divergent = shadow_value != primary_value
    report = ShadowReport(
        primary_handler=getattr(primary, "__name__", repr(primary)),
        shadow_handler=getattr(shadow, "__name__", repr(shadow)),
        shadow_enabled=shadow_enabled,
        primary_value=primary_value,
        shadow_value=shadow_value,
        shadow_error=shadow_error,
        divergent=bool(divergent),
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

# Parity baseline: identical to BINARY_OPS at pilot start. Pilot work swaps
# entries here for System One candidates (e.g. "add": system_one_add).
SYSTEM_ONE_OPS = dict(BINARY_OPS)

def route_operation(op, a, b, *, shadow_enabled=False):
    """Routes op to its primary handler, optionally shadowed by System One.

    Returns (value, ShadowReport); value is always the primary handler's result.
    """
    if op not in BINARY_OPS:
        valid = ", ".join(sorted(BINARY_OPS))
        raise ValueError(f"Unknown operation {op!r}; valid ops: {valid}")
    return shadow_route(BINARY_OPS[op], SYSTEM_ONE_OPS[op], a, b,
                        shadow_enabled=shadow_enabled)
