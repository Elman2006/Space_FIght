class GameStats:
    """ Track statistics for alien invasion"""

    def __init__(
            self,
            ai_settings,
            r_ship,
            screen,
            y_ship
    ):
        """ Initialize statistics"""
        self.ai_settings = ai_settings
        self.r_ship = r_ship
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.y_ship = y_ship

        # Start Alien invasion in inactive state
        self.game_active = False

    def reset_stats(self):
        """ initialize statistics that can change during the game"""
        self.ai_settings.red_ship_health = 10
        self.ai_settings.yellow_ship_health = 10

        self.r_ship.rect.midleft = self.screen_rect.midleft
        self.y_ship.rect.midright = self.screen_rect.midright
