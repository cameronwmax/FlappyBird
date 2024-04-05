import sys

import pygame

from time import sleep

from settings import Settings
from bird import Bird
from background import Background
from gamePipes import Pipes


class FlappyBird:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self)
        self.bg = Background(self)
        self.pipe = Pipes(self)

        self.gameState = True


    def runGame(self):
        while True:
            self._checkEvents()
            
            if self.gameState:

                self.bird.movement()
                self.pipe.move()
                self.detectFall()
            
            self._updateScreen()
            self.clock.tick(60)
    
  
    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()


    def _updateScreen(self):
        # Redraw the screen during each pass through the loop
        self.bg.blitBg()
        
        self.bird.blitme()
        self.bird.updateFrame()

        self.pipe.createPipes()
        self.pipe.blitPipe()

        pygame.display.flip() 


    def detectFall(self):
        if self.bird.rect.y > 600:
            self.bird.fallingSpeed = 1
            self.bird.centerBird()
            self.pipe.clearPipes()
            sleep(0.5)

if __name__ == '__main__':
    fb = FlappyBird()
    fb.runGame()