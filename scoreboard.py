import pygame

class Scoreboard:
    def __init__(self, fbGame):
        self.screen = fbGame.screen
        self.screen_rect = self.screen.get_rect()

        self.score = 0
        self.pipe_passed = False


    def draw_text(self, x, y, string, col, window):
        font = pygame.font.Font('font/04B_19__.TTF', 60)
        text = font.render(string, True, col)
        textbox = text.get_rect()
        textbox.center = (x, y)
        window.blit(text, textbox)


    def checkPipes(self, bird, pipe_group):
        if len(pipe_group) > 0:
            if bird.rect.left > pipe_group.sprites()[0].rect.left\
                and bird.rect.right < pipe_group.sprites()[0].rect.right\
                and self.pipe_passed == False:
                self.pipe_passed = True
            if self.pipe_passed == True:
                if bird.rect.left > pipe_group.sprites()[0].rect.right:
                    self.score += 1
                    self.pipe_passed = False


    def resetScoreboard(self):
        self.score = 0