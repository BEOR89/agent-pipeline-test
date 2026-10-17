# Agent Pipeline Test

Small repository used to validate the Hermes multi-agent development pipeline.

## Current pilot

The repository includes a System One shadow-routing pilot. Shadow execution is
explicitly opt-in, the primary result remains authoritative, and divergences or
shadow/comparison errors are reported without changing the caller-visible value.

`add` currently uses `system_one_add` as its candidate shadow; operations without
a candidate use themselves as the parity shadow.
