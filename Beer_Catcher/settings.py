import pygame as pg

class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.flag = pg.RESIZABLE
        self.bottles_allowed = 3
        self.bottle_limit = 3
        self.game_over = False
        self.apple_points = 1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.human_speed = 0.8
        self.bottle_drop_speed = 0.2
