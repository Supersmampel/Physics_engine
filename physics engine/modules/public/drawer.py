import pygame
from pygame import gfxdraw

class Drawer:
    def __init__(self, screen, backgroundcolor = (0, 0, 0)):
        self.screen = screen
        self.backgroundcolor = backgroundcolor
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.center_cords = self.get_center_cords()
    
    """
    Het scherm updaten:
        - clear: Reset het scherm
        - update: Tekent wat er naar het scherm geschreven is
    """
    def clear(self):
        self.screen.fill(self.backgroundcolor)

    def update(self):
        pygame.display.flip()

    """
    Viguren tekenen:
        - draw_circle: Tekent een cirkel
    """

    def get_center_cords(self):
        return (self.width / 2, self.height / 2)
    
    def get_cords(self, x, y):
        return (self.center_cords[0] + x, self.center_cords[1] - y)

    def draw_circle(self, color:tuple|list, x:float, y:float, radius:float, outline_radius:float=7, outline_color:tuple|list=(255, 255, 255), anti_aliasing:bool=True):
        cords = self.get_cords(x, y)
        if anti_aliasing:
            gfxdraw.filled_circle(self.screen, int(cords[0]), int(cords[1]), int(radius), outline_color)
            gfxdraw.aacircle(self.screen, int(cords[0]), int(cords[1]), int(radius), outline_color)
            gfxdraw.filled_circle(self.screen, int(cords[0]), int(cords[1]), int(radius) - outline_radius, color)
            gfxdraw.aacircle(self.screen, int(cords[0]), int(cords[1]), int(radius) - outline_radius, color)
        else:
            gfxdraw.filled_circle(self.screen, int(cords[0]), int(cords[1]), int(radius), outline_color)
            gfxdraw.filled_circle(self.screen, int(cords[0]), int(cords[1]), int(radius) - outline_radius, color)
        
    def draw_line(self, color:tuple|list, point_1:tuple, point_2:tuple):
        point_1 = self.get_cords(point_1[0], point_1[1])
        point_2 = self.get_cords(point_2[0], point_2[1])
        gfxdraw.line(self.screen, int(point_1[0]), int(point_1[1]), int(point_2[0]), int(point_2[1]), color)
    
    def draw_polygon(self, color, *points):
        cords = []
        for point in points:
            cords.append(self.get_cords(point[0], point[1]))
        gfxdraw.filled_polygon(self.screen, cords, (35, 69, 14))
        gfxdraw.aapolygon(self.screen, cords, (0, 0, 0))