import sys

import pygame
import random
import time

from background import Background
from bird import Bird
from gamePipes import Pipes
from ground import Ground
from restartImage import Restart
from scoreboard import Scoreboard
from settings import Settings


class FlappyBird:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.hit_sound = pygame.mixer.Sound("sounds\hit.wav")
        self.die_sound = pygame.mixer.Sound("sounds\die.wav")
         
        # Game variable
        self.pipe_frequency = 1500
        self.gameState = False
        self.game_over = False
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
        
        self.scoreboard = Scoreboard(self)
        self.resart = Restart(self)

        self.ground = Ground(self)
        self.ground_top = 490


    def runGame(self):
        while True:
            self._checkEvents()

            if self.bird.flying:
                self.bird.gravity()
            if self.gameState:
                self.createNewPipes()

                # Move pipes
                for pipe in self.pipe_group:
                    pipe.movePipe()

                self.detectCollision()
                self.scoreboard.checkPipes(self.bird, self.pipe_group)

            if self.bird.rect.y >= self.ground_top:
                self.bird.flying = False


            self._updateScreen()

            self.clock.tick(60)

  
    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.bird.flying == False and self.game_over == False:
                self.gameState = True
                self.bird.flying = True
                self.ground.speed = 3
            elif event.type == pygame.MOUSEBUTTONDOWN and self.gameState == True and self.game_over == False:
                self.bird.flap()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.gameState == False and self.game_over == True and self.bird.flying == False:
                self.resetGame()


    def _updateScreen(self):
        # Draw background
        self.bg.blitBg()
        
        # Handling pipes
        self.pipe_group.draw(self.screen)
        self.pipe_group.update()
        

        self.ground.blitGround()
        
        # Handling bird
        self.bird.blitme()
        self.bird.updateFrame()

        if self.game_over == True and self.bird.flying == False:
            self.resart.blitRestart()

        self.drawText(self.scoreboard.score)

        pygame.display.flip() 
            

    def detectCollision(self):
        if pygame.sprite.spritecollideany(self.bird, self.pipe_group) or self.bird.rect.top < 0:
            self.gameover()
            self.die_sound.play()
        elif self.bird.rect.y >= self.ground_top:
            self.gameover()
            self.bird.flying = False


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


    def gameover(self):
        self.hit_sound.play()
        self.ground.speed = 0
        self.gameState = False
        self.game_over = True

    
    def resetGame(self):
        self.game_over = False
        self.pipe_group.empty()
        self.bird.centerBird()
        self.scoreboard.resetScoreboard()


    def drawText(self, score):
        x = 200
        y = 50
        self.scoreboard.draw_text(x - 2, y - 2, f"{score}", "black", self.screen)
        self.scoreboard.draw_text(x + 2, y - 2, f"{score}", "black", self.screen)
        self.scoreboard.draw_text(x - 2, y + 2, f"{score}", "black", self.screen)
        self.scoreboard.draw_text(x + 2, y + 2, f"{score}", "black", self.screen)

        self.scoreboard.draw_text(x, y, f"{score}", "white", self.screen)


if __name__ == '__main__':
    fb = FlappyBird()
    fb.runGame()
