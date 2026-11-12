import cleaning
import equipment_manager
import security
from menu_utils import choose_option


def run_dashboard(user_id, staff_codes):
    actions = {}
    options = {0: "Log Out"}
    for code in staff_codes:
        if 30 <= code < 40 and 1 not in actions:
            options[1] = "Equipment Manager"
            actions[1] = (equipment_manager.run_dashboard, code)
        elif 20 <= code < 30 and 2 not in actions:
            options[2] = "Cleaning"
            actions[2] = (cleaning.run_dashboard, code)
        elif 10 <= code < 20 and 3 not in actions:
            options[3] = "Security"
            actions[3] = (security.run_dashboard, code)

    while True:
        choice = choose_option("Staff Dashboard", options)
        if choice == 0:
            print("Logging Out...\n")
            return
        action, staff_id = actions[choice]
        action(staff_id)
