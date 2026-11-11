import equipment_manager
import cleaning



def when_called(id = -1):
    response = -1
    while response != 0:
        #gives the user the menu for logging out or going to the equipment manager menu
        try:
            response = int(input("Choose an option:\n0. LogOut\n1. EquipmentManager\n2. Cleaning\nEnter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if response == 0:
            print("--------------")
            print("Logging Out...\n")
        elif response == 1:
            equipment_manager.when_called()
        elif response == 2:
            cleaning.when_called()
        else:
            print("Invalid option. Please choose 0, 1, or 2.")

    return