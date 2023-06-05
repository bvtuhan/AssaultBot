from Memory import *

entity_list_pointer = 0x591FCC


class Entity:
    health_offset = 0xEC

    xOffset = 0x4
    yOffset = 0x8
    zOffset = 0xC

    yawOffset = 0x34
    pitchOffset = 0X38


entity = Entity()

entity_list_base_address = procID.read_int(entity_list_pointer)

entity_base_address = procID.read_int(module_base_address + 0x17E0A8)
