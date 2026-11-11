import equipment_manager




def when_called():
    response = -1
    while response != 0:
        #gives the user the menu for logging out or going to the equipment manager menu
        try:
            response = int(input("Choose an option:\n0. LogOut\n1. EquipmentManager\nEnter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if response == 0:
            print("--------------")
            print("Logging Out...\n")
        elif response == 1:
            equipment_manager.when_called()
        else:
            print("Invalid option. Please choose 0 or 1.")

    return