# v0.1.0

- Initial version

# v0.1.1

- Minor patch for `setup.py`

# v0.2.0

- Include `/recorders` in the package
- Introduce new table `packets` for raw `op | payload` data
- `snooper` -> `snoopy` (and aliased)
- Debugging
- `Configuration.events` -> `event_flags`
- New `OpFlags` for filtering `packets` table.
- New event dispatched `socket_send`
- New `OpDetails` for generic data for packets sent and received.
