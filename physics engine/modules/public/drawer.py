import pygame
import math

class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def draw_rect(self, color, x, y, width, height):
        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def draw_circle(self, color, x, y, r):
        pygame.draw.circle(self, color, (x, y), r)
    
    def draw_line(self, color, start_pos, end_pos, width=1):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def draw_polygon(self, color, point_list):
        pygame.draw.polygon(self.screen, color, point_list)

    def draw_text(self, text, font, font_size, color, x, y):
        font = pygame.font.SysFont(font, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def update(self):
        pygame.display.flip()
    
    def draw_image(self, image, x, y, angle=0, scale=1):
        rotated_image = pygame.transform.rotate(image, angle)
        scaled_image = pygame.transform.scale(rotated_image, (int(rotated_image.get_width() * scale), int(rotated_image.get_height() * scale)))
        self.screen.blit(scaled_image, (x, y))

    def get_screen(self):
        return self.screen
    
    def get_width(self):
        return self.screen.get_width()
    
    def get_height(self):
        return self.screen.get_height()
    
    def get_center(self):
        return (self.get_width() // 2, self.get_height() // 2)
    
    def draw_polygon_outline(self, color, point_list, width=1):
        pygame.draw.polygon(self.screen, color, point_list, width)

    def draw_circle_outline(self, color, x, y, r, width=1):
        pygame.draw.circle(self.screen, color, (x, y), r, width)
    
    def draw_rect_outline(self, color, x, y, width, height, outline_width=1):
        pygame.draw.rect(self.screen, color, (x, y, width, height), outline_width)
    
    def draw_line_outline(self, color, start_pos, end_pos, width=1, outline_width=1):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width + outline_width)
    
    def draw_text_outline(self, text, font, font_size, color, outline_color, x, y, outline_width=1):
        font = pygame.font.SysFont(font, font_size)
        text_surface = font.render(text, True, color)
        outline_surface = font.render(text, True, outline_color)
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    self.screen.blit(outline_surface, (x + dx, y + dy))
        self.screen.blit(text_surface, (x, y))
    
    def draw_image_outline(self, image, x, y, angle=0, scale=1, outline_color=(255, 255, 255), outline_width=1):
        rotated_image = pygame.transform.rotate(image, angle)
        scaled_image = pygame.transform.scale(rotated_image, (int(rotated_image.get_width() * scale), int(rotated_image.get_height() * scale)))
        outline_image = pygame.Surface((scaled_image.get_width() + 2 * outline_width, scaled_image.get_height() + 2 * outline_width), pygame.SRCALPHA)
        outline_image.fill(outline_color)
        outline_image.blit(scaled_image, (outline_width, outline_width))
        self.screen.blit(outline_image, (x - outline_width, y - outline_width))
    
    def draw_grid(self, color=(255, 255, 255), x=0, y=0, line_width = 5, grid_size=20):
        width = self.get_width()
        height = self.get_height()
        for i in range(0, width, grid_size):
            self.draw_line(color, (i + x, height), (i + x, 0), line_width)
        for i in range(0, height, grid_size):
            self.draw_line(color, (0, height-(i + y)), (width, height-(i + y)), line_width)
    
    def draw_arrow(self, color, start_pos, end_pos, width=5):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)
        angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
        arrow_length = 10
        arrow_angle = 0.5
        left_arrow = (end_pos[0] - arrow_length * math.cos(angle - arrow_angle), end_pos[1] - arrow_length * math.sin(angle - arrow_angle))
        right_arrow = (end_pos[0] - arrow_length * math.cos(angle + arrow_angle), end_pos[1] - arrow_length * math.sin(angle + arrow_angle))
        pygame.draw.line(self.screen, color, end_pos, left_arrow, width)
        pygame.draw.line(self.screen, color, end_pos, right_arrow, width)
    
    def draw_axes(self, color1=(255, 0, 0), color2=(0, 0, 255), x=15, y=15, length=100, width=2):
        y = self.get_height() - y
        self.draw_arrow(color1, (x, y), (x + length, y), width=width)
        self.draw_arrow(color2, (x, y), (x, y - length), width=width)

    def get_clock(self):
        return pygame.time.Clock()
    
    def get_time(self):
        return pygame.time.get_ticks()
    
    def get_fps(self):
        return self.get_clock().get_fps()
    
    def get_delta_time(self):
        return self.get_clock().tick(60) / 1000.0