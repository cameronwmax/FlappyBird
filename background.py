import pygame


class Background():
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()
        
        self.bg_img = pygame.image.load("images/bg1.png").convert()
        self.rect = self.bg_img.get_rect()

        self.scroll = 0
        
    def blitBg(self):
        for i in range(1):
            self.screen.blit(self.bg_img, (i * self.rect.x + self.scroll, 0))

        # self.scroll -= 5

        # if self.scroll < -500:
        #     self.scroll = 0

        