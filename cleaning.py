#----------
#cleaning.py
#==========

import os
import time

import Equipment


#this is a helper function to clear the output (makes things easier to read)
def clear_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return



#Reads an integer from the user. Returns None if the input is not a number.
def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None



#The entry point from the staff menu. Displays the cleaning staff's menu.
def when_called(id = -1):
    clear_output()

    response = -1
    while response != 0:
        print("Cleaning Dashboard\n")
        print("Choose an option:")
        print("0. Exit to Staff Dashboard")
        print("1. View Equipment Needing Cleaning")
        print("2. Mark Equipment Cleaned")
        print("3. Inspect Equipment")

        response = read_int("Enter a number: ")
        if response is None:
            response = -1
            continue

        if response == 0:
            print("\nExiting to Staff Dashboard")
            time.sleep(1)
            clear_output()
            break
        elif response == 1:
            clear_output()
            View_Cleaning_Queue()
        elif response == 2:
            clear_output()
            Mark_Cleaned()
        elif response == 3:
            clear_output()
            Inspect_Equipment()
        else:
            print("Invalid option. Please choose 0, 1, 2, 3\n")

    return



#Returns the equipment currently in the Cleaning state.
def get_cleaning_queue():
    return [
        item
        for item in Equipment.all_equipment
        if item.status == Equipment.EquipmentStatus.CLEANING
    ]



#True if the equipment has a pending reservation request.
def has_upcoming_reservation(item):
    return any(request.equipID == item.id for request in Equipment.all_requests)



#Prints the list of equipment waiting to be cleaned. Returns it.
def print_queue(queue):
    print(f"{'EQUIPMENT NEEDING CLEANING':^60}\n")
    print(f"{'#':<3} | {'ID':<3} | {'Name':<15} | Description")
    print('-' * 60)
    for number, item in enumerate(queue, start=1):
        print(f"{number:<3} | {item.id:<3} | {item.name:<15} | {item.description}")
    print()



#Lets the user pick one item from the cleaning queue. Returns it, or None.
def choose_from_queue(queue):
    print_queue(queue)
    print("0. Cancel")
    choice = read_int("\nWhich equipment? Select a number.")
    if choice is None or choice < 1 or choice > len(queue):
        return None
    return queue[choice - 1]



#Prints the equipment waiting to be cleaned.
def View_Cleaning_Queue():
    queue = get_cleaning_queue()

    if not queue:
        print("No equipment needs cleaning.")
    else:
        print_queue(queue)

    pause()
    return



#Marks a piece of equipment as cleaned.
#  [has upcoming reservation] -> Reserved
#  [no upcoming reservation]  -> In Storage, notify equipment manager
def Mark_Cleaned():
    queue = get_cleaning_queue()

    if not queue:
        print("No equipment needs cleaning.")
        pause()
        return

    item = choose_from_queue(queue)
    if item is None:
        print("No equipment cleaned.")
        pause()
        return

    item.assigned = 0  #it has been returned, so nobody is holding it anymore

    if has_upcoming_reservation(item):
        item.status = Equipment.EquipmentStatus.RESERVED
        print(f"\n{item.name} is cleaned and reserved for its upcoming event.")
    else:
        item.status = Equipment.EquipmentStatus.IN_STORAGE
        print(f"\n{item.name} is cleaned and back in storage.")
        print("Equipment Manager Notification Sent")

    pause()
    return



#Inspects a piece of equipment that is being cleaned.
#  [repair needed] -> In Repair
#  [not repairable] -> Broken
def Inspect_Equipment():
    queue = get_cleaning_queue()

    if not queue:
        print("No equipment needs cleaning.")
        pause()
        return

    item = choose_from_queue(queue)
    if item is None:
        print("No equipment inspected.")
        pause()
        return

    print(f"\nInspecting {item.name}")
    print("0. Cancel")
    print("1. Repair needed")
    print("2. Not repairable")
    result = read_int("Enter a number: ")

    if result == 1:
        item.status = Equipment.EquipmentStatus.IN_REPAIR
        print(f"\n{item.name} sent to repair.")
        print("Equipment Manager Notification Sent")
    elif result == 2:
        item.status = Equipment.EquipmentStatus.BROKEN
        print(f"\n{item.name} marked as broken.")
        print("Equipment Manager Notification Sent")
    else:
        print("No changes made.")

    pause()
    return


def pause():
    input("\nPress Enter to continue...")
    clear_output()
