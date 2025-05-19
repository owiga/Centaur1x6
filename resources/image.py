import pygame

from settings import IMAGE_SIZE


class Image(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.source = "images/centaurQ.jpg"
        self.original_image = pygame.Surface(IMAGE_SIZE, pygame.SRCALPHA)
        self.loaded_image = pygame.image.load(self.source).convert_alpha()
        self.original_image = pygame.transform.scale(self.loaded_image, IMAGE_SIZE)
        self.rect = self.original_image.get_rect()
        self.rounded_image()

    def rounded_image(self):
        self.rect_image = pygame.Surface(IMAGE_SIZE, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *IMAGE_SIZE), border_radius=5)
        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

    def add_outline(self):
        self.border = pygame.Rect(0, 0, *self.original_image.get_size())
        self.border_color = (100, 34, 26)
        pygame.draw.rect(self.image, self.border_color, self.border, 2, border_radius=7)