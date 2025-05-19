from pickle import FRAME

import pygame
import random

from resources.rectangle import Rectangle
from resources.image import Image
from settings import BAR_SIZE, BAR_PROGRESS_SIZE, BAR_CLICKABLE_SIZE, RESOLUTION, RED, IMAGE_SIZE


class Bar:
    def __init__(self, screen):
        self.static_y = RESOLUTION[0] // 1.4
        self.bar = Rectangle(BAR_SIZE, color=(51, 4, 5)) # ,
        self.bar.rect.x = RESOLUTION[0] // 4 - IMAGE_SIZE[0] // 2
        self.bar.rect.y = RESOLUTION[0] // 1.4
        self.bar.set_rounded(5)
        self.bar.add_outline()

        self.bar_clickable_sprite = Rectangle(BAR_CLICKABLE_SIZE, color=(187, 45, 26))
        self.bar_clickable_sprite.rect.x = (random.randint(RESOLUTION[0] // 4 - IMAGE_SIZE[0] // 2, RESOLUTION[0] // 4 + BAR_SIZE[0] - IMAGE_SIZE[0] // 2))
        self.bar_clickable_sprite.rect.y = self.static_y
        self.bar_clickable_sprite.set_rounded(2)

        self.bar_progress_sprite = Rectangle(BAR_PROGRESS_SIZE, color=(188, 150, 110))
        self.bar_progress_sprite.set_rounded(3)
        self.bar_progress_sprite.rect.center = (RESOLUTION[0] // 4 + 15 // 2,
                                                self.static_y + BAR_PROGRESS_SIZE[1] // 2)
        self.bar_progress_x = RESOLUTION[0] // 4 - IMAGE_SIZE[0] // 2

        self.image = Image()
        self.image.rect.y = self.static_y - self.image.rect.size[1] / 4
        self.image.rect.x = RESOLUTION[0] // 4 - IMAGE_SIZE[0] // 2 + BAR_SIZE[0]
        self.image.add_outline()


        self.score_font = pygame.font.SysFont('None', 60)
        self.tutorial_font = pygame.font.SysFont('None', 36)
        self.current_score = 0
        self.score = self.score_font.render(f"Текущие очки: {self.current_score}", True, (255, 0, 0))
        self.score_skill = self.score_font.render(str(self.current_score), False, (255, 255, 255)).convert()
        self.score_skillOut = self.create_outlined_text(self.score_font, str(self.current_score), (255, 255, 255), (0, 0, 0), 1)

        self.tutorial = self.tutorial_font.render("При наведении красной полоски на красную шкалу жмите 'E'!", True, (255, 0, 0))

        self.bar_group = pygame.sprite.Group([self.bar, self.bar_clickable_sprite, self.bar_progress_sprite, self.image])
        self.screen = screen

    def update(self, time):
        self.bar_progress_x += 250 * time
        self.bar_group.draw(self.screen)
        self.bar_progress_sprite.rect.x = self.bar_progress_x
        if self.bar_progress_x >= RESOLUTION[0] // 4 + BAR_SIZE[0] - BAR_PROGRESS_SIZE[0] - IMAGE_SIZE[0] // 2:
            self.miss()

    def miss(self):
        self.bar_progress_x = RESOLUTION[0] // 4 - BAR_PROGRESS_SIZE[0] - IMAGE_SIZE[0] // 2
        self.current_score -= 1 if self.current_score > 0 else 0
        self.score = self.score_font.render(f"Текущие очки: {self.current_score}", True, (255, 0, 0))
        self.score_skillOut = self.create_outlined_text(self.score_font, str(self.current_score), (255, 255, 255),
                                                        (0, 0, 0), 1)
        self.bar_clickable_sprite.rect.x = (random.randint(RESOLUTION[0] // 4 - IMAGE_SIZE[0] // 2,
                                                           RESOLUTION[0] // 4 + BAR_SIZE[0] - IMAGE_SIZE[0] // 2 - BAR_CLICKABLE_SIZE[0]))

    def get_score(self):
        return self.score

    def get_scoreSkill(self):
        return self.score_skillOut

    def get_tutorial(self):
        return self.tutorial

    def hit(self):
        self.bar_clickable_sprite.rect.x = (random.randint(RESOLUTION[0] // 4 - IMAGE_SIZE[0] // 2,
                                                          RESOLUTION[0] // 4 + BAR_SIZE[0] - IMAGE_SIZE[0] // 2 -
                                                          BAR_CLICKABLE_SIZE[0]))
        self.bar_progress_x = RESOLUTION[0] // 4
        self.current_score += 1
        self.score = self.score_font.render(f"Текущие очки: {self.current_score}", True, (255, 0, 0))
        self.score_skillOut = self.create_outlined_text(self.score_font, str(self.current_score), (255, 255, 255),
                                                        (0, 0, 0), 1)

    def check_collide(self):
        return pygame.sprite.collide_rect(self.bar_progress_sprite, self.bar_clickable_sprite)

    @staticmethod
    def create_outlined_text(font, text, text_color, outline_color, outline_width):
        """Более эффективный метод с предварительным рендерингом"""
        text_surface = font.render(text, True, text_color)
        w, h = text_surface.get_size()

        # Создаем поверхность с обводкой
        outline_surface = pygame.Surface((w + 2 * outline_width, h + 2 * outline_width), pygame.SRCALPHA)

        # Рисуем обводку
        for dx, dy in [(x, y) for x in (-outline_width, 0, outline_width)
                       for y in (-outline_width, 0, outline_width) if x or y]:
            outline_surface.blit(font.render(text, True, outline_color), (outline_width + dx, outline_width + dy))

        # Рисуем основной текст
        outline_surface.blit(text_surface, (outline_width, outline_width))

        return outline_surface