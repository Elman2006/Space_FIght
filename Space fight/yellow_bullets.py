# ================================ Open modules ======================================
import pygame
from pygame.sprite import Sprite


# =============================== yellow bullets class ===================================
class YellowBullets(Sprite):
    """ A class to creat and manage yellow bullets for yellow spaceship"""

    def __init__(
            self,
            ai_settings,
            screen,
            y_ship
    ):
        """ Creat the bullet object and ship current position"""
        super(
            YellowBullets,
            self
        ).__init__()
        # Objects
        self.screen = screen
        self.ai_settings = ai_settings

        # Creat a bullet rect at (0, 0) and then set current position.
        self.rect = pygame.Rect(0,
                                0,
                                ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.midleft = y_ship.rect.midleft

        # Store the bullet's position as a decimal value
        self.bullet_x = float(self.rect.x)

    def update_yellow_bullets(self):
        """ Move the bullet right to the screen """
        # Update the decimal position of the bullet
        self.rect.x -= self.ai_settings.bullet_speed

    def draw_yellow_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(
            self.screen,
            self.ai_settings.yellow_clr,
            self.rect
        )
