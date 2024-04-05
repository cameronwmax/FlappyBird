import pygame


class Bird:
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()

        self.fallingSpeed = 1
        self.isFalling = True
        

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

    def updateFrame(self):
        self.currentFrame += 0.2
        if self.currentFrame >= len(self.frames):
            self.currentFrame = 0
        self.image = self.frames[int(self.currentFrame)]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def flap(self):
        self.rect.y -= 50
        self.fallingSpeed = 1

    def movement(self):
        if self.isFalling:
            self.fallingSpeed += .1
            self.rect.y += self.fallingSpeed

    def centerBird(self):
        self.rect.y = 300
