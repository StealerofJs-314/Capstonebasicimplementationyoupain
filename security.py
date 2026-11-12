from display_service import display_security_personnel, display_security_requests
from input_utils import read_positive_int
from menu_utils import choose_option
from query_service import get_event_by_id, get_security_personnel
from security_models import SecurityRequest
from security_state import security_requests


def run_dashboard(staff_id):
    options = {
        0: "Log Out",
        1: "List Security Requests",
        2: "Personnel Roster",
        3: "Create Security Request",
    }
    while True:
        choice = choose_option("Security Dashboard", options)
        if choice == 0:
            return
        if choice == 1:
            display_security_requests(security_requests)
        elif choice == 2:
            display_security_personnel(get_security_personnel())
        else:
            create_security_request()


def create_security_request():
    event_id = read_positive_int("Event ID: ")
    if get_event_by_id(event_id) is None:
        print(f"No event exists with ID {event_id}.")
        return
    personnel_count = read_positive_int("Number of officers: ")
    start_time = read_positive_int("Start time (24-hour clock, e.g. 800): ")
    duration = read_positive_int("Event duration in hours: ")
    security_requests.append(
        SecurityRequest(event_id, personnel_count, start_time, duration)
    )
    print(f"Security request for event {event_id} created.")
