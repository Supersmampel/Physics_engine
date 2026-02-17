import math
from pygame import math as pymath

class Physics:
    def __init__(self, drawer):
        self.drawer = drawer

    def init_static_floor(self, pos1, pos2, angle=0):
        return {
            'pos': (pos1, pos2),
            'angle': angle,
            'normal': self.calculate_normal(pos1, pos2, angle),
            'static': True,
            'edge_normals': (self.calculate_normal(pos1, pos2, angle),self.calculate_normal(pos2, pos1, angle))
            }
    
    def init_dynamic_ball(self, position, vx, vy, radius):
        return {
            'position': position,
            'velocity': (vx, vy),
            'normal': self.calculate_normal((position[0], position[1] + radius), position, 0),
            'radius': radius,
            'static': False
        }
    
    def collision_ballToFloor(self, ball, floor):
        ball_to_floor = (ball['position'][0] - floor['pos'][0][0], ball['position'][1] - floor['pos'][0][1])
        distance = ball_to_floor[0] * floor['normal'][0] + ball_to_floor[1] * floor['normal'][1]
        if distance < ball['radius']:
            return True
        return False

    def calculate_normal(self, pos1, pos2, angle):
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        length = math.hypot(dx, dy)
        if length == 0:
            return (0, 0)
        normal_x = -dy / length
        normal_y = dx / length
        cos_angle = math.cos(math.radians(angle))
        sin_angle = math.sin(math.radians(angle))
        rotated_normal_x = normal_x * cos_angle - normal_y * sin_angle
        rotated_normal_y = normal_x * sin_angle + normal_y * cos_angle
        return (rotated_normal_x, rotated_normal_y)

    def update(self, obj):
        obj.position[0] += obj.velocity[0] * self.drawer.get_delta_time()
        obj.position[1] += obj.velocity[1] * self.drawer.get_delta_time()
    
    def apply_gravity(self, obj, gravity=9.81):
        obj.velocity[1] += gravity * self.drawer.get_delta_time()

    def apply_friction(self, obj, friction_coefficient=0.1):
        obj.velocity[0] *= (1 - friction_coefficient * self.drawer.get_delta_time())
        obj.velocity[1] *= (1 - friction_coefficient * self.drawer.get_delta_time())
