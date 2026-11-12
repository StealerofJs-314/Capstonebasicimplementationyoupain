from query_service import (
    get_event_by_id,
    get_equipment_by_id,
    get_event_equipment,
)


def format_event(event):
    fields = (
        ("Event ID", event.id),
        ("Name", event.name),
        ("Time", event.time),
        ("Date", f"{event.year:04d}-{event.month:02d}-{event.day:02d}"),
        ("Building", event.building),
        ("Room", event.room),
        ("Requester", event.requester_name),
        ("Equipment IDs", ", ".join(
            str(item.id) for item in get_event_equipment(event.id) if item is not None
        )),
        ("Status", event.status.name),
    )
    return "\n".join(
        f"{label}: {value}" for label, value in fields if value != ""
    )


def display_event(event):
    print(format_event(event))


def display_events(events, empty_message):
    if not events:
        print(empty_message)
        return
    for event in events:
        display_event(event)
        print("--------------")


def display_equipment(item):
    print(
        f"ID: {item.id}\n"
        f"Name: {item.name}\n"
        f"Description: {item.description}\n"
        f"Status: {item.status.name}\n"
        f"Assigned user: {item.assigned_user_id}"
    )


def display_equipment_list(items):
    if not items:
        print("No equipment.")
        return
    print(f"{'ID':<5} {'Name':<20} {'Status':<15} Description")
    for item in items:
        print(f"{item.id:<5} {item.name:<20} {item.status.name:<15} {item.description}")


def display_equipment_requests(requests):
    if not requests:
        print("No pending equipment requests.")
        return
    for request in requests:
        event = get_event_by_id(request.event_id)
        item = get_equipment_by_id(request.equipment_id)
        event_label = f"{event.id}: {event.name}" if event else f"{request.event_id}: (missing event)"
        equipment_label = f"{item.id}: {item.name}" if item else f"{request.equipment_id}: (removed)"
        print(f"Event {event_label} | Equipment {equipment_label} | {request.reason}")


def display_security_requests(requests):
    if not requests:
        print("No security requests.")
        return
    for request in requests:
        event = get_event_by_id(request.event_id)
        event_label = event.name if event else "(missing event)"
        print(
            f"Event ID: {request.event_id} ({event_label})\n"
            f"Personnel needed: {request.personnel_count}\n"
            f"Start time: {request.start_time:04d}hrs\n"
            f"Duration: {request.duration} hours"
        )


def display_security_personnel(personnel):
    if not personnel:
        print("No security personnel.")
        return
    for person in personnel:
        print(
            f"Employee ID: {person.id}\n"
            f"Employee Name: {person.name}\n"
            f"Employee Rank: {person.rank}\n"
            f"Employee Schedule: {person.available_days}"
        )
