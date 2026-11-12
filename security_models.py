class SecurityRequest:
    def __init__(self, event_id, personnel_count, start_time, duration):
        self.event_id = event_id
        self.personnel_count = personnel_count
        self.start_time = start_time
        self.duration = duration


class SecurityPersonnel:
    def __init__(self, personnel_id, name, rank, available_days):
        self.id = personnel_id
        self.name = name
        self.rank = rank
        self.available_days = available_days
