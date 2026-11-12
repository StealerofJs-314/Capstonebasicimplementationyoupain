from equipment_models import (
    Equipment,
    EquipmentRequest,
    EquipmentStatus,
    EventEquipment,
)


equipment = [
    Equipment(1, "Lavalier Mic", "Microphone that clips to your shirt"),
    Equipment(2, "Kiln", "Used for firing clay into pottery"),
    Equipment(3, "Microscope", "Used for viewing microscopic objects"),
    Equipment(4, "Basketball", "Used for playing basketball"),
]

equipment[0].status = EquipmentStatus.CLEANING
equipment[1].status = EquipmentStatus.IN_USE
equipment[2].status = EquipmentStatus.BROKEN
equipment[3].status = EquipmentStatus.IN_REPAIR

event_equipment = [
    EventEquipment(1, 1),
    EventEquipment(2, 2),
    EventEquipment(3, 3),
    EventEquipment(5, 4),
]

equipment_requests = [
    EquipmentRequest(2, 2, "Art Workshop"),
]
