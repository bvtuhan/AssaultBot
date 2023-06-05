import math


class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self, target: 'Vector3'):
        return math.sqrt(math.pow(target.x - self.x, 2) +
                         math.pow(target.y - self.y, 2) + math.pow(target.z - self.z, 2))

    def yawAngle(self, target: 'Vector3'):
        return math.atan2(target.y - self.y, target.x - self.x) * (180 / math.pi) + 90

    def pitchAngle(self, target: 'Vector3'):
        return math.asin((target.z - self.z) / self.magnitude(target)) * (180 / math.pi)
