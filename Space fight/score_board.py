# ================================== modules =======================================
# ------------------------------- Open modules -------------------------------------


# ================================== Score class ==============================================
class ScoreBoard:
    """ A class to report scoring information """

    def __init__(
            self,
            ai_settings,
            border,
            screen
    ):
        """ Initialize score keeping information"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.border = border
        self.ai_settings = ai_settings

        # Prepare the initial score images
        self.prep_red_ship_health()
        self.prep_yellow_ship_health()

    # ****************************************** Prep the health ******************************************
    def prep_red_ship_health(self):
        """ Turn the red spaceship health into a rendered image"""
        self.r_health_img = self.ai_settings.game_font.render(
            "Health: {}".format(self.ai_settings.red_ship_health),
            True,
            self.ai_settings.white_clr
        )

        # Display the red spaceship health at the bottom-left of the screen
        self.r_health_rect = self.r_health_img.get_rect()
        self.r_health_rect.left = self.screen_rect.left + 20
        self.r_health_rect.top = self.screen_rect.top + 10

        self.screen.blit(
            self.r_health_img,
            self.r_health_rect
        )

    def prep_yellow_ship_health(self):
        """ Turn the yellow spaceship health into a rendered image"""
        self.y_health_img = self.ai_settings.game_font.render(
            f"Health: {self.ai_settings.yellow_ship_health}",
            True,
            self.ai_settings.white_clr
        )

        # Display the red spaceship health at the bottom-left of the screen
        self.y_health_rect = self.y_health_img.get_rect()
        self.y_health_rect.right = self.screen_rect.right - 20
        self.y_health_rect.top = self.screen_rect.top + 10

        self.screen.blit(
            self.y_health_img,
            self.y_health_rect
        )

    # ****************************************** prep the round ******************************************
    def prep_round(self):
        """ A class to prep the round (level) of game"""
        self.round_img = self.ai_settings.game_font.render(
            f"Round: {self.ai_settings.game_round}",
            True,
            self.ai_settings.white_clr
        )

        # Display the round of the game in the top-center of the screen
        self.round_rect = self.round_img.get_rect()
        self.round_rect.centerx = self.screen_rect.centerx
        self.round_rect.top = self.screen_rect.top + 10

        # Display the round
        self.screen.blit(
            self.round_img,
            self.round_rect
        )

    # ****************************************** Score ******************************************
    def red_score(self):
        """ Turn the red spaceship score """
        self.red_score_img = self.ai_settings.game_font.render(
            "Score: {}".format(self.ai_settings.red_score),
            True,
            self.ai_settings.white_clr
        )

        # Display and set the position of the red spaceship-score in the left-bottom
        self.red_score_rect = self.red_score_img.get_rect()
        self.red_score_rect.bottom = self.screen_rect.bottom - 20
        self.red_score_rect.left = self.screen_rect.left + self.ai_settings.ship_space_limit

        # Draw the red spaceship in the screen
        self.screen.blit(
            self.red_score_img,
            self.red_score_rect
        )

    def yellow_score(self):
        """ Turn the yellow spaceship score """
        self.yellow_score_img = self.ai_settings.game_font.render(
            "Score: {}".format(self.ai_settings.yellow_score),
            True,
            self.ai_settings.white_clr
        )

        # Display and set the position of the yellow spaceship score in right-bottom
        self.yellow_score_rect = self.yellow_score_img.get_rect()
        self.yellow_score_rect.bottom = self.screen_rect.bottom - 20
        self.yellow_score_rect.right = self.screen_rect.right - self.ai_settings.ship_space_limit

        # Draw the yellow spaceship score to the screen
        self.screen.blit(
            self.yellow_score_img,
            self.yellow_score_rect
        )

    # ****************************************** Winning rounds ******************************************
    def red_round(self):
        """ Turn how many rounds that red spaceship win"""
        self.round_red = self.ai_settings.game_font.render(
            f"Round win: {self.ai_settings.red_round}",
            True,
            self.ai_settings.white_clr
        )

        # Display and set the position of the red spaceship round win
        self.round_red_rect = self.round_red.get_rect()
        self.round_red_rect.left = self.ai_settings.ship_space_limit
        self.round_red_rect.bottom = self.screen_rect.bottom - 70

        # Draw the red spaceship round level to the screen
        self.screen.blit(
            self.round_red,
            self.round_red_rect
        )

    def yellow_round(self):
        """ Turn how many rounds that yellow spaceship win"""
        self.round_yellow = self.ai_settings.game_font.render(
            f"Round win: {self.ai_settings.yellow_round}",
            True,
            self.ai_settings.white_clr
        )

        # Display and set the position of the yellow spaceship round win
        self.round_yellow_rect = self.round_yellow.get_rect()
        self.round_yellow_rect.bottom = self.screen_rect.bottom - 70
        self.round_yellow_rect.right = self.screen_rect.right - self.ai_settings.ship_space_limit

        # Draw the yellow spaceship round level to the screen
        self.screen.blit(
            self.round_yellow,
            self.round_yellow_rect
        )

    # ****************************************** Winner ******************************************
    def red_win(self):
        """ Turn the red spaceship win massage"""
        self.r_win_img = self.ai_settings.game_font.render(
            "  Red win!!!  ",
            True,
            self.ai_settings.white_clr,
            self.ai_settings.red_clr
        )

        # Display the red spaceship health at the bottom-left of the screen
        self.r_win_rect = self.r_win_img.get_rect()
        self.r_win_rect.center = self.screen_rect.center

        self.screen.blit(
            self.r_win_img,
            self.r_win_rect
        )

    def yellow_win(self):
        """ Turn the red spaceship win massage"""
        self.y_win_img = self.ai_settings.game_font.render(
            "  Yellow win!!!  ",
            True,
            self.ai_settings.white_clr,
            self.ai_settings.yellow_clr
        )

        # Display the red spaceship health at the bottom-left of the screen
        self.y_win_rect = self.y_win_img.get_rect()
        self.y_win_rect.center = self.screen_rect.center

        self.screen.blit(
            self.y_win_img,
            self.y_win_rect
        )
