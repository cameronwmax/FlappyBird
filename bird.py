import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, fbGame):
        pygame.sprite.Sprite.__init__(self)
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()        

        imgs = [
            pygame.image.load("images/frame-1.png"),
            pygame.image.load("images/frame-2.png"),
            pygame.image.load("images/frame-3.png"),
            pygame.image.load("images/frame-4.png"),
            pygame.image.load("images/frame-5.png"),
            pygame.image.load("images/frame-6.png"),
            pygame.image.load("images/frame-7.png"),
            pygame.image.load("images/frame-8.png")
        ]
 
        self.frames = []
        for img in imgs:
            self.frames.append(pygame.transform.scale(img, (50, 50)))
        
        self.currentFrame = 0
        self.image = self.frames[self.currentFrame]

        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.velocity = 0

    def updateFrame(self):
        self.currentFrame += 0.2
        if self.currentFrame >= len(self.frames):
            self.currentFrame = 0
        self.image = self.frames[int(self.currentFrame)]

        self.image = pygame.transform.rotate(self.image, self.velocity * -2)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def flap(self):
        self.velocity = -9

    def gravity(self):
        self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        self.rect.y += int(self.velocity)

    def centerBird(self):
        self.rect.y = 300
