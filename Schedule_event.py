from enum import Enum


class Approval_Status(Enum):
    REQUESTED = 0
    APPROVED = 1
    DENIED = 2
    PASTDATE = 3
    IN_PROGRESS=4

class Schedule_event():

    def __init__(self, time=-1, day_date=-1, day_month=-1, day_year=-1,
                 building="", room=-1, name="", requester = "",requesterID= -1):
        self.time = time
        self.day_date = day_date
        self.day_month = day_month
        self.day_year = day_year
        self.building = building
        self.room = room
        self.name = name
        self.requester = requester
        self.requesterID = requesterID
        self.approved = Approval_Status.IN_PROGRESS
        self.approved_or_denied_by_id = -1

        self.staff_assigned = [] # singled digit for regular staff, 10s for security, 20s for cleaning, 30s for equipment_mananger

    def add_staff(self, Id):
        self.staff_assigned.append(Id)


    def approve(self,ID):
        self.approved = Approval_Status.APPROVED
        self.approved_or_denied_by_id = ID

    def denied(self, ID):
        self.approved = Approval_Status.DENIED
        self.approved_or_denied_by_id = ID

    def valid(self):
        reasons = []

        if self.time == -1:
            reasons.append("Time is missing.")
        if self.day_date == -1:
            reasons.append("Day is missing.")
        if self.day_month == -1:
            reasons.append("Month is missing.")
        if not isinstance(self.building, str) or not self.building.strip():
            reasons.append("Building is missing.")
        if self.room == -1:
            reasons.append("Room is missing.")
        if not isinstance(self.requester, str) or not self.requester.strip():
            reasons.append("Requester is missing.")
        if self.requesterID == -1:
            reasons.append("Requester ID is missing.")

        return not reasons, reasons
    def submit(self):
        is_valid, reasons = self.valid()
        if not is_valid:
            return is_valid, reasons
        self.approved = Approval_Status.REQUESTED
        return True, ""

    def __str__(self):
        is_valid, _ = self.valid()
        if not is_valid or self.approved == Approval_Status.IN_PROGRESS:
            return ""

        fields = (
            ("Name", self.name),
            ("Time", self.time),
            ("Day", self.day_date),
            ("Month", self.day_month),
            ("Year", self.day_year),
            ("Building", self.building),
            ("Room", self.room),
            ("Requester", self.requester),
            ("Status", self.approved.name),
        )
        return "\n".join(
            f"{label}: {value}"
            for label, value in fields
            if value != -1 and value != ""
        )


def sort_events_by_requester_id(all_events):
    return sorted(all_events, key=lambda event: event.requesterID)

# TODO: Implement ts
def search_rooms():
    print("Room search needs to be implemented.")
    return


def get_events_by_staff_id(all_events, staff_ID):
    return [
        event
        for event in all_events
        if staff_ID in event.staff_assigned
    ]


def get_requested_events(all_events):
    return [
        event
        for event in all_events
        if event.approved == Approval_Status.REQUESTED
    ]
    


all_events = [
    Schedule_event(
        time="09:00", day_date=12, day_month=11, day_year=2026,
        building="Main", room=101, name="Club Meeting",
        requester="Alex", requesterID=1001,
    ),
    Schedule_event(
        time="13:30", day_date=14, day_month=11, day_year=2026,
        building="Arts", room=204, name="Art Workshop",
        requester="Alex", requesterID=1001,
    ),
    Schedule_event(
        time="10:00", day_date=16, day_month=11, day_year=2026,
        building="Science", room=12, name="Science Fair",
        requester="Sam", requesterID=1003,
    ),
    Schedule_event(
        time="15:00", day_date=18, day_month=11, day_year=2026,
        building="Main", room=202, name="Study Group",
        requester="Taylor", requesterID=1004,
    ),
    Schedule_event(
        time="11:00", day_date=20, day_month=11, day_year=2026,
        building="Gym", room=1, name="Basketball Practice",
        requester="Morgan", requesterID=1005,
    ),
]

all_events[0].add_staff(11)
all_events[0].add_staff(21)
all_events[1].add_staff(22)
all_events[2].add_staff(4)

all_events[0].approve(1)
all_events[1].approve(2)
all_events[4].denied(1)

