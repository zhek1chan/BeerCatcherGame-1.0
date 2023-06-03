import pygame.font

class Button:
    def __init__(self, ac_game, text):
        self.screen = ac_game.screen
        self.screen_rect = ac_game.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 153)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._show_text(text)

    def _show_text(self, text):
        self.text_image = self.font.render(text, True, \
        self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
