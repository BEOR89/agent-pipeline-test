# Architecture

A minimal Python module with pytest tests and an isolated System One shadow-routing pilot.

Current public surface:
- arithmetic helpers: `add`, `subtract`, `multiply`, `divide`, `power`, and `modulo`
- `shadow_route(primary, shadow, a, b, shadow_enabled=False)`, which always returns the primary value
- `route_operation(op, a, b, shadow_enabled=False)`, which selects the primary and shadow handlers

The `add` operation is shadowed by `system_one_add`; operations without a candidate shadow themselves for parity. Shadow failures and comparison failures are recorded in `ShadowReport` and never replace the primary result.
