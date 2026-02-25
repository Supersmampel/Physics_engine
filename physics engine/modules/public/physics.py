import math
import pygame.math as pymath



class Physics:
    def __init__(self, drawer, gravity=0.07, air_tightness=0.5):
        self.math = math
        self.vector = pymath.Vector2
        self.drawer = drawer
        self.gravity = gravity
        self.air_tightness = air_tightness
        self.drag_coefficient_circle = 0.47  # uit binask
        self.scale = 50
    
    def init_ball(self, x, y, radius, vx=0, vy=0, density=10, bounciness=0.8, static=False):
        return {
            "type": "ball",
            "position": self.vector(x, y),
            "radius": radius,
            "density": density,
            "mass": density * (4/3) * self.math.pi * (radius**3),   # m = p * 3/4 * pi * r^3
            "velocity": self.vector(vx, vy),
            "bounciness": bounciness,
            "frontal_surface": self.math.pi * (radius**2),
            "visible": True
        }

    def init_line(self, x1, y1, x2, y2, friction=0.8):
        p1 = self.vector(x1, y1)
        p2 = self.vector(x2, y2)
        line = p2 - p1
        edge = self.vector(-line.y, line.x)     # Vector loodrecht op de lijn vanaf de rand
        n_edge = self.vector(line.y, -line.x)
        return {
            "type": "floor",
            "point_1": p1,
            "point_2": p2,
            "positive_n": edge,
            "negative_n": n_edge,
            "edge_normal": edge,
            "friction": friction,
            "visible": True
        }

    def init_static_polygon(self, color, *points):
        def init_polygon_lines():
            return

        lines = []
        lenght = len(points)
        for i in range(lenght):
            if i == lenght-1:
                lines.append((self.vector(points[i]), self.vector(points[0])))
            else:
                lines.append((self.vector(points[i]), self.vector(points[i+1])))
        
        def_lines = []
        for line in lines:
            def_lines.append(self.init_line(line[0][0], line[0][1], line[1][0], line[1][1]))
        print(def_lines)

        return {
            "type": "polygon_floor",
            "points": points,
            "color": color
        }
    
    def apply_gravity(self, object, dt):
        object["position"] += object["velocity"] * dt
        # Fz = m * g
        # a = g
        object["velocity"][1] -= self.gravity * dt
        # Fd = 0.5 * p * Cd * A * v^2
        v = object["velocity"]
        speed = self.vector.length(v)

        if speed > 0:
            drag_force = (
                -0.5
                * self.air_tightness
                * self.drag_coefficient_circle
                * object["frontal_surface"]
                * speed
                * v
            )

            acceleration = drag_force / object["mass"]
            object["velocity"] += acceleration * dt
    
    def points_towards_direction(self, velocity, normal):
        return velocity.dot(normal) < 0

    def distance_to_normal_direction(self, point, normal):
        return normal.dot(point)
    
    def ball_to_wall_colission(self, ball, wall):
        if self.points_towards_direction(ball["velocity"], wall["normal"]):
            if self.distance_to_normal_direction(ball["position"]) <= 0 + ball["radius"]:
                # v_new ​= v − (1 + e)(v * n) n
                v = ball["velocity"]
                n = wall["normal"]
                e = .9  # later verranderen
                ball["velocity"] = v - (1 + e) * v.dot(n) * n
                return True
        return False

    
    
    def update(self, object, dt):
        for object in object:
            if object["type"] == "floor":
                self.drawer.draw_line((0, 0, 0), object["point_1"], object["point_2"])
            if object["type"] == "ball":
                self.drawer.draw_circle((69, 173, 68), object["position"][0], object["position"][1], object["radius"])
                self.apply_gravity(object, dt)
                self.ball_to_wall_colission(object, object["lines"])
            if object["type"] == "polygon_floor":
                self.drawer.draw_polygon(object["color"], *object["points"])
        
        for floor in object["floor"]:
            if floor["visible"]:
                self.drawer.draw_line((0, 0, 0), floor["point_1"], floor["point_2"])
        
        for ball in object["ball"]:
            if ball["visible"]:
                self.apply_gravity(ball, dt)
                self.ball_to_wall_collission(ball, object["lines"])
        
        for polygon in object["polygon_floor"]:
            if polygon["visible"]:
                self.drawer.draw_polygon(polygon["color"], *polygon["points"])
                