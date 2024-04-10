import pygame


class Background():
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()
        
        self.bg_img = pygame.image.load("images/bg.png")
        self.rect = self.bg_img.get_rect()
        self.rect.bottom = self.screen_rect.bottom

        
    def blitBg(self):
        self.screen.blit(self.bg_img, self.rect)
        