import pygame
import random

class Pipes:
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()

        self.img = pygame.image.load("images\pipe.png")
        self.pipes = []
        self.rects = []
        self.sizes = [
            [225, 225],
            [250, 200], [200, 250],
            [275, 175], [175, 275],
            [150, 300], [300, 150],
            [125, 325], [325, 125],
            [100, 350], [350, 100],
            [75, 375], [375, 75]
        ]        
        # Refactor using a for loop?
        # Test

        
    def createPipes(self):
        if len(self.pipes) != 2:
            sizes = random.choice(self.sizes)
            for _ in range(2):
                self.pipes.append(pygame.transform.scale(self.img, (100, sizes[_])))

            for pipe in self.pipes:
                self.rects.append(pipe.get_rect())

            self.rects[0].bottomright = (500, 600)
            self.rects[1].topright = (500, 0)

    def blitPipe(self):
        for i in range(2):
            self.screen.blit(self.pipes[i], self.rects[i])

    def move(self):
        for rect in self.rects:
            rect.x -= 3
            if rect.x < -100:
                self.clearPipes()

    def clearPipes(self):
        self.pipes.clear()
        self.rects.clear()