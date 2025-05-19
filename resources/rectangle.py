import pygame


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, size: tuple, color: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.Surface(size)
        self.original_image.fill(color)
        self.image = self.original_image
        self.rect = self.image.get_rect()

    def set_rounded(self, roundness):
        size = self.original_image.get_size()
        self.rect_image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)
        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

    def add_outline(self):
        self.border = pygame.Rect(0, 0, *self.original_image.get_size())
        self.border_color = (100, 34, 26)
        pygame.draw.rect(self.image, self.border_color, self.border, 2, border_radius=7)
