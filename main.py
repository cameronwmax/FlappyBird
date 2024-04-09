import sys

import pygame
import random

from time import sleep

from settings import Settings
from bird import Bird
from background import Background
from gamePipes import Pipes




class FlappyBird:
    def __init__(self):
        pygame.init()

        self.pipe_frequency = 1500
        self.last_pipe = pygame.time.get_ticks() - self.pipe_frequency

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self)
        self.bg = Background(self)

        self.pipe_group = pygame.sprite.Group()

        # gap = random.randint(50, 100)
        # btm_pipe = Pipes(self, 400, (self.settings.screen_height / 2), 1, gap)
        # self.pipe_group.add(btm_pipe) 
        # top_pipe = Pipes(self, 400, (self.settings.screen_height / 2), -1, gap)
        # self.pipe_group.add(top_pipe)

        self.gameState = True


    def runGame(self):
        while self.gameState:
            self._checkEvents()

            # Create new pipes
            time_now = pygame.time.get_ticks()
            if time_now - self.last_pipe > self.pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipes(
                    self, 
                    500, (self.settings.screen_height / 2) + pipe_height, 
                    1
                )
                top_pipe = Pipes(
                    self, 
                    500, (self.settings.screen_height / 2) + pipe_height,
                    -1
                )
                self.pipe_group.add(btm_pipe) 
                self.pipe_group.add(top_pipe)
                self.last_pipe = time_now

            self.bird.movement()
            for pipe in self.pipe_group:
                pipe.movePipe()
            self.detectFall()

            
            self._updateScreen()
            self.clock.tick(60)
    
  
    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if event.key == pygame.MOUSEBUTTONUP:
                self.bird.flap()


    def _updateScreen(self):
        # Redraw the screen during each pass through the loop
        self.bg.blitBg()
        
        self.bird.blitme()
        self.bird.updateFrame()

        self.pipe_group.draw(self.screen)
        self.pipe_group.update()



        pygame.display.flip() 


    def detectFall(self):
        if self.bird.rect.y > 600:
            self.bird.fallingSpeed = 1
            self.bird.centerBird()
            sleep(0.5)

if __name__ == '__main__':
    fb = FlappyBird()
    fb.runGame()
