import pygame
import random
from pygame.sprite import Sprite

class Beer(Sprite):
    def __init__(self, ac_game):
        super().__init__()
        self.screen = ac_game.screen
        self.settings = ac_game.settings
        self.screen_rect = ac_game.screen.get_rect()
        self.image = pygame.image.load('Images/beer.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(20, self.screen_rect.right-30)
        self.rect.y = 0
        self.y = float(self.rect.y)


    def update(self):
        self.y += self.settings.bottle_drop_speed
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)
