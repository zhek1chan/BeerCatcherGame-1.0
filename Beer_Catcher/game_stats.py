class GameStats:
    def __init__(self, ac_game):
        self.settings = ac_game.settings
        self.game_active = False
        self.reset_stats()
    def reset_stats(self):
        self.bottles_left = self.settings.bottle_limit
        self.score = 0
        self.level = 1