"""
       ΒΙΒΛΙΟΘΗΚΕΣ:
"""
import pygame   # Για τη δημιουργία του παιχνιδιού

'''
    Draw MAIN GAME:

'''


# Δηλώνει τη συνάρτηση που δημιουργεί το ΠΑΡΑΘΥΡΟ του παιχνιδιού:
def draw_game(
        # Παράμετροι Συνάρτησης:
        wn, ground, ground_rect, background, background_rect, width,    # Window
        score, power_ups, power_up_seconds,                             # Texts
        pipe_group, spaceship_group, power_up_group, missing_pipe_group, alien_group, rocket_group,  # Groups
        power_up_text_disappear, seconds_text_disappear,                # Έλεγχος εμφάνισης κειμένων.
        font_score, font_seconds, font_power_ups, font_guide            # Fonts
):
    """
            BACKGROUND:
    """

    wn.blit(
        # Εμφανίζει το background στην οθόνη.
        background, (background_rect.x, background_rect.y)
    )
    wn.blit(
        # Εμφανίζει το ίδιο background ακριβώς απο δίπλα.
        background, (background_rect.x + width, background_rect.y)
    )
    '''
            GROUPS_part1:
    '''
    alien_group.draw(wn)  # Εμφανίζει τους εξωγήινους στην οθόνη.
    power_up_group.draw(wn)  # Εμφανίζει τα power ups στην οθόνη.
    pipe_group.draw(wn)  # Εμφανίζει τα εμπόδια στην οθόνη.
    '''
            GROUND:
    '''
    wn.blit(
        # Εμφανίζει το έδαφος στην οθόνη.
        ground, (ground_rect.x, ground_rect.y)
    )
    wn.blit(
        # Εμφανίζει το ίδιο έδαφος ακριβώς απο δίπλα.
        ground, (ground_rect.x + width, ground_rect.y)
    )
    '''
                GROUPS_part2:
    '''
    missing_pipe_group.draw(wn)     # Εμφανίζει το υπόλοιπο των εμποδίων στην οθόνη.
    rocket_group.draw(wn)           # Εμφανίζει τους πυραύλους στην οθόνη.
    spaceship_group.draw(wn)        # Εμφανίζει το διαστημόπλοιο στην οθόνη.

    '''
            FUNCTIONS:
    '''

    draw_score(  # Εμφανίζει το score στην οθόνη.
        # Παράμετροι Συνάρτησης:
        wn,             # Παράθυρο.
        score,          # Score.
        font_score      # Fonts
    )

    # Εμφανίζει τον μετρητή των power ups στην οθόνη:
    draw_power_ups(
        # Παράμετροι Συνάρτησης:
        wn,                         # Παράθυρο.
        power_ups,                  # Μετρητής των Power_ups
        font_power_ups              # Fonts
    )

    if not seconds_text_disappear:
        # Ελέγχει αν πρέπει να εμφανιστούν τα seconds.
        draw_seconds(
            # Παράμετροι Συνάρτησης:
            wn,                     # Παράθυρο.
            power_up_seconds,       # Χρόνος.
            font_seconds            # Fonts
        )
    if not power_up_text_disappear:
        # Ελέγχει αν πρέπει να εξηγήσει στο χρήστη πως να χρησιμοποιήσει τα power_ups του.
        draw_press_SPACE(
            # Παράμετροι Συνάρτησης:
            wn,                     # Παράθυρο.
            font_guide              # Fonts.
        )


def draw_score(
        # Παράμετροι Συνάρτησης:
        wn,                         # Παράθυρο.
        score,                      # Score.
        font_score                  # Fonts
):
    # Εμφανίζει το score στην οθόνη σε χρώμα άσπρο:
    score_text = font_score.render(str(score), True, (255, 255, 255))
    wn.blit(score_text, (450, 30))


def draw_seconds(
        # Παράμετροι Συνάρτησης:
        wn,                         # Παράθυρο.
        power_up_seconds,           # Χρόνος.
        font_seconds                # Fonts
):
    # Εμφανίζει τη διάρκεια power_ups σε χρώμα κόκκινο και άσπρο.
    seconds_text_a = font_seconds.render("seconds: ", True, (255, 0, 0))
    seconds_text_b = font_seconds.render(str(int(power_up_seconds / 1000)), True, (255, 255, 255))
    wn.blit(seconds_text_a, (800, 30))
    wn.blit(seconds_text_b, (950, 30))


def draw_press_SPACE(
        # Παράμετροι Συνάρτησης:
        wn,                         # Παράθυρο.
        font_guide                  # Fonts.
):
    # Εμφανίζει το κείμενο εξηγεί στο χρήστη πως να χρησιμοποιήσει τα power_ups του σε χρώμα άσπρο:
    press_space = font_guide.render("press \"SPACE\" to use your power ups", True, (255, 255, 255))
    wn.blit(press_space, (20, 400))


def draw_power_ups(
        # Παράμετροι Συνάρτησης:
        wn,                         # Παράθυρο.
        power_ups,                  # Μετρητής των Power_ups
        font_power_ups              # Fonts
):
    # Εμφανίζει τον μετρητή των power ups στην οθόνη σε χρώμα ροζ και άσπρο:
    power_ups_text_a = font_power_ups.render("POWER UPS: ", True, (255, 0, 255))
    power_ups_text_b = font_power_ups.render(str(power_ups), True, (255, 255, 255))
    wn.blit(power_ups_text_a, (20, 550))
    wn.blit(power_ups_text_b, (230, 550))


def draw_high_score(
        # Παράμετροι Συνάρτησης:
        wn,                         # Παράθυρο.
        High_score,                 # Highscore
        font_high_score             # Fonts
):
    # Εμφανίζει το highscore στο αρχικό menu.
    high_score_text = font_high_score.render("Highscore: " + str(High_score), True, (255, 255, 255))
    wn.blit(high_score_text, (800, 20))


'''
                Draw menu:
'''


def draw_menu(
        # Παράμετροι Συνάρτησης:
        wn, MENU_picture, title_group, High_score,                                              # Menu.
        font_high_score, font_current_skin,                                                     # Fonts.
        animation1_group, animation2_group, current_skin_group,                                 # Groups.
        exit_button_group, play_button_group, co_op_button_group, skins_button_group            # Buttons.
):
    wn.blit(
        # Εμφανίζει το background του menu.
        MENU_picture, (0, 0)
    )
    '''
            Εμφανίζονται τα groups:
    '''

    # Animations:
    animation1_group.draw(wn)                       # Το 1ο animation.
    animation2_group.draw(wn)                       # To 2o animation.

    # Menu:
    title_group.draw(wn)                            # Ο τίτλος του παιχνιδιού.
    current_skin_group.draw(wn)                     # Η εικόνα που δείχνει το skin που έχει επιλέξει ο χρήστης.

    # Buttons:
    exit_button_group.draw(wn)                      # Το κουμπί που κλείνει το παράθυρο.
    co_op_button_group.draw(wn)                     # Το κουμπί που ξεκινάει το co-op.
    skins_button_group.draw(wn)                     # Το κουμπί που ανοίγει το menu με τα skins.
    play_button_group.draw(wn)                      # Το κουμπί που ξεκινάει το κύριο παιχνίδι.

    # Functions:
    draw_high_score(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο.
        High_score, font_high_score                     # High score.
    )
    draw_current_skin(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο.
        font_current_skin                               # Fonts.
    )
    pygame.display.update()


'''

    Draw skins:

'''


def draw_current_skin(
        # Παράμετροι Συνάρτησης:
        wn,                                              # Παράθυρο
        font_current_skin                                # Fonts
):
    current_skin_text = font_current_skin.render("Current Skin:", True, (128, 128, 128))
    wn.blit(current_skin_text, (800, 430))


'''
Εμφανίζεται στην οθόνη ένα μήνυμα το οποίο ζητάει από το χρήστη να επιλέξει skin για το διαστημόπλοιο. 
'''


def draw_skin_TEXT(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο
        font_skins                                      # Fonts
):
    skin_text = font_skins.render("Choose a skin:", True, (255, 255, 255))
    wn.blit(skin_text, (150, 50))


def draw_skin_menu(
        # Παράμετροι Συνάρτησης:
        wn,                                                                                             # Παράθυρο.
        font_skins,                                                                                     # Fonts.
        skin_1_group, skin_2_group, skin_3_group, skin_4_group, skin_5_group, menu_button_group         # Buttons.
):

    """
                Menu:
    """
    wn.fill(
        # Γεμίζει το background με μαύρο χρώμα.
        (0, 0, 0)
    )
    menu_button_group.draw(wn)  # Εμφανίζει το κουμπί του επιστρέφει στο αρχικό menu.

    '''
                Εμφανίζει τις Επιλογές των skins:
    '''
    skin_1_group.draw(wn)
    skin_2_group.draw(wn)
    skin_3_group.draw(wn)
    skin_4_group.draw(wn)
    skin_5_group.draw(wn)

    '''
        Functions:
    '''
    # Εμφανίζεται στην οθόνη ένα μήνυμα το οποίο ζητάει από το χρήστη να επιλέξει skin για το διαστημόπλοιο:
    draw_skin_TEXT(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο
        font_skins                                      # Fonts
    )

    pygame.display.update()


'''
        DRAW CO-OP:
'''


def draw_co_op(
        # Παράμετροι Συνάρτησης:
        wn, player_1_background_group, player_2_background_group, border,           # Παράθυρο
        red_pipe_group, blue_pipe_group,                                            # Εμπόδια
        menu_button_group,                                                          # Buttons
        player_1_group, player_2_group                                              # Players
):
    # Εμφανίζει το background, τα εμπόδια και τον player 1 στην οθόνη:
    player_1_background_group.draw(wn)
    blue_pipe_group.draw(wn)
    player_1_group.draw(wn)

    # Εμφανίζει το background, τα εμπόδια και τον player 2 στην οθόνη:
    player_2_background_group.draw(wn)
    red_pipe_group.draw(wn)
    player_2_group.draw(wn)

    menu_button_group.draw(wn)  # Εμφανίζει το κουμπί του επιστρέφει στο αρχικό menu.

    wn.blit(
        # Διαχωρισμός των δύο backgrounds.
        border, (500.9, 0)
    )


def draw_player_1_guide(
        # Παράμετροι Συνάρτησης:
        wn,                                                 # Παράθυρο.
        font_players                                        # Fonts.
):
    # Δείχνει στον player 1 πως να χειριστεί τον χαρακτήρα του.
    player_1_guide = font_players.render("press \"W\" to jump", True, (255, 255, 255))
    wn.blit(player_1_guide, (50, 400))


def draw_player_2_guide(
        # Παράμετροι Συνάρτησης:
        wn,                                                 # Παράθυρο.
        font_players                                        # Fonts.
):
    # Δείχνει στον player 2 πως να χειριστεί τον χαρακτήρα του.
    player_2_guide = font_players.render("press \"UP\" to jump", True, (255, 255, 255))
    wn.blit(player_2_guide, (550, 400))


def draw_game_starts(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο.
        seconds,                                        # Χρόνος.
        font_score                                      # Fonts
):
    # Δείχνει πότε ξεκινάει το παιχνίδι.
    game_starts = font_score.render(str(3 - int(seconds / 1000)), True, (255, 255, 255))
    wn.blit(game_starts, (250, 200))
    wn.blit(game_starts, (750, 200))


'''
        RESULTS:
'''


def player_1_win(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο.
        font_CO_OP                                      # Fonts.
):
    # Εμφανίζει μήνυμα ότι νίκησε ο player 1.
    player_1_win_text = font_CO_OP.render("PLAYER 1 WON!!", True, (0, 0, 200))
    wn.blit(player_1_win_text, (100, 250))


def player_2_win(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο.
        font_CO_OP                                      # Fonts.
):
    # Εμφανίζει μήνυμα ότι νίκησε ο player 2.
    player_2_win_text = font_CO_OP.render("PLAYER 2 WON!!", True, (150, 0, 0))
    wn.blit(player_2_win_text, (100, 250))


def Draw(
        # Παράμετροι Συνάρτησης:
        wn,                                             # Παράθυρο.
        font_CO_OP                                      # Fonts.
):
    # Εμφανίζει μήνυμα ότι βγήκε ισοπαλία.
    player_2_win_text = font_CO_OP.render("DRAW!!", True, (128, 128, 128))
    wn.blit(player_2_win_text, (300, 250))
