import pygame
import random

class Pipes(pygame.sprite.Sprite):
    def __init__(self, fbGame, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()
        self.screen_height = fbGame.settings.screen_height

        self.image = pygame.image.load("images/pipe.png")
        self.rect = self.image.get_rect()
        self.gap = 150
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomright = [x, y - int(self.gap / 2)]
        if position == -1:
            self.rect.topright = [x, y + int(self.gap / 2)]
        
    def movePipe(self):
        self.rect.x -= 3
        if self.rect.x < -100:
            self.kill()