# ====================================== Importing modules ======================================
# -------------------------------------- Open modules -------------------------------------------
import pygame
from pygame.sprite import Sprite


# =============================== yellow bullets class ===================================
class RedBullets(Sprite):
    """ A class to creat and manage red bullets for red spaceship"""

    def __init__(
            self,
            ai_settings,
            screen,
            r_ship,
    ):
        """ Creat the bullet object and ship current position"""
        super(RedBullets, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Creat a bullet rect at (0, 0) and then set current position.
        self.rect = pygame.Rect(
            0,
            0,
            ai_settings.bullet_width,
            ai_settings.bullet_height
        )
        self.rect.midright = r_ship.rect.midright

        # Store the bullet's position as a decimal value
        self.bullet_x = float(self.rect.x)

    def update_red_bullets(self):
        """ Move the bullet right to the screen """
        # Update the decimal position of the bullet
        self.rect.x += self.ai_settings.bullet_speed

    def draw_red_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(
            self.screen,
            self.ai_settings.red_clr,
            self.rect
        )
