import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, fbGame):
        pygame.sprite.Sprite.__init__(self)
        pygame.mixer.init()
        
        self.flap_sound = pygame.mixer.Sound("sounds/flap.mp3")
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()    

        self.flying = False    

        self.frames = [
            pygame.image.load("images/bird1.png"),
            pygame.image.load("images/bird2.png"),
            pygame.image.load("images/bird3.png"),
        ]
        
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
        self.flap_sound.play()

    def gravity(self):
        self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        self.rect.y += int(self.velocity)

    def centerBird(self):
        self.velocity = 0
        self.rect.y = 300

