# ================================ Modules =================================
import pygame


# ============================= Red spaceship class ===============================
class RedShip:
    """ A class to creat and manage red spaceship"""

    def __init__(
            self,
            ai_settings,
            border,
            screen
    ):
        """ Initialise ship"""
        # Objects
        self.ai_settings = ai_settings
        self.border = border
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load red spaceship image and get its rect
        self.image = pygame.transform.scale(
            pygame.transform.rotate(
                pygame.image.load("assets/img/spaceship_red.png"), 90
            ), (self.ai_settings.ship_width, self.ai_settings.ship_height)
        )
        self.rect = self.image.get_rect()

        # Set the spaceships position
        self.rect.midleft = self.screen_rect.midleft

        # Red spaceship movement
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

    def update_red_ship(self):
        """ to manage position of yellow spaceship with keyboard"""
        if self.move_up and self.rect.top > self.ai_settings.ship_space_limit:
            self.rect.y -= self.ai_settings.ship_speed

        elif self.move_down and self.rect.bottom < self.screen_rect.bottom - self.ai_settings.ship_space_limit:
            self.rect.y += self.ai_settings.ship_speed

        elif self.move_right and self.rect.right < self.border.border.left - self.ai_settings.ship_space_limit:
            self.rect.x += self.ai_settings.ship_speed

        elif self.move_left and self.rect.left > self.screen_rect.left + self.ai_settings.ship_space_limit:
            self.rect.x -= self.ai_settings.ship_speed

    def blit_red_ship(self):
        """ To show the red spaceship in the screen"""
        self.screen.blit(
            self.image,
            self.rect
        )
