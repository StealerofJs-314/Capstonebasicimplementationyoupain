from display_service import display_equipment_list
from equipment_models import EquipmentStatus
from input_utils import pause, read_int
from menu_utils import choose_option
from query_service import (
    get_equipment_by_status,
    get_equipment_requests_for_item,
)
from equipment_service import set_equipment_status


def run_dashboard(staff_id):
    options = {
        0: "Exit to Staff Dashboard",
        1: "View Equipment Needing Cleaning",
        2: "Mark Equipment Cleaned",
        3: "Inspect Equipment",
    }
    while True:
        choice = choose_option("Cleaning Dashboard", options)
        if choice == 0:
            return
        if choice == 1:
            view_cleaning_queue()
        elif choice == 2:
            mark_equipment_cleaned()
        else:
            inspect_equipment()


def choose_equipment(queue):
    if not queue:
        print("No equipment is available for this action.")
        return None
    display_equipment_list(queue)
    item_id = read_int("Equipment ID (0 to cancel): ")
    if item_id == 0:
        return None
    item = next((candidate for candidate in queue if candidate.id == item_id), None)
    if item is None:
        print("No equipment found with that ID.")
    return item


def view_cleaning_queue():
    display_equipment_list(get_equipment_by_status(EquipmentStatus.CLEANING))
    pause()


def mark_equipment_cleaned():
    item = choose_equipment(get_equipment_by_status(EquipmentStatus.CLEANING))
    if item is None:
        return
    next_status = (
        EquipmentStatus.RESERVED
        if get_equipment_requests_for_item(item.id)
        else EquipmentStatus.IN_STORAGE
    )
    set_equipment_status(item, next_status)
    print(f"{item.name} cleaned and marked {next_status.name.lower()}.")
    pause()


def inspect_equipment():
    item = choose_equipment(get_equipment_by_status(EquipmentStatus.CLEANING))
    if item is None:
        return
    result = choose_option(
        f"Inspecting {item.name}",
        {0: "Cancel", 1: "Repair needed", 2: "Not repairable"},
    )
    if result == 1:
        set_equipment_status(item, EquipmentStatus.IN_REPAIR)
        print(f"{item.name} sent to repair.")
    elif result == 2:
        set_equipment_status(item, EquipmentStatus.BROKEN)
        print(f"{item.name} marked as broken.")
    pause()
