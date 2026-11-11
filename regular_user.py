from datetime import datetime

import Schedule_event


def when_called(id=-1, requester_name=""):
    while True:
        print("\nRegular User Dashboard")
        print("0. Log Out")
        print("1. Search Rooms and Submit a Request")
        print("2. View Upcoming Events")
        print("3. View Room Requests")
        try:
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if response == 0:
            print("Logging Out...\n")
            return
        elif response == 1:
            search_room(id, requester_name)
        elif response == 2:
            view_upcoming_events()
        elif response == 3:
            view_requests()
        else:
            print("Invalid option. Please choose 0, 1, 2, or 3.")


def search_room(requester_id, requester_name):
    #Schedule_event.search_rooms()
    while True:
        response = input("Would you like to submit a room request? (y/n): ").strip().lower()
        if response == "y":
            submit_request(requester_id, requester_name)
            return
        elif response == "n":
            return
        else:
            print("Please enter y or n.")


def read_text(prompt):
    while True:
        response = input(prompt).strip()
        if response:
            return response
        print("Please enter a value.")


def read_number(prompt):
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if response > 0:
            return response
        print("Please enter a positive number.")


def submit_request(requester_id, requester_name):
    name = read_text("Event name: ")
    building = read_text("Building: ")
    room = read_number("Room number: ")

    while True:
        event_date = read_text("Event date (YYYY-MM-DD, e.g. 2026-12-26): ")
        try:
            parsed_date = datetime.strptime(event_date, "%Y-%m-%d").date()
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format (year-month-day).")
            continue

        event_time = read_text("Event time (HH:MM, 24-hour): ")
        try:
            parsed_time = datetime.strptime(event_time, "%H:%M").time()
        except ValueError:
            print("Please enter a valid time in 24-hour HH:MM format, such as 14:30.")
            continue

        event_datetime = datetime.combine(parsed_date, parsed_time)
        if event_datetime <= datetime.now():
            print("Please enter a future date and time.")
            continue
        break

    event = Schedule_event.Schedule_event(
        time=event_datetime.strftime("%H:%M"),
        day_date=event_datetime.day,
        day_month=event_datetime.month,
        day_year=event_datetime.year,
        building=building,
        room=room,
        name=name,
        requester=requester_name,
        requesterID=requester_id,
    )
    is_valid, reasons = event.submit()
    if not is_valid:
        print("Unable to submit the request:")
        for reason in reasons:
            print(reason)
        return

    Schedule_event.all_events.append(event)
    #print("Room request submitted. Waiting for approval...")
    #event.approve(-1)
    #print("Simulated notification: Your event request has been approved.")
    return


def view_upcoming_events():
    print("\nUpcoming Events")
    found = False
    for event in Schedule_event.all_events:
        if event.approved != Schedule_event.Approval_Status.APPROVED:
            continue
        try:
            event_time = datetime.strptime(event.time, "%H:%M").time()
            event_datetime = datetime(
                event.day_year, event.day_month, event.day_date,
                event_time.hour, event_time.minute,
            )
        except (TypeError, ValueError):
            print("An approved event has an invalid date or time and cannot be displayed.")
            continue
        if event_datetime > datetime.now():
            print(event)
            print("--------------")
            found = True
    if not found:
        print("No upcoming events.")
    return


def view_requests():
    requester_id = read_number("Requester ID: ")
    print("\nRoom Requests")
    found = False
    for event in Schedule_event.all_events:
        if event.requesterID == requester_id and event.approved != Schedule_event.Approval_Status.IN_PROGRESS:
            print(event)
            print("--------------")
            found = True
    if not found:
        print("No room requests found.")
    return
