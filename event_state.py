from event import Event, EventStatus


events = [
    Event(
        "09:00", 12, 11, 2026, "Main", 101, "Club Meeting", 1001, "Alex",
        status=EventStatus.APPROVED, decision_by_id=9001,
    ),
    Event(
        "13:30", 14, 11, 2026, "Arts", 204, "Art Workshop", 1001, "Alex",
        status=EventStatus.APPROVED, decision_by_id=9002,
    ),
    Event(
        "10:00", 16, 11, 2026, "Science", 12, "Science Fair", 1003, "Sam",
        status=EventStatus.REQUESTED,
    ),
    Event(
        "15:00", 18, 11, 2026, "Main", 202, "Study Group", 1004, "Taylor",
        status=EventStatus.REQUESTED,
    ),
    Event(
        "11:00", 20, 11, 2026, "Gym", 1, "Basketball Practice", 1005, "Morgan",
        status=EventStatus.DENIED, decision_by_id=9001,
    ),
]
