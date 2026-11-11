#----------
#Equipment.py
#==========
#  * Defines equipment in the sytem and the functions to request it
#----------

from enum import Enum
import Schedule_event   #used for making requests

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
    #No status for sold as its no longer tracked by the system
#----------


#Class representing a piece of equipment.
class Equipment:
    """Class representing a piece of equipment."""
    def __init__(self, ID = -1, Name = "", Desc = ''):
        self.id = ID              #ID of the equipment
        self.name = Name          #Name of the equipment
        self.description = Desc   #Description of the equipment
        self.status = EquipmentStatus.CLEANING
        self.assigned = 0      #userID that currently has the equipment
    #----------

    #adds equipment to the list
    def Add_Equipment():


        return
    #----------

    #removes equipment from the list
    def Remove_Equipment():

        return
    #----------
#----------

#outputs a table of equipment in the system
def Query_Equipment():
    lenOfOutput = 3 + 15 + 70 + 30 + 6 + (3 * 4) #each header + column spacing = 139
    print(f"{'EQUIPMENT':^139}")
    print(f"{'ID':<3} | {'Name':^15} | {'Description':^70} | {'Status':^30} | {'Assigned':<6}")
    print('-' * lenOfOutput)
    if len(all_equipment) > 0:
        for eq in all_equipment:
            print(f"{eq.id:<3} | {eq.name:<15} | {eq.description:<70} | {eq.status:<30} | {eq.assigned:<6}")
            print('-' * lenOfOutput)
        print()
    elif len(all_equipment) == 0:
        print(f"{'No equipment...':^139}")
#----------


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
#Class representing an equipment request
# Vars:
#  * userID:  ID of the requesting user.
#  * equipID: ID of the requested equipment.
class EquipmentRequest:
    """Class representing an equipment request\n Vars:\n\t* userID: ID of the requesting user.\n\t* equipID: ID of the requested equipment."""
    def __init__(self, userID, equipID, reason):
        self.userID = userID
        self.equipID = equipID
        self.reason = reason
    #----------

    def Add_Equipment_Request(userID, equipID):
        if all_equipment[equipID].status != 0 or all_equipment[equipID].status != 1:
            print("We're sorry. That is not available at this time.")
        else:
            all_requests.append(EquipmentRequest(userID, equipID))

        return
    #----------

    def Aproove_EquipmentRequest(requestID):
        """Aproove a user's request for equipment for their event"""
        #updates the associated equipment to be IN_USE and assigned to the requesting userID
        all_equipment[all_requests[requestID].equipID].status = EquipmentStatus.IN_USE
        all_equipment[all_requests[requestID].equipID].assigned = all_requests[requestID].userID
        #removes the request from the list
        all_requests.__delitem__(requestID)
        print("Request aprooval notification sent.")
        return
    #----------

    def Deny_EquipmentRequest(requestID):
        """Deny the user's request for equipment for their event"""
        #removes the request from the list
        all_requests.__delitem__(requestID)
        print("Request denied notification sent.")
        return
    #----------
#----------


#outputs a table of equipment requests in the system
def Query_Equipment_Requests():
    #basically a selection over a join of the Equipment_Reservations and Schedule_Event tables
    lenOfOutput = 3 + 6 + 15 + 15 + 6 + 10 + 20 + 6 + 15 + 21 + (3 * 9) #each header + column spacing = 144
    counter = 0
    print(f"{'EQUIPMENT REQUESTS':^144}")
    print('-' * lenOfOutput)
    print(f"{'':<3} | {'userID':^6} | {'Username':^15} | {'Event Name':^15} | {'Time':^6} | {'Event Date':^10} | {'Building':^20} | {'Room':^6} | {'Equipment Name':^15} | {'Equipment Description':^21}")
    print('-' * lenOfOutput)
    if len(all_requests) > 0:
        for req in all_requests:
            for event in Schedule_event.all_events:
                if req.userID == event.requesterID:
    #problem: This returns the first matching event information even if the equipment does not match
                    print(f"{counter:^3} | {req.userID:^6} | {event.requester:^15} | {event.name:^15} | {event.time:>6} | {event.day_month:>2}/{event.day_date:>2}/{event.day_year:>4} | {event.building:^20} | {event.room:^6} | {all_equipment[req.equipID].name:^15} | {all_equipment[req.equipID].description:<21}")
                    print('-' * lenOfOutput)
                    counter += 1
                break
    elif len(all_requests) == 0:
        print(f"{'No pending requests...':^144}")
    return
#----------

#The list of all pending equipment requests.
all_requests = [
    EquipmentRequest(
        Schedule_event.all_events[1].requesterID, 1, Schedule_event.all_events[1].name
    )
]
"""The list of all pending equipment requests."""