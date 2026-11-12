from enum import Enum


class EquipmentStatus(Enum):
    IN_STORAGE = 0
    RESERVED = 1
    IN_USE = 2
    CLEANING = 3
    BROKEN = 4
    IN_REPAIR = 5


class Equipment:
    def __init__(self, equipment_id, name, description=""):
        self.id = equipment_id
        self.name = name
        self.description = description
        self.status = EquipmentStatus.IN_STORAGE
        self.assigned_user_id = 0


class EventEquipment:
    def __init__(self, event_id, equipment_id):
        self.event_id = event_id
        self.equipment_id = equipment_id


class EquipmentRequest:
    def __init__(self, event_id, equipment_id, reason=""):
        self.event_id = event_id
        self.equipment_id = equipment_id
        self.reason = reason
