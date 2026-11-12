from display_service import display_events
from event import EventStatus
from menu_utils import choose_option
from query_service import (
    get_approved_events,
    get_conflicting_event,
    get_event_by_id,
    get_requested_events,
)
from input_utils import read_int


def choose_requested_event(action):
    requested = get_requested_events()
    display_events(requested, f"There are no requested events to {action}.")
    if not requested:
        return None

    event_id = read_int(f"Event ID to {action} (0 to cancel): ")
    if event_id == 0:
        return None
    event = get_event_by_id(event_id)
    if event is None or event.status != EventStatus.REQUESTED:
        print("No requested event found with that ID.")
        return None
    return event


def run_dashboard(admin_id):
    options = {
        0: "Log Out",
        1: "Approve a requested event",
        2: "View all approved events",
        3: "Deny a requested event",
    }
    while True:
        choice = choose_option("Admin Dashboard", options)
        if choice == 0:
            print("Logging Out...\n")
            return
        if choice == 1:
            event = choose_requested_event("approve")
            if event is None:
                continue
            conflict = get_conflicting_event(event)
            if conflict is not None:
                print(
                    f"Cannot approve: room conflicts with event {conflict.id} "
                    f"({conflict.name})."
                )
                continue
            event.approve(admin_id)
            print(f"Event {event.id} approved.")
        elif choice == 2:
            display_events(get_approved_events(), "There are no approved events.")
        else:
            event = choose_requested_event("deny")
            if event is not None:
                event.deny(admin_id)
                print(f"Event {event.id} denied.")
