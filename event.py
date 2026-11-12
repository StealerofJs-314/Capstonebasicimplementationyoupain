from enum import Enum


class EventStatus(Enum):
    REQUESTED = 0
    APPROVED = 1
    DENIED = 2
    PAST_DATE = 3
    IN_PROGRESS = 4


class Event:
    _next_id = 1

    def __init__(
        self,
        time,
        day,
        month,
        year,
        building,
        room,
        name,
        requester_id,
        requester_name,
        status=EventStatus.IN_PROGRESS,
        decision_by_id=-1,
    ):
        self.id = Event._next_id
        Event._next_id += 1
        self.time = time
        self.day = day
        self.month = month
        self.year = year
        self.building = building
        self.room = room
        self.name = name
        self.requester_id = requester_id
        self.requester_name = requester_name
        self.status = status
        self.decision_by_id = decision_by_id

    def validate(self):
        reasons = []
        if not self.time:
            reasons.append("Time is missing.")
        if self.day == -1 or self.month == -1 or self.year == -1:
            reasons.append("Date is missing.")
        if not isinstance(self.building, str) or not self.building.strip():
            reasons.append("Building is missing.")
        if self.room == -1:
            reasons.append("Room is missing.")
        if not isinstance(self.requester_name, str) or not self.requester_name.strip():
            reasons.append("Requester is missing.")
        if self.requester_id == -1:
            reasons.append("Requester ID is missing.")
        return not reasons, reasons

    def submit(self):
        valid, reasons = self.validate()
        if valid:
            self.status = EventStatus.REQUESTED
        return valid, reasons

    def approve(self, admin_id):
        self.status = EventStatus.APPROVED
        self.decision_by_id = admin_id

    def deny(self, admin_id):
        self.status = EventStatus.DENIED
        self.decision_by_id = admin_id
