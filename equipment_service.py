from equipment_models import Equipment, EquipmentRequest, EquipmentStatus, EventEquipment
from equipment_state import equipment, equipment_requests, event_equipment
from query_service import get_event_by_id, get_equipment_by_id


def create_equipment(name, description):
    equipment_id = max((item.id for item in equipment), default=0) + 1
    item = Equipment(equipment_id, name, description)
    equipment.append(item)
    return item


def delete_equipment(equipment_id):
    item = get_equipment_by_id(equipment_id)
    if item is None:
        return False
    equipment.remove(item)
    equipment_requests[:] = [
        request for request in equipment_requests
        if request.equipment_id != equipment_id
    ]
    event_equipment[:] = [
        link for link in event_equipment
        if link.equipment_id != equipment_id
    ]
    return True


def create_equipment_request(event_id, equipment_id, reason=""):
    item = get_equipment_by_id(equipment_id)
    if item is None or item.status not in (
        EquipmentStatus.IN_STORAGE,
        EquipmentStatus.RESERVED,
    ):
        return False
    equipment_requests.append(EquipmentRequest(event_id, equipment_id, reason))
    if not any(
        link.event_id == event_id and link.equipment_id == equipment_id
        for link in event_equipment
    ):
        event_equipment.append(EventEquipment(event_id, equipment_id))
    return True


def approve_equipment_request(request):
    item = get_equipment_by_id(request.equipment_id)
    event = get_event_by_id(request.event_id)
    if item is None or event is None:
        return False
    item.status = EquipmentStatus.IN_USE
    item.assigned_user_id = event.requester_id
    equipment_requests.remove(request)
    return True


def deny_equipment_request(request):
    if request not in equipment_requests:
        return False
    equipment_requests.remove(request)
    return True


def set_equipment_status(item, status):
    if item not in equipment:
        return False
    item.status = status
    if status != EquipmentStatus.IN_USE:
        item.assigned_user_id = 0
    return True


def update_equipment(item, name, description):
    if item not in equipment:
        return False
    if name:
        item.name = name
    if description:
        item.description = description
    return True
