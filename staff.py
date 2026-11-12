import equipment_manager
import cleaning
import security

def when_called(id=-1, staff_codes=None):
    staff_codes = staff_codes or []
    available_actions = []
    equipment_manager_id = next(
        (code for code in staff_codes if 30 <= code < 40), None
    )
    if equipment_manager_id is not None:
        available_actions.append(
            ("Equipment Manager", equipment_manager.when_called, equipment_manager_id)
        )

    cleaning_id = next((code for code in staff_codes if 20 <= code < 30), None)
    if cleaning_id is not None:
        available_actions.append(("Cleaning", cleaning.when_called, cleaning_id))

    security_id = next((code for code in staff_codes if 10 <= code < 20), None)
    if security_id is not None:
        available_actions.append(("Security", security.when_called, security_id))

    while True:
        print("\nStaff Dashboard")
        print("0. Log Out")
        for option, (label, _, _) in enumerate(available_actions, start=1):
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
            _, action, staff_id = available_actions[response - 1]
            action(staff_id)
        else:
            print("Invalid option. Please choose one of the displayed options.")