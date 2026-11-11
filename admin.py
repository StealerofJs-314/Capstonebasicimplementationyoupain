
import Schedule_event


def when_called(id = -1):
    while True:
        print("\nAdmin Dashboard")
        print("0. Log Out")
        print("1. Approve a requested event")
        print("2. View all approved events")
        try:
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if response == 0:
            print("Logging Out...\n")
            return
        elif response == 1:
            requested_events = Schedule_event.get_requested_events(
                Schedule_event.all_events
            )
            if not requested_events:
                print("There are no requested events to approve.")
                continue

            print("\nRequested Events")
            for event in requested_events:
                print(event)
                print("--------------")

            try:
                event_id = int(input("Enter the event ID to approve: "))
            except ValueError:
                print("Please enter a valid event ID.")
                continue

            event_to_approve = next(
                (event for event in requested_events if event.event_id == event_id),
                None,
            )
            if event_to_approve is None:
                print("No requested event found with that ID.")
                continue

            event_to_approve.approve(id)
            print(f"Event {event_id} approved.")
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
        else:
            print("Invalid option. Please choose 0, 1, or 2.")