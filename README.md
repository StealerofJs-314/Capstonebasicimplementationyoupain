# Capstone

Run the application with `python main.py`. Test accounts are defined in
`user_state.py`; they all use the password `password`.

The project separates event, equipment, user, staff, and security records into
domain and state modules. Equipment reservations and staff assignments refer
to events by event ID. Queries, display formatting, and common input/menu
handling are shared services rather than duplicated in each dashboard.

All records are stored in memory and reset when the application exits.