from datetime import datetime

from display_service import display_events
from event import Event
from event_state import events
from input_utils import read_future_datetime, read_positive_int, read_text
from menu_utils import choose_option
from query_service import (
    get_approved_events,
    get_conflicting_event,
    get_events_by_requester,
)


def run_dashboard(user_id, requester_name):
    options = {
        0: "Log Out",
        1: "Submit an event request",
        2: "View upcoming approved events",
        3: "View my event requests",
    }
    while True:
        choice = choose_option("Regular User Dashboard", options)
        if choice == 0:
            print("Logging Out...\n")
            return
        if choice == 1:
            submit_event_request(user_id, requester_name)
        elif choice == 2:
            show_upcoming_events()
        else:
            display_events(
                get_events_by_requester(user_id),
                "No event requests found for your account.",
            )


def submit_event_request(requester_id, requester_name):
    name = read_text("Event name: ")
    building = read_text("Building: ")
    room = read_positive_int("Room number: ")
    event_datetime = read_future_datetime()

    event = Event(
        time=event_datetime.strftime("%H:%M"),
        day=event_datetime.day,
        month=event_datetime.month,
        year=event_datetime.year,
        building=building,
        room=room,
        name=name,
        requester_id=requester_id,
        requester_name=requester_name,
    )
    conflict = get_conflicting_event(event)
    if conflict is not None:
        print(f"That room is already booked by event {conflict.id}. Request not submitted.")
        return

    valid, reasons = event.submit()
    if not valid:
        print("Unable to submit the request:")
        for reason in reasons:
            print(reason)
        return

    events.append(event)
    print(f"Event request {event.id} submitted and is waiting for admin approval.")


def show_upcoming_events():
    upcoming = []
    for event in get_approved_events():
        try:
            event_datetime = datetime.strptime(
                f"{event.year:04d}-{event.month:02d}-{event.day:02d} {event.time}",
                "%Y-%m-%d %H:%M",
            )
        except ValueError:
            print(f"Event {event.id} has an invalid date or time and cannot be displayed.")
            continue
        if event_datetime > datetime.now():
            upcoming.append(event)
    display_events(upcoming, "No upcoming approved events.")
