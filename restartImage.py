import pygame

class Restart:
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/restart.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitRestart(self):
        self.screen.blit(self.image, self.rect)