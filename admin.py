
import Schedule_event


def choose_requested_event(action):
    """Lists the requested events and asks the admin to pick one to approve
    or deny. Returns the chosen event, or None if there is nothing to pick
    or the admin cancels."""
    requested_events = Schedule_event.get_requested_events(
        Schedule_event.all_events
    )
    if not requested_events:
        print(f"There are no requested events to {action}.")
        return None

    print("\nRequested Events")
    for event in requested_events:
        print(event)
        print("--------------")

    try:
        event_id = int(input(f"Enter the event ID to {action} (0 to cancel): "))
    except ValueError:
        print("Please enter a valid event ID.")
        return None
    if event_id == 0:
        return None

    chosen_event = next(
        (event for event in requested_events if event.event_id == event_id),
        None,
    )
    if chosen_event is None:
        print("No requested event found with that ID.")
    return chosen_event


def when_called(id = -1):
    while True:
        print("\nAdmin Dashboard")
        print("0. Log Out")
        print("1. Approve a requested event")
        print("2. View all approved events")
        print("3. Deny a requested event")
        try:
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if response == 0:
            print("Logging Out...\n")
            return
        elif response == 1:
            event_to_approve = choose_requested_event("approve")
            if event_to_approve is None:
                continue

            conflict = Schedule_event.get_conflicting_event(
                Schedule_event.all_events, event_to_approve
            )
            if conflict is not None:
                print(
                    f"Cannot approve: that room is already booked at that time "
                    f"by event {conflict.event_id} ({conflict.name})."
                )
                continue

            event_to_approve.approve(id)
            print(f"Event {event_to_approve.event_id} approved.")
        elif response == 2:
            approved_events = [
                event
                for event in Schedule_event.all_events
                if event.approved == Schedule_event.Approval_Status.APPROVED
            ]
            if not approved_events:
                print("There are no approved events.")
                continue

            print("\nApproved Events")
            for event in approved_events:
                print(event)
                print("--------------")
        elif response == 3:
            event_to_deny = choose_requested_event("deny")
            if event_to_deny is None:
                continue

            event_to_deny.denied(id)
            print(f"Event {event_to_deny.event_id} denied.")
        else:
            print("Invalid option. Please choose 0, 1, 2, or 3.")
