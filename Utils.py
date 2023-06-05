from Vector3 import *
from Offsets import *


def aimAt():
    local = Vector3(x=procID.read_float(entity_base_address + entity.xOffset),
                    y=procID.read_float(entity_base_address + entity.yOffset),
                    z=procID.read_float(entity_base_address + entity.zOffset))
    target = getClosestEnemy(local)
    yaw = local.yawAngle(target)
    pitch = local.pitchAngle(target)
    procID.write_float(entity_base_address + entity.yawOffset, yaw)
    procID.write_float(entity_base_address + entity.pitchOffset, pitch)


def getClosestEnemy(local: 'Vector3'):
    closestPlayer: 'Vector3' = None
    for index in range(0, 32):
        enemy_base = procID.read_int(entity_list_base_address + (index * 4))
        enemy_health = procID.read_int(enemy_base + entity.health_offset)
        if enemy_health < 0 or enemy_health > 100:
            continue
        enemy_coordinates = Vector3(procID.read_float(enemy_base + entity.xOffset),
                                    procID.read_float(enemy_base + entity.yOffset),
                                    procID.read_float(enemy_base + entity.zOffset))
        if closestPlayer is None or local.magnitude(closestPlayer) > local.magnitude(enemy_coordinates):
            closestPlayer = enemy_coordinates
    return closestPlayer


def shutdown():
    print("Exiting...")
    procID.write_int(entity_base_address + entity.health_offset, 100)
    procID.close_process()
    exit()
