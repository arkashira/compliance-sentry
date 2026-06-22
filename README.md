# compliance-sentry

A minimal, pure‑Python implementation of a real‑time audit‑ready logging system.
It records immutable access events for consent records and exposes a simple
query API.

## Features

- Immutable log entries per consent record
- Each log contains timestamp, actor, action, and data scope
- In‑memory query interface (no external DB)

## Usage
