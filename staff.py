import equipment_manager
import cleaning


def when_called(id=-1, staff_codes=None):
    staff_codes = staff_codes or []
    available_actions = []
    if any(30 <= code < 40 for code in staff_codes):
        available_actions.append(("Equipment Manager", equipment_manager.when_called))
    if any(20 <= code < 30 for code in staff_codes):
        available_actions.append(("Cleaning", cleaning.when_called))

    while True:
        print("\nStaff Dashboard")
        print("0. Log Out")
        for option, (label, _) in enumerate(available_actions, start=1):
            print(f"{option}. {label}")

        try:
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if response == 0:
            print("--------------")
            print("Logging Out...\n")
            return
        elif 1 <= response <= len(available_actions):
            available_actions[response - 1][1]()
        else:
            print("Invalid option. Please choose one of the displayed options.")