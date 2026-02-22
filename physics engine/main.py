import pygame
from modules.public.drawer import Drawer
from modules.public.physics import Physics

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
target_fps = 120
dt = 1


class Static_color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.color = (r, g, b)

background = Static_color(11, 161, 139)
drawer = Drawer(screen, background.color)
physics = Physics(drawer)
ball = Static_color(69, 173, 68)

objects = [
    physics.init_ball(-200, 0, 30),
    physics.init_ball(200, 0, 30),
    physics.init_static_polygon((0, 0, 0), (-800, -500), (800, -500), (0, -400))
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawer.clear()
    physics.update(objects, dt)
    
    


    drawer.update()
    dt = clock.get_fps() / target_fps
    clock.tick(target_fps)