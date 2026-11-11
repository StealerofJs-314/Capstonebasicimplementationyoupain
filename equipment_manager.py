#----------
#Equipment_Manager.py
#==========
# * Defines the functions for the role of the equipment manager

from enum import Enum
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
#-----------------


#The entry point from the staff menu. Displays the Equipment Manager's menu.
def when_called(id = -1):
    clear_output()
    
    response = -1
    while response != 0:
        try:
            print("Equipment Manager Dashboard\n")
            print("Choose an option:")
            print("0. Exit to Staff Dashboard")
            print("1. Check Equipment Reservations")
            print("2. Inspect Equipment")
            print("3. Buy Equipment")
            print("4. Sell Equipment")
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")

        if response == 0:
            print("Exiting to Staff Dashboard")
            time.sleep(1)
            clear_output()

            break
        elif response == 1:
            clear_output()
            Check_Reservations()
        elif response == 2:
            clear_output()
            Inspect_Equipment()
        elif response == 3:
            print("Buying Equipment")
        elif response == 4:
            print("Selling Equipment")
        else:
            print("Invalid option. Please choose 0, 1, 2, 3, 4\n")

    return
#---------


#Queries any equipment requests and gives options to accept or deny
def Check_Reservations():
    Equipment.Query_Equipment_Requests()

    response = -1
    while response != 0:
        try:
            print("Choose an option:")
            print("0. Back")
            print("1. Approve")
            print("2. Deny")
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
        if response == 0:
            clear_output()
            break
        #approve
        elif response == 1:
            clear_output()
            Equipment.Query_Equipment_Requests()
            if len(Equipment.all_requests) > 0:
                index = -1
                while index != 0:
                    try:
                        print("Choose a request to aproove:")
                        print("0. Back")
                        for i in range(0, len(Equipment.all_requests)):
                            print(i + 1, ". ", Equipment.all_equipment[Equipment.all_requests[i].equipID].name, "for: ", Equipment.all_requests[i].reason)
                        index = int(input("Enter a number: "))
                    except ValueError:
                        print("\nPlease enter a valid number.")
                    if index == 0:
                        break
                    elif index > 0 and index < len(Equipment.all_requests) + 1:
                        Equipment.EquipmentRequest.Aproove_EquipmentRequest(index - 1)
                        break
                    else:
                        print("Invalid option.")#better prompt?
                #-----
            elif len(Equipment.all_requests) == 0:
                print("No pending requests...")
        #deny
        elif response == 2:
            clear_output()
            Equipment.Query_Equipment_Requests()
            if len(Equipment.all_requests) > 0:
                index = -1
                while index != 0:
                    try:
                        print("Choose a request to deny")
                        print("0. Back")
                        for i in range(0, len(Equipment.all_requests)):
                            print(i + 1, ". ", Equipment.all_equipment[Equipment.all_requests[i].equipID].name, "for: ", Equipment.all_requests[i].reason)
                        index = int(input("Enter a number: "))
                    except ValueError:
                        print("\nPlease enter a valid number.")
                    if index == 0:
                        break
                    elif index > 0 and index < len(Equipment.all_requests) + 1:
                        Equipment.EquipmentRequest.Deny_EquipmentRequest(index - 1)
                        break
                    else:
                        print("Invalid option.")
                #-----
            elif len(Equipment.all_requests) == 0:
                print("No pending requests...")
        else:
            print("Invalid option. Please choose 0, 1, 2")
    return
#-----------


#Query all equipment and give options to repair, clean, or dispose as well as update the equipment information
def Inspect_Equipment():
    response = -1
    while response != 0:
        try:
            Equipment.Query_Equipment()
            print("Choose an option:")
            print("0. Back")
            print("1. Clean")
            print("2. Repair")
            print("3. Dispose")
            print("4. Update Entry")
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
        if response == 0:
            clear_output()
            break
        #clean
        elif response == 1:
            Clean_Equipment()
        elif response == 2:
            Repair_Equipment()
        elif response == 3:
            Dispose_Equipment()
        elif response == 4:
            #update entry
            pass
    #options:
    # broken
    #   -> dispose()
    #       -> 
    # update
    #   -> update the information in the system

    return
#----------

def Clean_Equipment():
    clear_output()
    cleaning = []
    for eq in Equipment.all_equipment:
        if eq.status == Equipment.EquipmentStatus.CLEANING:
            cleaning.append(eq)
    if len(cleaning) == 0:
        print("No equipment needs cleaning at this time.")
    else:
        index = -1
        while index != 0:
            try:
                print("Choose an equipment to clean:")
                print("0. Back")
                if len(cleaning) > 0:
                    for i in range(0, len(cleaning)):
                        print(i + 1,".",cleaning[i].name)
                    index = int(input("Enter a number: "))
                else:
                    clear_output()
                    print("All equipment has been cleaned.")
                    break
            except ValueError:
                print("Please enter a valid number.")
            if index == 0:
                clear_output()
                break
            elif index > 0 and index < len(cleaning) + 1:
                for eq in Equipment.all_equipment:
                    if cleaning[index - 1].id == eq.id:
                        eq.status = Equipment.EquipmentStatus.IN_STORAGE
                        cleaning.remove(eq)
                        break
            else:
                print("Invalid Option.")
    return
#----------

def Repair_Equipment():
    clear_output()
    repairing = []
    for eq in Equipment.all_equipment:
        if eq.status == Equipment.EquipmentStatus.IN_REPAIR:
            repairing.append(eq)
    if len(repairing) == 0:
        print("No equipment needs repairing at this time.")
    else:
        index = -1
        while index != 0:
            try:
                print("Choose an equipment to repair")
                print("0. Back")
                if len(repairing) > 0:
                    for i in range(0, len(repairing)):
                        print(i + 1,".",repairing[i].name)
                    index = int(input("Enter a number: "))
                else:
                    clear_output()
                    print("All equipment has been repaired.")
                    break
            except ValueError:
                print("Please enter a valid number.")
            if index == 0:
                clear_output()
                break
            elif index > 0 and index < len(repairing) + 1:
                for eq in Equipment.all_equipment:
                    if repairing[index - 1].id == eq.id:
                        eq.status = Equipment.EquipmentStatus.IN_STORAGE
                        repairing.remove(eq)
                        break
            else:
                print("Invalid Option.")
    return
#----------

def Dispose_Equipment():
    clear_output()
    broken = []
    for eq in Equipment.all_equipment:
        if eq.status == Equipment.EquipmentStatus.BROKEN:
            broken.append(eq)
    if len(broken == 0):
        print("No broken equipment.")
    else:
        index = -1
        while index != 0:
            try:
                print("Choose an equipment to dispose of:")
                print("0. Back")
                if len(broken) > 0:
                    for i in range(0, len(broken)):
                        print(i + 1,".",broken[i].name)
                    index = int(input("Enter a number: "))
                else:
                    clear_output()
                    print("All broken equipment disposed of.")
                    break
            except ValueError:
                print("Please enter a valid number")
            if input == 0:
                clear_output()
                break
            elif index > 0 and index < len(broken) + 1:
                for eq in Equipment.all_equipment:
                    if eq.status == Equipment.EquipmentStatus.BROKEN:
                        Equipment.all_equipment.remove(eq)
                        broken.remove(eq)
                        break
            else:
                print("Invalid Option.")
    return
#----------


def Buy_Equipment():
    #go through the process of adding equipment to the system.



    #self.id = ID              #ID of the equipment
    #self.name = Name          #Name of the equipment
    #        self.description = Desc   #Description of the equipment
    #        self.status = EquipmentStatus.IN_STORAGE

    return