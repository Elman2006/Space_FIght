# ================================== Open modules ============================
import pygame


# =================================== main class ==============================
class Settings:
    """ A class to sort all settings in game"""

    def __init__(self):
        """ Initialize the game settings"""

        # Colors
        self.black_clr = (0, 0, 0)
        self.white_clr = (255, 255, 255)
        self.yellow_clr = (255, 255, 0)
        self.red_clr = (255, 0, 0)
        self.light_blue_clr = (28, 214, 206)
        self.dark_blue_clr = (41, 52, 98)

        # Files
        self.game_font = pygame.font.Font("assets/Font/Flappy.TTF", 40)
        self.icon_img = pygame.image.load("assets/img/logo-2.png")
        self.bg_img = pygame.image.load("assets/img/planet.jpg")
        self.shoot_sound = pygame.mixer.Sound("assets/sound/Gun+Silencer.mp3")
        self.hit_sound = pygame.mixer.Sound("assets/sound/Grenade+1.mp3")

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 620
        self.caption = "Space fight"
        self.fps = 90
        self.game_round = 1
        self.score = 15

        # Spaceship settings
        self.ship_speed = 8
        self.ship_space_limit = 5
        self.red_ship_health = 10
        self.yellow_ship_health = 10
        self.red_score = 0
        self.yellow_score = 0
        self.red_round = 0
        self.yellow_round = 0
        self.ship_width = 60
        self.ship_height = 50

        # Border
        self.border_width = 10

        # Bullets
        self.bullet_width = 20
        self.bullet_height = 4
        self.bullet_speed = 8
        self.bullets_allowed = 4

        # Button
        self.btn_width = 160
        self.btn_height = 90
        self.btn_msg = "Play"
