"""
       ΒΙΒΛΙΟΘΗΚΕΣ:
"""
from CLASSES import *
from functions import *
'''
       ΑΡΧΙΚΟΠΟΙΗΣΗ ΠΑΙΧΝΙΔΙΟΥ:

'''

pygame.init()  # Αρχικοποίηση του pygame

'''                                
                                    HIGHSCORE:
 Κάθε φορά που εκτελείται το πρόγραμμα, διαβάζεται το αρχείο highscore.txt 
 και μετατρέπει τον αριθμό, που αρχικά είναι σε μορφή σύμβολο-σειράς, 
 σε μορφή ακεραίου και τον αποθηκεύει στη μεταβλητή high_score.
'''
with open('files/highscore.txt', 'r') as f:
    High_score = int(f.read())

'''   
       Αρχικοποίηση Μεταβλητών: 
'''

border = pygame.transform.scale(pygame.image.load('images/border.gif'), (5, 603))

'''
________________________________________________________________________________________________________________________
                                                    FONTS:
                        Δηλώνουμε Τι Είδους Font θα Χρησιμοποιήσουμε Για:
'''

# Το CO-OP:
font_CO_OP = pygame.font.Font('freesansbold.ttf', 102)

# Το score:
font_score = pygame.font.Font('freesansbold.ttf', 82)

# Τα skins:
font_skins = pygame.font.Font('freesansbold.ttf', 82)

# Τα power_ups:
font_power_ups = pygame.font.Font('freesansbold.ttf', 32)

# Το μήνυμα που εξηγεί στον χρήστη πως να χρησιμοποιήσει τα power ups του:
font_guide = pygame.font.Font('freesansbold.ttf', 32)

# Τον χρόνο που κρατάνε τα power_ups:
font_seconds = pygame.font.Font('freesansbold.ttf', 32)

# Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για τους παίκτες:
font_players = pygame.font.Font('freesansbold.ttf', 32)

# Τρέχον skin:
font_current_skin = pygame.font.Font('freesansbold.ttf', 25)

# Το highscore
font_high_score = pygame.font.Font('freesansbold.ttf', 22)

# Window:
width, height = 1000, 603                           # Πλάτος και ύψος του παραθύρου.
wn = pygame.display.set_mode((width, height))       # Δημιουργία του παραθύρου.
pygame.display.set_caption("Flappy Spaceship")      # Τίτλος παραθύρου Flappy spaceship.

# Φορτώνει την εικόνα του menu:
MENU_picture = pygame.transform.scale(pygame.image.load('images/MENU.jpg'), (1000, 603))
# Η εικόνα που δείχνει πιο skin έχει διαλέξει ο χρήστης:
current_skin_group = pygame.sprite.Group()
Current_skin = current_skin(900, 520)
current_skin_group.add(Current_skin)

# Αρχικοποιεί τη μεταβλητή που ελέγχει αν πρέπει να ξανά-ξεκινήσει το κύριο παιχνίδι:
retry_button_clicked = False

# Αν ο παίκτης δεν επιλέξει κάποιο skin τότε αυτόματα το διαστημόπλοιο παίρνει το πρώτο skin:
current_sprite = 0

"""
________________________________________________________________________________________________________________________
                                    DEFINE BUTTONS:
________________________________________________________________________________________________________________________
"""

# Δήλωση της κλάσης του κουμπιού που ξεκινάει το κύριο παιχνίδι.
play_button_group = pygame.sprite.Group()
Play_button = play_button(498, 350)
play_button_group.add(Play_button)

# Δήλωση της κλάσης του κουμπιού που επιστρέφει στο αρχικό menu
menu_button_group = pygame.sprite.Group()
Menu_button = menu_button(80, 30)
menu_button_group.add(Menu_button)

# Δήλωση της κλάσης του κουμπιού που κλείνει το παράθυρο.
exit_button_group = pygame.sprite.Group()
Exit_button = exit_button(70, 550)
exit_button_group.add(Exit_button)

# Δήλωση της κλάσης του τίτλου του παιχνιδιού
title_group = pygame.sprite.Group()
Title = title(498, 150)
title_group.add(Title)

# Δήλωση της κλάσης του κουμπιού που ξανά-ξεκινάει το παιχνίδι
retry_button_group = pygame.sprite.Group()
Retry_button = retry_button(880, 560)
retry_button_group.add(Retry_button)

# Δήλωση της κλάσης του κουμπιού που πηγαίνει στο menu με τα skins
skins_button_group = pygame.sprite.Group()
Skins_button = skins_button(494, 420)
skins_button_group.add(Skins_button)

'''
 Δηλώνονται όλες οι κλάσεις με τις επιλογές των skins που δίνονται στον χρήστη:
'''

# Skin 1:
skin_1_group = pygame.sprite.Group()
Skin_1 = skin_1(200, 250)
skin_1_group.add(Skin_1)

# Skin 2:
skin_2_group = pygame.sprite.Group()
Skin_2 = skin_2(350, 250)
skin_2_group.add(Skin_2)

# Skin 3:
skin_3_group = pygame.sprite.Group()
Skin_3 = skin_3(500, 250)
skin_3_group.add(Skin_3)

# Skin 4:
skin_4_group = pygame.sprite.Group()
Skin_4 = skin_4(650, 250)
skin_4_group.add(Skin_4)

# Skin 5:
skin_5_group = pygame.sprite.Group()
Skin_5 = skin_5(800, 250)
skin_5_group.add(Skin_5)
'''
            CO-OP:
'''

# Co-op button:
co_op_button_group = pygame.sprite.Group()
CO_OP_button = co_op_button(496, 490)
co_op_button_group.add(CO_OP_button)

# Player 1 background:
player_1_background_group = pygame.sprite.Group()
background_p1 = player_1_background(width / 4, height / 2)
player_1_background_group.add(background_p1)

# Player 2 background:
player_2_background_group = pygame.sprite.Group()
background_p2 = player_2_background(750, height / 2)
player_2_background_group.add(background_p2)

# Αρχικοποιεί τη μεταβλητή που ελέγχει αν πρέπει να ξανά-ξεκινήσει το CO-OP.
retry_COOP_clicked = False
'''
________________________________________________________________________________________________________________________
'''

'''
________________________________________________________________________________________________________________________
                                            Μεταβλητές Κεντρικής Loop:
________________________________________________________________________________________________________________________
'''
MAIN_LOOP = True
menu = True
skins = True
Game = True
CO_OP = True
