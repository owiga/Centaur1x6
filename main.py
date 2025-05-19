import pygame
import sys

from resources.bar import Bar
from settings import RESOLUTION, WHITE, IMAGE_SIZE

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.bar = Bar(self.screen)
        self.skill_image = pygame.image.load("images/centaurQ.jpg")
        pygame.display.set_caption("Centaur Q")

    def run(self):
        while True:
            time = self.clock.tick() / 1000.0
            self.screen.fill(WHITE)
            self.bar.update(time)
            self.screen.blit(self.bar.get_score(), (RESOLUTION[0] // 2 - self.bar.get_score().get_rect().size[0] // 2, RESOLUTION[0] // 4))
            self.screen.blit(self.bar.get_scoreSkill(), (self.bar.image.rect.x + IMAGE_SIZE[0] // 2.6, RESOLUTION[0] // 1.38))
            self.screen.blit(self.bar.get_tutorial(), (RESOLUTION[0] // 2 - self.bar.get_tutorial().get_rect().size[0] // 2, RESOLUTION[0] // 3.2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if not self.bar.check_collide():
                        self.bar.miss()
                    else:
                        self.bar.hit()
            pygame.display.flip()


if __name__ == '__main__':
    engine = Game()
    engine.run()
