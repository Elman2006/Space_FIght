# =================================== Modules ======================================
# --------------------------------- Open modules ----------------------------------
import pygame
from pygame.sprite import Group
# --------------------------------- my modules -------------------------------------
from settings import Settings
import game_functions as gf
from red_ship import RedShip
from yellow_ship import YellowShip
from border import Border
from score_board import ScoreBoard
from game_states import GameStats
from button import Button


# ======================================== Main function ===============================
def run_game():
    """ The main function to run the game"""

    # Initialise
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    border = Border(ai_settings, screen)
    r_ship = RedShip(ai_settings, border, screen)
    y_ship = YellowShip(ai_settings, border, screen)
    r_bullets = Group()
    y_bullets = Group()
    sb = ScoreBoard(
        ai_settings,
        border,
        screen
    )
    stats = GameStats(ai_settings, r_ship, screen, y_ship)
    btn = Button(ai_settings, screen)
    clock = pygame.time.Clock()

    while True:
        " An infinity loop for update the screen"
        # Set fps
        clock.tick(ai_settings.fps)

        # Event function
        gf.check_events(
            ai_settings,
            btn,
            r_bullets,
            r_ship,
            screen,
            stats,
            y_bullets,
            y_ship
        )

        if stats.game_active:
            # Update spaceships
            y_ship.update_yellow_ship()
            r_ship.update_red_ship()
            gf.update_bullets(
                ai_settings,
                r_bullets,
                r_ship,
                y_bullets,
                y_ship
            )

        # Update screen
        gf.update_screen(
            ai_settings,
            border,
            btn,
            r_bullets,
            r_ship,
            sb,
            screen,
            stats,
            y_bullets,
            y_ship
        )


# --------------------------------------- Call function -------------------------------------------
run_game()
