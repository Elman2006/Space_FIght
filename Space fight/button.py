# ========================================= Open Modules  ========================================
import pygame.font


# ========================================= Button class ======================================
class Button:

    def __init__(
            self,
            ai_settings,
            screen
    ):
        """Initialize button attributes """
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Build the button's rect object and center it.
        self.btn_rect = pygame.Rect(
            0,
            0,
            self.ai_settings.btn_width,
            self.ai_settings.btn_height
        )
        self.btn_rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.prep_msg()

    def prep_msg(self):
        """ Turn msg into a rendered image and center text on the button"""
        self.msg_img = self.ai_settings.game_font.render(
            self.ai_settings.btn_msg,
            True,
            self.ai_settings.dark_blue_clr,
        )
        self.msg_rect = self.msg_img.get_rect()
        self.msg_rect.center = self.btn_rect.center

    def draw_btn(self):
        """ Draw bland button and then draw massage"""
        self.screen.fill(self.ai_settings.light_blue_clr, self.btn_rect)
        self.screen.blit(self.msg_img, self.msg_rect)
