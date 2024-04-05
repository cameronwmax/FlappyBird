import pygame
import random

class Pipes:
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = fbGame.screen.get_rect()

        self.img = pygame.image.load("images\pipe.png")
        self.pipes = []
        self.rects = []       
        self.sizes = []
        
        left = 75
        right = 375
        increment = 25
        while left != 375 and right != 75:
            self.sizes.append([left, right])
            left += increment
            right -= increment

        
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