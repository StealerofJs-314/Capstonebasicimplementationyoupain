from display_service import display_equipment_list, display_equipment_requests
from equipment_models import EquipmentStatus
from equipment_service import (
    approve_equipment_request,
    create_equipment,
    delete_equipment,
    deny_equipment_request,
    set_equipment_status,
    update_equipment,
)
from input_utils import pause, read_int, read_text
from menu_utils import choose_option
from query_service import (
    get_all_equipment,
    get_equipment_by_id,
    get_equipment_requests,
)


def run_dashboard(staff_id):
    options = {
        0: "Exit to Staff Dashboard",
        1: "Check Equipment Reservations",
        2: "Inspect Equipment",
        3: "Buy Equipment",
        4: "Sell Equipment",
    }
    while True:
        choice = choose_option("Equipment Manager Dashboard", options)
        if choice == 0:
            return
        if choice == 1:
            manage_reservations()
        elif choice == 2:
            inspect_equipment()
        elif choice == 3:
            buy_equipment()
        else:
            sell_equipment()


def manage_reservations():
    requests = get_equipment_requests()
    display_equipment_requests(requests)
    if not requests:
        return
    index = read_int("Request number (0 to cancel): ")
    if index == 0:
        return
    if not 1 <= index <= len(requests):
        print("No request found with that number.")
        return

    choice = choose_option(
        "Equipment Request",
        {0: "Cancel", 1: "Approve", 2: "Deny"},
    )
    request = requests[index - 1]
    if choice == 1:
        if approve_equipment_request(request):
            print("Equipment request approved.")
        else:
            print("The request refers to equipment or an event that no longer exists.")
    elif choice == 2:
        deny_equipment_request(request)
        print("Equipment request denied.")


def inspect_equipment():
    display_equipment_list(get_all_equipment())
    item_id = read_int("Equipment ID (0 to cancel): ")
    if item_id == 0:
        return
    item = get_equipment_by_id(item_id)
    if item is None:
        print("No equipment found with that ID.")
        return

    choice = choose_option(
        f"Manage {item.name}",
        {
            0: "Back",
            1: "Mark for cleaning",
            2: "Mark in repair",
            3: "Mark as broken",
            4: "Return to storage",
            5: "Update details",
        },
    )
    statuses = {
        1: EquipmentStatus.CLEANING,
        2: EquipmentStatus.IN_REPAIR,
        3: EquipmentStatus.BROKEN,
        4: EquipmentStatus.IN_STORAGE,
    }
    if choice in statuses:
        set_equipment_status(item, statuses[choice])
    elif choice == 5:
        name = read_text("New name (blank to keep current): ", allow_empty=True)
        description = read_text(
            "New description (blank to keep current): ", allow_empty=True
        )
        update_equipment(item, name, description)
        print(f"Equipment {item.id} updated.")
    pause()


def buy_equipment():
    name = read_text("New equipment name: ")
    description = read_text("Description: ")
    item = create_equipment(name, description)
    print(f"Added {item.name} with equipment ID {item.id}.")


def sell_equipment():
    display_equipment_list(get_all_equipment())
    item_id = read_int("Equipment ID to sell (0 to cancel): ")
    if item_id == 0:
        return
    if delete_equipment(item_id):
        print(f"Equipment {item_id} and its pending requests were removed.")
    else:
        print("No equipment found with that ID.")
