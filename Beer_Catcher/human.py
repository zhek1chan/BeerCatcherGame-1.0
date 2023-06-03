import pygame

class Human:
    def __init__(self, ac_game):
        self.screen = ac_game.screen
        self.settings = ac_game.settings
        self.screen_rect = ac_game.screen.get_rect()

        self.image = pygame.image.load('Images/chel.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.human_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.human_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)