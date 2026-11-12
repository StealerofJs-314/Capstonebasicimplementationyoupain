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
#----------

#The entry point from the staff menu. Displays the Equipment Manager's menu.
def when_called(id = -1, staff_codes = None):
    clear_output()
    print("Equipment Manager Dashboard\n")
    actions = ['Exit to Staff Dashboard', 'Check Equipment Requests', 'Check Equipment', 'Buy Equipment', 'Sell Equipment']

    response = -1
    while response != 0:
        response = Menu(actions)
        if response == 0:
            pass
        elif response == 1:
            Check_Equipment_Requests()
        elif response == 2:
            Check_Equipment()
        elif response == 3:
            Buy_Equipment()
        elif response == 4:
            Sell_Equipment()
    return
#-----

#displays a menu of actions for the user and handles the user input
#Returns: the user's response
def Menu(actions):
    response = -1
    while response != 0:
        for option, (label) in enumerate(actions, start = 0):
            print(f"{option}. {label}")
        try:
            response = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
        if response < 0 and response > len(actions):
            print("Invalid option.")
        else:
            return response
    return -1
#-----

#Queries for equipment requests and gives options to accept or deny
def Check_Equipment_Requests():
    #clear_output()
    Equipment.Query_Equipment_Requests()
    actions = ['Back', 'Approve Request', 'Deny Request']
    response = Menu(actions)
    if response == 0:
        clear_output()
    elif response == 1:
        Equipment.EquipmentRequest.Aproove_EquipmentRequest()
    elif response == 2:
        Equipment.EquipmentRequest.Deny_EquipmentRequest()
    return
#-----

#Queries for all equipments and gives options to repair, clean, or dispose
def Check_Equipment():
    #clear_output()
    Equipment.Query_Equipment()
    actions = ['Back', 'Clean', 'Repair', 'Dispose']
    response = Menu(actions)
    if response == 0:
        clear_output()
    elif response == 1:
        Clean_Equipment()
    elif response == 2:
        Repair_Equipment()
    elif response == 3:
        Dispose_Equipment()
    return
#-----

#sends the equipment to the cleaners
def Clean_Equipment():
    #clear_output()
    count = 0
    for eq in Equipment.all_equipment:
        if eq.status == Equipment.EquipmentStatus.CLEANING:
            count += 1
    if count > 0:
        print("Sent notification to Cleaner.")
        print(f"{count} items need cleaned.\n")
        time.sleep(1)
    else:
        print("No equipment needs cleaned.")
    return
#-----

#repair equipment
def Repair_Equipment():
    actions = ['Back']
    for eq in Equipment.all_equipment:
        if eq.status == Equipment.EquipmentStatus.IN_REPAIR:
            actions.append(eq.name)
    if len(actions) == 0:
        print("No equipment needs repairing at this time.")
    else:
        response = Menu(actions)
        if response == 0:
            clear_output()
        #repair the chosen equipment
        elif response > 0 and response < len(actions) + 1:
            for eq in Equipment.all_equipment:
                if actions[response] == eq.name:
                    #mark it as IN_STORAGE and return it to storage
                    eq.status = Equipment.EquipmentStatus.IN_STORAGE
    return
#-----

#dispose of equipment
def Dispose_Equipment():
    actions = ['Back']
    for eq in Equipment.all_equipment:
        if eq.status == Equipment.EquipmentStatus.BROKEN:
            actions.append(eq.name)
    if len(actions) == 0:
        print("No broken equipment")
    else:
        response = Menu(actions)
        if response == 0:
            clear_output()
        #dispose of the chosen equipment
        elif response > 0 and response < len(actions) + 1:
            for eq in Equipment.all_equipment:
                if actions[response] == eq.name:
                    #dispose of the equipment
                    Equipment.Equipment.Remove_Equipment(eq.id)
    return
#-----

#buy equipment
def Buy_Equipment():
    print("Buying new equipment...")
    name = input("Enter new equipment name: ")
    desc = input("Enter new equipment description: ")
    Equipment.Equipment.Add_Equipment(name, desc)
    return
#-----

#sell equipment
def Sell_Equipment():
    actions = ['Back']
    for eq in Equipment.all_equipment:
        if eq.status != Equipment.EquipmentStatus.IN_USE and eq.status != Equipment.EquipmentStatus.RESERVED:
            actions.append(eq.name)
    if len(actions) == 0:
        print("There is no equipment.")
    else:
        response = Menu(actions)
        if response == 0:
            clear_output()
        #sell the chosen equipment
        if response > 0 and response < len(actions) + 1:
            for eq in Equipment.all_equipment:
                if actions[response] == eq.name:
                    Equipment.Equipment.Remove_Equipment(eq.id)
    return
#-----