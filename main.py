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
        self.bg = Background(self)

        self.bird = Bird(self)
        

        self.pipe_group = pygame.sprite.Group()

        self.gameState = False


    def runGame(self):
        while True:
            self._checkEvents()

            if self.bird.flying:
                self.bird.gravity()
            if self.gameState:
                self.createNewPipes()

                
                for pipe in self.pipe_group:
                    pipe.movePipe()
                self.detectFall()
                self.detectCollision()

            self._updateScreen()
            self.clock.tick(60)

  
    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.bird.flying == False:
                self.gameState = True
                self.bird.flying = True
                self.bird.flap()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.gameState == True:
                self.bird.flap()

    def _updateScreen(self):
        # Draw background
        self.bg.blitBg()
        
        # Handling pipes
        self.pipe_group.draw(self.screen)
        self.pipe_group.update()
        
        # Handling bird
        self.bird.blitme()
        self.bird.updateFrame()

        pygame.display.flip() 


    def detectFall(self):
        if self.bird.rect.y >= 560:
            self.gameState = False
            self.bird.flying = False
            


    def detectCollision(self):
        if pygame.sprite.spritecollideany(self.bird, self.pipe_group) or self.bird.rect.top < 0:
            self.gameState = False


    def createNewPipes(self):
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


if __name__ == '__main__':
    fb = FlappyBird()
    fb.runGame()
