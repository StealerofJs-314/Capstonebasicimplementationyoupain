#----------
#Equipment_Manager.py
#==========
# * Defines the functions for the role of the equipment manager

from enum import Enum
import os
import time

import Schedule_event
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
def when_called():
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
            print("\nExiting to Staff Dashboard")
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

    return


#Query all equipment
def Inspect_Equipment():
    Equipment.Query_Equipment()

    #options:
    # repair
    #   -> sell() [not worth repairing] -> sold
    #   -> inspect() [beyond repair] -> broken
    # clean
    #   -> inspect() [repair needed] -> 
    #   -> inspect() [not repairble] -> broken
    # broken
    #   -> dispose()
    #       -> 

    return 