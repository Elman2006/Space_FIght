# ======================================= Modules =====================================
# --------------------------------------- Open modules -------------------------------------
import pygame
from sys import exit


from red_bullets import RedBullets
from yellow_bullets import YellowBullets


# ====================================== Functions ==========================================
# -------------------------------------- Event functions -----------------------------------

def check_keyup_events(
        event,
        r_ship,
        y_ship
):
    """ function to manage keydown events"""

    # ****************************** Red spaceship movement ******************************
    if event.key == pygame.K_w:
        r_ship.move_up = False

    elif event.key == pygame.K_s:
        r_ship.move_down = False

    elif event.key == pygame.K_d:
        r_ship.move_right = False

    elif event.key == pygame.K_a:
        r_ship.move_left = False

    # ****************************** yellow spaceship movement ******************************
    if event.key == pygame.K_UP:
        y_ship.move_up = False

    elif event.key == pygame.K_DOWN:
        y_ship.move_down = False

    elif event.key == pygame.K_RIGHT:
        y_ship.move_right = False

    elif event.key == pygame.K_LEFT:
        y_ship.move_left = False


def check_keydown_events(
        ai_settings,
        event,
        r_bullets,
        r_ship,
        screen,
        stats,
        y_bullets,
        y_ship
):
    """ function to manage keydown events"""

    # Quit the game
    if event.key == pygame.K_ESCAPE:
        exit()

    # ****************************** Red spaceship movement ******************************
    if event.key == pygame.K_w:
        r_ship.move_up = True

    elif event.key == pygame.K_s:
        r_ship.move_down = True

    elif event.key == pygame.K_d:
        r_ship.move_right = True

    elif event.key == pygame.K_a:
        r_ship.move_left = True

    # ****************************** yellow spaceship movement ******************************
    if event.key == pygame.K_UP:
        y_ship.move_up = True

    elif event.key == pygame.K_DOWN:
        y_ship.move_down = True

    elif event.key == pygame.K_RIGHT:
        y_ship.move_right = True

    elif event.key == pygame.K_LEFT:
        y_ship.move_left = True

    # ***************************** Fire bullets ******************************************
    # Red spaceship bullets
    elif event.key == pygame.K_LCTRL and stats.game_active:
        fire_red_bullets(
            ai_settings,
            r_bullets,
            screen,
            r_ship,
        )
        ai_settings.shoot_sound.play()

    # Yellow spaceship bullets
    elif event.key == pygame.K_RCTRL and stats.game_active:
        fire_yellow_bullets(
            ai_settings,
            screen,
            y_bullets,
            y_ship,
        )

        ai_settings.shoot_sound.play()

    # ********************************* Start Game ****************************************
    elif event.key == pygame.K_p and not stats.game_active:
        update_stats(ai_settings)
        ai_settings.game_round += 1
        stats.game_active = True
        stats.reset_stats()


def check_events(
        ai_settings,
        play_btn,
        r_bullets,
        r_ship,
        screen,
        stats,
        y_bullets,
        y_ship
):
    """ A functions for checking all events in the game"""
    """ Respond to key presses and mouse events"""

    for event in pygame.event.get():
        # Exit from the game
        if event.type == pygame.QUIT:
            exit()

        # Check for mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_btn(
                mouse_x,
                mouse_y,
                play_btn,
                stats
            )

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                ai_settings,
                event,
                r_bullets,
                r_ship,
                screen,
                stats,
                y_bullets,
                y_ship
            )

        elif event.type == pygame.KEYUP:
            check_keyup_events(
                event,
                r_ship,
                y_ship
            )


# --------------------------------------- Button -------------------------------------------
def check_play_btn(
    mouse_x,
    mouse_y,
    play_btn,
    stats
):
    """ Start a new game when player click PLAY """
    btn_clicked = play_btn.btn_rect.collidepoint(mouse_x, mouse_y)

    if btn_clicked:

        # Hide the mouse courser
        pygame.mouse.set_visible(False)

        stats.game_active = True


def winner(
        ai_settings,
        sb,
        stats
):
    """ To prep the winner to screen"""
    if ai_settings.yellow_ship_health == 0:
        sb.red_win()
        stats.game_active = False

    elif ai_settings.red_ship_health == 0:
        sb.yellow_win()
        stats.game_active = False


def update_stats(
    ai_settings
):
    """Increase the winner states"""
    if ai_settings.yellow_ship_health == 0:
        ai_settings.red_round += 1

    elif ai_settings.red_ship_health == 0:
        ai_settings.yellow_round += 1


# --------------------------------------- Bullets -------------------------------------------
def fire_red_bullets(
        ai_settings,
        r_bullets,
        screen,
        r_ship,
):
    """ Fire a bullet if limit not reached yet. """
    # Create a new bullet and add it to the bullets group
    if len(r_bullets) < ai_settings.bullets_allowed:
        new_bullet = RedBullets(ai_settings, screen, r_ship)
        r_bullets.add(new_bullet)


def fire_yellow_bullets(
        ai_settings,
        screen,
        y_bullets,
        y_ship,
):
    """ Fire a bullet if limit not reached yet. """
    # Create a new bullet and add it to the bullets group
    if len(y_bullets) < ai_settings.bullets_allowed:
        new_bullet = YellowBullets(ai_settings, screen, y_ship)
        y_bullets.add(new_bullet)


def check_bullet_ship_collision(
    ai_settings,
    r_bullets,
    r_ship,
    y_bullets,
    y_ship
):
    """ TO check collision between each ship's bullets and other ship"""
    # Check for red-bullet and yellow-ship collision
    r_bullet_y_ship = pygame.sprite.spritecollide(y_ship, r_bullets, True)
    if r_bullet_y_ship:
        ai_settings.yellow_ship_health -= 1
        ai_settings.red_score += ai_settings.score
        ai_settings.hit_sound.play()

    # Check for yellow-bullet and red-ship collision
    y_bullet_r_ship = pygame.sprite.spritecollide(r_ship, y_bullets, True)
    if y_bullet_r_ship:
        ai_settings.red_ship_health -= 1
        ai_settings.yellow_score += ai_settings.score
        ai_settings.hit_sound.play()


def update_bullets(
        ai_settings,
        r_bullets,
        r_ship,
        y_bullets,
        y_ship
):
    """ Update position of bullets and get rid of old bullets"""
    # Update red-bullet position
    r_bullets.update()
    for bullet in r_bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width:
            r_bullets.remove(bullet)

    # Update yellow-bullet position
    y_bullets.update()
    for bullet in y_bullets.copy():
        if bullet.rect.right <= 0:
            y_bullets.remove(bullet)

    # Check for bullet-ship collision
    check_bullet_ship_collision(
        ai_settings,
        r_bullets,
        r_ship,
        y_bullets,
        y_ship
    )


# -------------------------------------- Update screen ------------------------------
def update_screen(
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
):
    """ A function to update screen and make most recent screen """
    # for screen
    pygame.display.set_caption(ai_settings.caption)
    pygame.display.set_icon(ai_settings.icon_img)
    screen.blit(ai_settings.bg_img, (0, 0))

    # Bullets update
    for r_bullet in r_bullets.sprites():
        r_bullet.update_red_bullets()
        r_bullet.draw_red_bullet()

    for y_bullet in y_bullets.sprites():
        y_bullet.update_yellow_bullets()
        y_bullet.draw_yellow_bullet()

    # Draw border
    border.draw_border()

    # Stats
    sb.prep_yellow_ship_health()
    sb.prep_red_ship_health()

    sb.red_score()
    sb.yellow_score()

    winner(ai_settings, sb, stats)

    sb.prep_round()
    sb.red_round()
    sb.yellow_round()

    # Update the spaceships
    r_ship.blit_red_ship()
    y_ship.blit_yellow_ship()

    # Draw the play button if the game is inactive
    if not stats.game_active and \
            not ai_settings.yellow_ship_health == 0 and \
            not ai_settings.red_ship_health == 0:
        btn.draw_btn()

    # Make the most recent screen
    pygame.display.flip()
