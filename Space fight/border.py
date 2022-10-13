# ================================== Open modules ==========================================
import pygame.rect


# =================================== Border class ==========================================
class Border:
    """ A class to creat a border center the screen"""

    def __init__(
            self,
            ai_settings,
            screen
    ):
        """ Initialize"""

        # screen
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Creat border
        self.border = pygame.Rect(
            self.screen_rect.width / 2 - self.ai_settings.border_width / 2,
            self.screen_rect.top,
            self.ai_settings.border_width,
            self.screen_rect.height
        )

    def draw_border(self):
        """ Draw the border to the screen"""
        pygame.draw.rect(
            self.screen,
            self.ai_settings.black_clr,
            self.border
        )
