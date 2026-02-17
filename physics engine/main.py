import pygame
from modules.public.drawer import Drawer
from modules.public.physics import Physics


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((3840, 2160), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.drawer = Drawer(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.drawer.clear((0, 0, 0))


            self.drawer.draw_grid(color=(76, 199, 10), grid_size=50, line_width=1)
            self.drawer.draw_axes(x=20, y=20, width=4)



            self.drawer.update()
            self.clock.tick(120)

game = Game()
game.run()
pygame.quit()