import time

import pygame as pg
import sys
from beer import Beer
from settings import Settings
from human import Human
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

surf = pg.Surface((200, 150))
surf.fill((255, 255, 255))
class BeerCatcher:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width,
        self.settings.screen_height), self.settings.flag)
        pg.display.set_caption('Любитель Пива v1.0')
        self.background = pg.image.load('Images/bar.png')
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.human = Human(self)
        self.beer_bottles = pg.sprite.Group()
        self.play_button = Button(self, "Играть")
        self.screen_rect = self.screen.get_rect()

       
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.human.update()
                self._drop_apples()
                self.beer_bottles.update()
                self._check_beer_bottles_bottom()
                self._update_beer_bottles()
            self._update_screen()

    def _update_beer_bottles(self):
        for beer in self.beer_bottles.copy():
            if beer.rect.bottom >= self.screen_rect.bottom:
                self.beer_bottles.remove(beer)
        self._check_human_and_beer_collisions()


    def _check_human_and_beer_collisions(self):
        collisions = pg.sprite.spritecollide(self.human, self.beer_bottles, True)
        if collisions:
            self.stats.score += self.settings.apple_points
            if self.stats.score == 10:
                self.background = pg.image.load('Images/win.png')

            self.sb.prep_score()


    def _check_beer_bottles_bottom(self):
        screen_rect = self.screen.get_rect()
        for apple in self.beer_bottles.sprites():
            if apple.rect.bottom >= screen_rect.bottom:
                self._apple_hit()
                break


    def _apple_hit(self):
        if self.stats.bottles_left > 0:
            self.stats.bottles_left -= 1

            self.sb.prep_beer_bottles()
        else:

            self.stats.game_active = False


        
    def _drop_apples(self):
        if self.stats.score <= 7:
            if len(self.beer_bottles) == 0:
                    new_apple = Beer(self)
                    self.beer_bottles.add(new_apple)
            if len(self.beer_bottles) == 1:
                for apple in self.beer_bottles.sprites():
                    if apple.rect.bottom > 300:
                        new_apple = Beer(self)
                        self.beer_bottles.add(new_apple)
            if len(self.beer_bottles) == 2:
                for apple in self.beer_bottles.sprites():
                    if apple.rect.bottom > 600:
                        new_apple = Beer(self)
                        self.beer_bottles.add(new_apple)
            if len(self.beer_bottles) == 3:
                for apple in self.beer_bottles.sprites():
                    if apple.rect.bottom > 900:
                        new_apple = Beer(self)
                        self.beer_bottles.add(new_apple)


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_beer_bottles()
            self.beer_bottles.empty()
        
        
    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            
                
    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.human.moving_right = True
        elif event.key == pg.K_LEFT:
            self.human.moving_left = True
        elif event.key == pg.K_SPACE:
            self._drop_apples()

    
    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.human.moving_right = False
        elif event.key == pg.K_LEFT:
            self.human.moving_left = False


    def _update_screen(self):
        self.screen.blit(self.background, (0,0))
        self.human.blitme()

        for apple in self.beer_bottles.sprites():
            apple.blitme()

        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()

        pg.display.flip()


if __name__ == '__main__':
    ec = BeerCatcher()
    ec.run_game()
