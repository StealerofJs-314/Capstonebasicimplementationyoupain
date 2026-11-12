from event import EventStatus
from event_state import events
from equipment_models import EquipmentStatus
from equipment_state import equipment, equipment_requests, event_equipment
from security_state import security_personnel, security_requests
from staff_state import staff_assignments
from user_state import users


def get_user_by_username(username):
    return next((user for user in users if user.username == username), None)


def get_all_users():
    return list(users)


def get_all_events():
    return list(events)


def get_event_by_id(event_id):
    return next((event for event in events if event.id == event_id), None)


def get_events_by_status(status):
    return [event for event in events if event.status == status]


def get_requested_events():
    return get_events_by_status(EventStatus.REQUESTED)


def get_approved_events():
    return get_events_by_status(EventStatus.APPROVED)


def get_events_by_requester(requester_id):
    return [event for event in events if event.requester_id == requester_id]


def get_events_for_staff(staff_id):
    event_ids = {
        assignment.event_id
        for assignment in staff_assignments
        if assignment.staff_id == staff_id
    }
    return [event for event in events if event.id in event_ids]


def get_conflicting_event(new_event):
    for event in get_approved_events():
        if event.id == new_event.id:
            continue
        if (
            event.building.strip().lower() == new_event.building.strip().lower()
            and event.room == new_event.room
            and event.day == new_event.day
            and event.month == new_event.month
            and event.year == new_event.year
            and event.time == new_event.time
        ):
            return event
    return None


def get_equipment_by_id(equipment_id):
    return next((item for item in equipment if item.id == equipment_id), None)


def get_all_equipment():
    return list(equipment)


def get_equipment_by_status(status):
    return [item for item in equipment if item.status == status]


def get_event_equipment(event_id):
    return [
        get_equipment_by_id(link.equipment_id)
        for link in event_equipment
        if link.event_id == event_id
    ]


def get_equipment_requests():
    return list(equipment_requests)


def get_equipment_requests_for_item(equipment_id):
    return [
        request
        for request in equipment_requests
        if request.equipment_id == equipment_id
    ]


def get_equipment_with_event_links():
    return list(event_equipment)


def get_security_requests():
    return list(security_requests)


def get_security_personnel():
    return list(security_personnel)
