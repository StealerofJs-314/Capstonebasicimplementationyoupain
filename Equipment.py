#----------
#Equipment.py
#==========
#  * Defines equipment in the sytem and the functions to request it
#----------

from enum import Enum
import Schedule_event   #used for making requests

#Status of Equipment
class EquipmentStatus(Enum):
    """
        Status of Equipment:\n
        IN_STORAGE(0): The equipment is in storage.\n
        RESERVED(1): The equipment has a reservation placed.\n
        IN_USE(2): The equipment is in use.\n
        CLEANING(3): The equipment is being cleaned.\n
        BROKEN(4): The equipment needs repaired\n
        IN_REPAIR(5): The equipment is being repaired
    """
    IN_STORAGE = 0
    RESERVED = 1
    IN_USE = 2
    CLEANING = 3
    BROKEN = 4
    IN_REPAIR = 5
    #No status for sold as its no longer tracked by the system
#----------


#Class representing a piece of equipment.
class Equipment:
    """Class representing a piece of equipment."""
    def __init__(self, ID = -1, Name = "", Desc = ''):
        self.id = ID              #ID of the equipment
        self.name = Name          #Name of the equipment
        self.description = Desc   #Description of the equipment
        self.status = EquipmentStatus.IN_STORAGE
        self.assigned = 0      #userID that currently has the equipment
#----------


#outputs a table of equipment in the system
def Query_Equipment():
    print(f"{'EQUIPMENT':^139}")
    print(f"{'ID':<3} | {'Name':^15} | {'Description':^70} | {'Status':^30} | {'Assigned':<6}")
    print('-' * 139)
    for eq in all_equipment:
        print(f"{eq.id:<3} | {eq.name:<15} | {eq.description:<70} | {eq.status:<30} | {eq.assigned:<6}")
        print('-' * 139)
    print()
#----------


#The list of equipment currently in the system.
all_equipment = [
    Equipment(#associated with the club meeting event
        1, "Lavalier Mic", "Microphone that clips to your shirt or jacket"
    ),
    Equipment(#associated with the art workshop event
        2, "Kiln", "Used for firing clay into pottery"
    ),
    Equipment(#associated with the science fair event
        3, "Microscope", "Used for viewing microscopic objects"
    ),
    Equipment(#associated with the basketball practice event
        4, "Basketball", "Used for playing basketball"
    )
]
"""The list of equipment currently in the system."""

#return the lavalier mic, it needs to be cleaned
all_equipment[0].status = EquipmentStatus.CLEANING
#break the microscope for demonstration purposes
all_equipment[2].status = EquipmentStatus.BROKEN

#Class representing an equipment request
# Vars:
#  * userID:  ID of the requesting user.
#  * equipID: ID of the requested equipment.
class EquipmentRequest:
    """Class representing an equipment request\n Vars:\n\t* userID: ID of the requesting user.\n\t* equipID: ID of the requested equipment."""
    def __init__(self, userID, equipID):
        self.userID = userID
        self.equipID = equipID
    #----------

    def RequestEquipment(userID, equipID):
        if all_equipment[equipID].status != 0 or all_equipment[equipID].status != 1:
            print("We're sorry. That is not available at this time.")
        else:
            all_requests.append(EquipmentRequest(userID, equipID))

        return
    #----------

    def Aproove(requestID):
        """Aproove a user's request for equipment for their event"""

        print("index is: ", requestID)
        all_equipment[all_requests[requestID].equipID].status = EquipmentStatus.IN_USE
        all_equipment[all_requests[requestID].equipID].assigned = all_requests[requestID].userID
        
        #update the equipment status to be IN_USE and assigned to the user
        
        #remove that request
        #all_requests.remove(requestID)
        print("Request Aprooved Notification Sent\n")
        return
    #----------

    def Deny(requestID):
        """Deny the user's request for equipment for their event"""
        all_requests.remove(requestID)
        print("Request Denied Notification Sent")
        return
    #----------

#----------


#The list of all pending equipment requests.
all_requests = [
    EquipmentRequest(
        Schedule_event.all_events[1].requesterID, 0
    )
]
"""The list of all pending equipment requests."""

