#------------
#Equipment.py
#============
#  * Defines equipment in the sytem and the functions to request it
#----------

from enum import Enum
import Schedule_event

#==============================
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
#----------

#class representing a piece of equipment.
class Equipment:
    """Class representing a piece of equipment"""
    def __init__(self, ID = -1, Name = "", Desc = ""):
        self.id = ID            #ID of the equipment
        self.name = Name        #Name of the equipment
        self.description = Desc #Description of the equipment
        self.status = EquipmentStatus.IN_STORAGE
    #-----

    def Add_Equipment(Name = "", Desc = ""):
        id = all_equipment[len(all_equipment) - 1].id + 1
        all_equipment.append(Equipment(id, Name, Desc))
        return
    #-----

    #Removes the designated equipment from the system (providing it broken)
    def Remove_Equipment(equipID):
        print(equipID)
        print(all_equipment[equipID - 1].name)
        all_equipment.remove(all_equipment[equipID - 1])
        return
    #-----
#----------

#outputs the table of equipment currently in the system
def Query_Equipment():
    lenOfOutput = 3 + 15 + 70 + 30 + (3 * 3) #each header + column spacing = 133
    print(f"{'EQUIPMENT':^133}")
    print(f"{'ID':<3} | {'Name':^15} | {'Description':^70} | {'Status':^30}")
    print('-' * lenOfOutput)
    if len(all_equipment) == 0:
        print(f"{'No equipment...':^133}")
    else:
        for eq in all_equipment:
            print(f"{eq.id:<3} | {eq.name:<15} | {eq.description:<70} | {eq.status:<30}")
            print('-' * lenOfOutput)
        print()
#-----

#The list of equipment currently in the system.
all_equipment = [
    Equipment(#associated with the club meeting event
        1, "Lavalier Mic", "Microphone that clips to your shirt"
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

#some hardcoded display examples
all_equipment[0].status = EquipmentStatus.CLEANING
all_equipment[1].status = EquipmentStatus.IN_USE
all_equipment[2].status = EquipmentStatus.BROKEN
all_equipment[3].status = EquipmentStatus.IN_REPAIR
#==============================


#==============================
#Class representing an equipment request
# Vars:
#  * userID:  ID of the requesting user.
#  * equipID: ID of the requested equipment.
class EquipmentRequest:
    """Class representing an equipment request\n Vars:\n\t* userID: ID of the requesting user.\n\t* equipID: ID of the requested equipment."""
    def __init__(self, Event_ID):
        self.event_id = Event_ID
    #-----

    #Creates a request for an equipment
    def Add_Equipment_Request(userID, Event_ID):
        all_requests.append(EquipmentRequest(Event_ID))
        return
    #-----

    def Aproove_EquipmentRequest():
        """Aproove a user's request for equipment for their event"""
        print("Equipment request aprooved notification sent.")
        return
    #-----

    def Deny_EquipmentRequest():
        """Deny a user's request for equipment for their event"""
        print("Equipment request denied notification sent.")
        return
    #-----
#----------

#outputs a table of pending equipment requests in the system
def Query_Equipment_Requests():
    if len(all_requests) == 0:
        print("No pending requests...")
    else:
        print(f"{'Equipment Requests':^52}")
        print('-' * 52)
        for req in all_requests:
            print(f"{req.event_id.event_id:<3} | {req.event_id.requester:<15} | {req.event_id.name:<15} | {req.event_id.day_month}/{req.event_id.day_date}/{req.event_id.day_year}")
            for eq in req.event_id.equipment_ids:
                print(f"\t* {all_equipment[eq - 1].name:<15} | {all_equipment[eq - 1].description:<30}")
    print()
    return
#-----

#The list of all pending equipment requests.
all_requests = [
    EquipmentRequest(
        Schedule_event.all_events[0]
    ),
    EquipmentRequest(
        Schedule_event.all_events[1]
    ),
    EquipmentRequest(
        Schedule_event.all_events[2]
    ),
    EquipmentRequest(
        Schedule_event.all_events[4]
    )
]
"""The list of all pending equipment requests."""