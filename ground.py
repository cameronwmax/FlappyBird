import pygame

class Ground():
    def __init__(self, fbGame):
        self.screen = fbGame.screen

        self.image = pygame.image.load("images/ground.png")
        self.rect = self.image.get_rect()


        self.scroll = 0
        self.speed = 0



    def blitGround(self):
        self.screen.blit(self.image, (self.scroll, 520))
        self.scroll -= self.speed
        if abs(self.scroll) > 35:
            self.scroll = 0
