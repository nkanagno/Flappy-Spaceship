"""
       ΒΙΒΛΙΟΘΗΚΕΣ:
"""
import random               # Για την παραγωγή τυχαίων αριθμών.
import time                 # Για να παγώνει το πρόγραμμα.
import pygame               # Για τη δημιουργία του παιχνιδιού.
from pygame import mixer    # Για τη χρήση μουσικής και ηχητικών εφέ

"""
________________________________________________________________________________________________________________________
                                                ΕΜΠΟΔΙΑ:
________________________________________________________________________________________________________________________
"""
'''
        Κλάση Εμποδίων Κύριου Παιχνιδιού:
'''


class pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pipe_gap = random.randint(120, 200)  # Το κενό που υπάρχει ανάμεσα στο πάνω και στο κάτω μέρος του εμποδίου.
        pygame.sprite.Sprite.__init__(self)  # Αρχικοποίηση των sprites μέσα στην κλάση
        self.image = pygame.transform.scale(pygame.image.load('images/pipes.gif'), (89, 286))  # Φόρτωση εμποδίων
        self.rect = self.image.get_rect()  # Δήλωση εμποδίων σε μορφή rectangle
        if position == 1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι 1
            self.image = pygame.transform.flip(self.image, False, True)  # τότε δηλώνεται το πάνω μέρος του εμποδίου
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]  # και οι συντεταγμένες του
        if position == -1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι -1
            '''
                Τότε δηλώνεται το κάτω μέρος του εμποδίου,
                καθώς και οι συντεταγμένες του:
            '''
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    # ΌΣΟ καλείται η συνάρτηση update τότε το κάθε εμπόδιο προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου
    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()


'''
        Κλάση Του Υπόλοιπου Των Εμποδίων Κύριου Παιχνιδιού:        
'''


class restpipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας του υπολοίπου του εμποδίου και ως rectangle
        self.image = pygame.transform.scale(pygame.image.load('images/missing_pipe.gif'), (89, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]  # βρίσκεται στη βάση του κάθε Εμποδίου

    # ΌΣΟ καλείται τότε το κάθε υπόλοιπο εμπόδιο προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()


'''
        Κλάση Εμποδίων Tου Player 1:
                   (CO-OP)
'''


class blue_pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pipe_gap = random.randint(120, 200)  # Το κενό που υπάρχει ανάμεσα στο πάνω και στο κάτω μέρος του εμποδίου.
        pygame.sprite.Sprite.__init__(self)  # Αρχικοποίηση των sprites μέσα στην κλάση
        self.image = pygame.transform.scale(pygame.image.load('images/pipes.gif'), (69, 406))  # Φόρτωση εμποδίων
        self.rect = self.image.get_rect()  # Δήλωση εμποδίων σε μορφή rectangle
        if position == 1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι 1
            self.image = pygame.transform.flip(self.image, False, True)  # τότε δηλώνεται το πάνω μέρος του εμποδίου
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]  # και οι συντεταγμένες του
        if position == -1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι -1
            '''
                Τότε δηλώνεται το κάτω μέρος του εμποδίου,
                καθώς και οι συντεταγμένες του:
            '''
            self.rect.topleft = [x, y + int(pipe_gap / 2)]
    ''' 
    ΌΣΟ καλείται η συνάρτηση update τότε το κάθε εμπόδιο προχωράει προς τα αριστερά 
    μέχρι να βγει εκτός της αριστερής μεριάς του παραθύρου.
    '''
    def update(self, speed):
        self.rect.x -= speed
        if self.rect.left < 0:
            self.kill()


'''
        Κλάση Εμποδίων Tου Player 2:
                   (CO-OP)
'''


class red_pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pipe_gap = random.randint(120, 200)  # Το κενό που υπάρχει ανάμεσα στο πάνω και στο κάτω μέρος του εμποδίου.
        pygame.sprite.Sprite.__init__(self)  # Αρχικοποίηση των sprites μέσα στην κλάση
        self.image = pygame.transform.scale(pygame.image.load('images/red_pipes.gif'), (69, 406))  # Φόρτωση εμποδίων
        self.rect = self.image.get_rect()  # Δήλωση εμποδίων σε μορφή rectangle
        if position == 1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι 1
            self.image = pygame.transform.flip(self.image, False, True)  # τότε δηλώνεται το πάνω μέρος του εμποδίου
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]  # και οι συντεταγμένες του
        if position == -1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι -1
            '''
                Τότε δηλώνεται το κάτω μέρος του εμποδίου,
                καθώς και οι συντεταγμένες του:
            '''
            self.rect.topleft = [x, y + int(pipe_gap / 2)]
    ''' 
    ΌΣΟ καλείται η συνάρτηση update τότε το κάθε εμπόδιο προχωράει προς τα αριστερά 
    μέχρι να ξεπεράσει τη μέση του παραθύρου.
    '''
    def update(self, speed):
        self.rect.x -= speed
        if self.rect.left < 500:
            self.kill()


"""
________________________________________________________________________________________________________________________
                                            ΔΙΑΣΤΗΜΟΠΛΟΙΑ - PLAYERS:
________________________________________________________________________________________________________________________
"""

'''
    Κλάση Διαστημοπλοίου Κύριου Παιχνιδιού:
'''


class spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites τις εικόνες του διαστημοπλοίου για να μπορώ να τις αλλάζω πιο εύκολα:
        self.sprites = [
            # 1o skins
            pygame.transform.scale(pygame.image.load('images/Spaceship_1.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            pygame.transform.scale(pygame.image.load('images/Spaceship_1_power_up_ON.png').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            # 2o skin:
            pygame.transform.scale(pygame.image.load('images/Spaceship_2.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            pygame.transform.scale(pygame.image.load('images/Spaceship_2_power_up_ON.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            # 3ο skin:
            pygame.transform.scale(pygame.image.load('images/Spaceship_3.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            pygame.transform.scale(pygame.image.load('images/Spaceship_3_power_up_ON.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            # 4o skin:
            pygame.transform.scale(pygame.image.load('images/Spaceship_4.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            pygame.transform.scale(pygame.image.load('images/Spaceship_4_power_up_ON.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            # 5o skin:
            pygame.transform.scale(pygame.image.load('images/Spaceship_5.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9))),
            pygame.transform.scale(pygame.image.load('images/Spaceship_5_power_up_ON.gif').convert_alpha(),
                                   (int(64 * 0.9), int(56 * 0.9)))

        ]
        self.current_sprite = 0     # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite     # Η εικόνα του διαστημοπλοίου ανάλογα ποιο είναι το τρέχον sprite.
        ]
        # Το διαστημόπλοιο ως rectangle και οι συντεταγμένες του
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.acceleration = 0.3  # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0  # Αρχικοποίηση της ταχύτητας
        self.clicked = False  # Δηλώνει ότι δεν έχει κάνει κλικ ο χρήστης ακόμα στην οθόνη
        self.sound = mixer.Sound('sounds/jump_sound.wav')  # Φορτώνει τον ήχο "jump" του διαστημόπλοιου.
        self.sound.set_volume(0.1)

    def update(self, GAME_OVER):
        # Ελέγχει αν έχει τελειώσει το παιχνίδι.
        if not GAME_OVER:
            # gravity
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            # control velocity:
            if self.velocity >= 11:
                self.velocity = 11
            # jump
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                # Αν ο χρήστης κάνει click και το STOP_GAME είναι False τότε το διαστημόπλοιο θα χοροπηδήσει:
                self.sound.play(0)
                self.clicked = True
                self.velocity = -4
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0

    # Όταν καλείται η συνάρτηση αυτή τότε το διαστημόπλοιο πέφτει μέχρι να ακουμπήσει το έδαφος.
    def fall(self):
        self.rect.y += 10
        if self.rect.y >= 450:
            self.rect.y = 450

    # Όταν καλείται τότε αλλάζει η εικόνα του διαστημοπλοίου.
    def change_sprite(self, current_sprite):
        self.current_sprite = current_sprite
        self.image = self.sprites[self.current_sprite]


'''
        Κλάση Διαστημοπλοίου Player 1:
                    (CO-OP)
'''


class player_1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites την εικόνα του player 1:
        self.sprites = [
            pygame.transform.scale(pygame.image.load('images/player_1.gif').convert_alpha(), (50, 46))
        ]
        self.current_sprite = 0         # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite         # Η εικόνα του player 1 ανάλογα ποιο είναι το τρέχον sprite.
        ]
        # Το διαστημόπλοιο ως rectangle και οι συντεταγμένες του
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.acceleration = 0.3  # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0  # Αρχικοποίηση της ταχύτητας
        self.pressed = False
        self.sound = mixer.Sound('sounds/jump_sound.wav')
        self.sound.set_volume(0.02)

    def update(self, GAME_OVER):
        keys = pygame.key.get_pressed()
        # Ελέγχει αν έχει τελειώσει το παιχνίδι.
        if not GAME_OVER:
            # gravity
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            # control velocity:
            if self.velocity >= 11:
                self.velocity = 11
            # jump
            if keys[pygame.K_w] and not self.pressed:
                self.pressed = True
                self.velocity = -4
                self.sound.play()
            if not keys[pygame.K_w]:
                self.pressed = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0
            # Αν πέσει εκτός ορίων τότε τηλεμεταφέρεται πάλι στην αρχική του θέση.
            if self.rect.y >= 603:
                self.rect.y = 80


'''
        Κλάση Διαστημοπλοίου Player 2:
                    (CO-OP)
'''


class player_2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites την εικόνα του player 2:
        self.sprites = [
            pygame.transform.scale(pygame.image.load('images/player_2.gif').convert_alpha(), (50, 46))
        ]
        self.current_sprite = 0         # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite         # Η εικόνα του player 2 ανάλογα ποιο είναι το τρέχον sprite.
        ]
        # Το διαστημόπλοιο ως rectangle και οι συντεταγμένες του
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.acceleration = 0.3  # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0  # Αρχικοποίηση της ταχύτητας
        self.pressed = False
        self.sound = mixer.Sound('sounds/jump_sound.wav')
        self.sound.set_volume(0.02)

    def update(self, GAME_OVER):
        keys = pygame.key.get_pressed()
        # Ελέγχει αν έχει τελειώσει το παιχνίδι.
        if not GAME_OVER:
            # gravity
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            # control velocity:
            if self.velocity >= 11:
                self.velocity = 11
            # jump
            if keys[pygame.K_UP] and not self.pressed:
                self.pressed = True
                self.velocity = -4
                self.sound.play()
            if not keys[pygame.K_UP]:
                self.pressed = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0
            # Αν πέσει εκτός ορίων τότε τηλεμεταφέρεται πάλι στην αρχική του θέση.
            if self.rect.y >= 603:
                self.rect.y = 80


"""
________________________________________________________________________________________________________________________
                                                ΕΞΩΓΗΙΝΟΙ:
________________________________________________________________________________________________________________________
"""


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας του κάθε εξωγήινου και ως rectangle καθώς και οι συντεταγμένες του.
        self.image = pygame.transform.scale(pygame.image.load('images/alien.gif'), (40, 40)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    # ΌΣΟ καλείται η συνάρτηση update τότε ο κάθε εξωγήινος προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου.
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()


"""
________________________________________________________________________________________________________________________
                                                ΠΥΡΑΥΛΟΙ:
________________________________________________________________________________________________________________________
"""


class rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας του πυραύλου και ως rectangle καθώς και οι συντεταγμένες του.
        self.image = pygame.transform.scale(pygame.image.load('images/rocket.gif'), (84, 46)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    # ΌΣΟ καλείται η συνάρτηση update τότε ο κάθε πύραυλος προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου.
    def update(self):
        self.rect.x -= 15
        if self.rect.right < 0:
            self.kill()


"""
________________________________________________________________________________________________________________________
    ΚΛΑΣΗ                                       POWER_UPS:
________________________________________________________________________________________________________________________
"""


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας των power_ups και ως rectangle καθώς και οι συντεταγμένες τους.
        self.image = pygame.transform.scale(pygame.image.load('images/power_up.gif').convert_alpha(), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    # ΌΣΟ καλείται η συνάρτηση update τότε το κάθε power_up προχωράει προς τα δεξιά μέχρι να βγει εκτός παραθύρου.
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()


"""
________________________________________________________________________________________________________________________
                                                BUTTONS:
________________________________________________________________________________________________________________________
"""

'''
        Play Button:
'''


class play_button(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/play_button.gif').convert_alpha(),
                                   (int(100 * 0.9), int(44 * 0.9))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/play_button.gif').convert_alpha(), (100, 44))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
        Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
        τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
        Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
        Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            self.image = self.sprites[self.current_sprite]
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            self.sound_check = True


'''
        Retry Button:
'''


class retry_button(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/retry_button.gif').convert_alpha(),
                                   (int(120 * 0.9), int(44 * 0.9))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/retry_button.gif').convert_alpha(), (120, 44))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_retry_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            self.image = self.sprites[self.current_sprite]
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            self.sound_check = True


'''
        Menu Button:
'''


class menu_button(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/menu_button.gif').convert_alpha(),
                                   (int(120 * 0.8), int(44 * 0.8))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/menu_button.gif').convert_alpha(),
                                   (int(120 * 0.9), int(44 * 0.9)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_menu_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        Exit Button:
'''


class exit_button(pygame.sprite.Sprite):
    """
            Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
            τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/exit_button.gif').convert_alpha(),
                                   (int(110 * 0.5), int(39 * 0.5))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/exit_button.gif').convert_alpha(),
                                   (int(110 * 0.6), int(39 * 0.6)))
        ]

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        Skin Menu Button:
'''


class skins_button(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skins_button.gif').convert_alpha(),
                                   (int(110 * 0.7), int(39 * 0.7))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skins_button.gif').convert_alpha(),
                                   (int(110 * 0.8), int(39 * 0.8)))
        ]

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        CO-OP Button:
'''


class co_op_button(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/co-op_button.gif').convert_alpha(),
                                   (int(150 * 0.6), int(44 * 0.6))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/co-op_button.gif').convert_alpha(),
                                   (int(150 * 0.7), int(44 * 0.7)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.i = 0
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


"""
________________________________________________________________________________________________________________________
                                                SKINS CHOICES:
________________________________________________________________________________________________________________________            
"""

'''
        SKIN 1:
'''


class skin_1(pygame.sprite.Sprite):

    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_1.gif').convert_alpha(),
                                   (int(130 * 0.7), int(109 * 0.7))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_1.gif').convert_alpha(),
                                   (int(130 * 0.9), int(109 * 0.9)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)
    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        SKIN 2:
'''


class skin_2(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_2.gif').convert_alpha(),
                                   (int(130 * 0.7), int(109 * 0.7))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_2.gif').convert_alpha(),
                                   (int(130 * 0.9), int(109 * 0.9)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        SKIN 3:
'''


class skin_3(pygame.sprite.Sprite):
    """
         Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
         τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_3.gif').convert_alpha(),
                                   (int(130 * 0.7), int(109 * 0.7))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_3.gif').convert_alpha(),
                                   (int(130 * 0.9), int(109 * 0.9)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        SKIN 4:
'''


class skin_4(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_4.gif').convert_alpha(),
                                   (int(130 * 0.7), int(109 * 0.7))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_4.gif').convert_alpha(),
                                   (int(130 * 0.9), int(109 * 0.9)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
        SKIN 5:
'''


class skin_5(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_5.gif').convert_alpha(),
                                   (int(130 * 0.7), int(109 * 0.7))),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/skin_5.gif').convert_alpha(),
                                   (int(130 * 0.9), int(109 * 0.9)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound('sounds/button_sound.wav')
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακούγεται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''

    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]


'''
            Τρέχον Skin:
'''


class current_skin(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        τη μετατροπή τους σε rectangle και τη θέση τους.
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Δείχνει ότι ο χρήστης χρησιμοποιεί το 1ο skin.
            pygame.transform.scale(pygame.image.load('images/skin_1.gif').convert_alpha(),
                                   (int(130 * 1.1), int(109 * 1.1))),
            pygame.transform.scale(pygame.image.load('images/skin_1.gif').convert_alpha(),
                                   (int(130 * 1.2), int(109 * 1.2))),

            # Δείχνει ότι ο χρήστης χρησιμοποιεί το 2ο skin.
            pygame.transform.scale(pygame.image.load('images/skin_2.gif').convert_alpha(),
                                   (int(130 * 1.1), int(109 * 1.1))),
            pygame.transform.scale(pygame.image.load('images/skin_2.gif').convert_alpha(),
                                   (int(130 * 1.2), int(109 * 1.2))),

            # Δείχνει ότι ο χρήστης χρησιμοποιεί το 3ο skin.
            pygame.transform.scale(pygame.image.load('images/skin_3.gif').convert_alpha(),
                                   (int(130 * 1.1), int(109 * 1.1))),
            pygame.transform.scale(pygame.image.load('images/skin_3.gif').convert_alpha(),
                                   (int(130 * 1.2), int(109 * 1.2))),

            # Δείχνει ότι ο χρήστης χρησιμοποιεί το 4ο skin.
            pygame.transform.scale(pygame.image.load('images/skin_4.gif').convert_alpha(),
                                   (int(130 * 1.1), int(109 * 1.1))),
            pygame.transform.scale(pygame.image.load('images/skin_4.gif').convert_alpha(),
                                   (int(130 * 1.2), int(109 * 1.2))),

            # Δείχνει ότι ο χρήστης χρησιμοποιεί το 5ο skin.
            pygame.transform.scale(pygame.image.load('images/skin_5.gif').convert_alpha(),
                                   (int(130 * 1.1), int(109 * 1.1))),
            pygame.transform.scale(pygame.image.load('images/skin_5.gif').convert_alpha(),
                                   (int(130 * 1.2), int(109 * 1.2)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    '''
        Με τη συνάρτηση αυτή, αλλάζει την εικόνα αυτή ανάλογα με ποιο skin διαλέξει ο παίκτης.
    '''
    def change_sprite(self, current_sprite):
        self.current_sprite = current_sprite
        self.image = self.sprites[self.current_sprite]

    '''
            Η συνάρτηση update, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι 
            πάνω στην εικόνα που δείχνει πιο skin χρησιμοποιεί 
            και αν το έχει τότε η εικόνα αυτή μεγαλώνει.
            Όσο δεν το έχει πάνω στην εικόνα τότε επιστρέφει στο αρχικό της μέγεθος.          
    '''
    def update(self, current_sprite):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = current_sprite + 1
        else:
            self.current_sprite = current_sprite
        self.image = self.sprites[self.current_sprite]


"""
________________________________________________________________________________________________________________________
                                                MENU ANIMATIONS:
________________________________________________________________________________________________________________________
"""
'''
        Animation 1:
'''


class animation_1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_count = 0        # Αρχικοποίηση του μετρητή των animations
        # Βάζω σε μία λίστα από sprites τις εικόνες του διαστημοπλοίου για να μπορώ να τις αλλάζω πιο εύκολα:
        self.sprites = [
            pygame.transform.scale(pygame.image.load('images/Spaceship_1.gif').convert_alpha(), (30, 26)),
            pygame.transform.scale(pygame.image.load('images/Spaceship_2.gif').convert_alpha(), (30, 26)),
            pygame.transform.scale(pygame.image.load('images/Spaceship_3.gif').convert_alpha(), (30, 26)),
            pygame.transform.scale(pygame.image.load('images/Spaceship_4.gif').convert_alpha(), (30, 26)),
            pygame.transform.scale(pygame.image.load('images/Spaceship_5.gif').convert_alpha(), (30, 26)),
        ]
        self.current_sprite = 0         # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite         # H εικόνα του διαστημοπλοίου ανάλογα ποιο είναι το τρέχον sprite.
        ]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]       # η θέση του κάθε διαστημοπλοίου.
        self.acceleration = 0.3         # Αρχικοποίηση της επιτάχυνσης.
        self.velocity = 0               # Αρχικοποίηση της ταχύτητας.
        self.limit = 70                 # Το όριο το οποίο δεν μπορεί να ξεπεράσει κάθε διαστημόπλοιο.
        self.ended = False              # Δηλώνει ότι δεν έχει τελειώσει το animation ακόμα.

    '''
            Αυτή η συνάρτηση καλείται όσο ο μετρητής των πόσων animations έχουν ολοκληρωθεί είναι ζυγός αριθμός.
            Όταν επιτρέπεται να καλεστεί τότε εμφανίζεται το κάθε skin του διαστημοπλοίου, 
            το ένα μετά από το άλλο, να χοροπηδάει και να κινείται προς τα δεξιά συνεχώς μέχρι να βρεθεί εκτός οθόνης
            ώσπου όταν και τα 5 εμφανιστούν, τότε αυξάνεται ο μετρητής των animations που έχουν ολοκληρωθεί κατά 1.
    '''

    def update(self, width, allow_animation_1, animation_count):
        self.animation_count = animation_count
        if self.animation_count % 2 == 0:
            self.ended = False
        if allow_animation_1:
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            if self.velocity > 5:
                self.velocity = -5
            self.rect.x += 3
            if self.rect.y <= self.limit:
                self.rect.y = self.limit
            if self.rect.x >= width + 18:
                self.rect.x = -40
                self.current_sprite += 1
                self.limit += 100
                self.rect.y += 100
                if self.current_sprite > 4:
                    self.limit = 70
                    self.rect.y = 100
                    self.ended = True
                    self.animation_count += 1
                    self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            time.sleep(0.01)

    # Επιστρέφει το μέγεθος του μετρητή των animations που έχουν ολοκληρωθεί στο κύριο πρόγραμμα.
    def Animation_count(self):
        return self.animation_count

    # Ελέγχει αν έχει τελειώσει το συγκεκριμένο animation ώστε να ξανά-ξεκινήσει το άλλο.
    def check(self):
        if self.ended:
            return True
        else:
            return False


'''
        Animation 2:
'''


class animation_2(pygame.sprite.Sprite):
    def __init__(self, x, y, limit, name):
        pygame.sprite.Sprite.__init__(self)
        self.animation_count = 0  # Αρχικοποίηση του μετρητή των animations
        # Βάζω σε μία λίστα από sprites το διαστημόπλοιο που έχει κάθε φορά διαφορετική εικόνα στο πρώτο animation:
        self.sprites = [pygame.transform.scale(pygame.image.load(name).convert_alpha(), (30, 26))]
        self.current_sprite = 0  # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite  # Η εικόνα του διαστημοπλοίου ανάλογα ποιο είναι το τρέχον sprite.
        ]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]  # Η θέση του κάθε διαστημοπλοίου.
        self.acceleration = 0.3  # Αρχικοποίηση της επιτάχυνσης.
        self.velocity = 0  # Αρχικοποίηση της ταχύτητας.
        self.limit = limit  # Το όριο το οποίο δεν μπορεί να ξεπεράσει κάθε διαστημόπλοιο.
        self.ended = False  # Δηλώνει οτι δεν έχει τελειώσει το δεύτερο animation.

    '''
        Αυτή η συνάρτηση καλείται όσο ο μετρητής των πόσων animations έχουν ολοκληρωθεί είναι μονός αριθμός.
        Όταν επιτρέπεται να καλεστεί τότε εμφανίζει ταυτόχρονα και τα πέντε skins των διαστημόπλοιων, 
        το ένα κάτω από το άλλο να χοροπηδάνε και να κινούνται προς τα δεξιά συνεχώς μέχρι να βρεθούνε εκτός οθόνης
        ώσπου αυξάνεται ο μετρητής των animations που έχουν ολοκληρωθεί κατά 1.
    '''

    def update(self, width, allow_animation_2, animation_count):
        self.animation_count = animation_count
        if self.animation_count % 2 == 1:
            self.ended = False
        if allow_animation_2:
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            if self.velocity > 5:
                self.velocity = -5
            self.rect.x += 3
            if self.rect.y <= self.limit:
                self.rect.y = self.limit
            if self.rect.x >= width + 18:
                self.ended = True
                self.rect.x = - 40
                self.animation_count += 1
            time.sleep(0.0018)

    # Επιστρέφει το μέγεθος του μετρητή των animations που έχουν ολοκληρωθεί στο κύριο πρόγραμμα.
    def Animation_count(self):
        return self.animation_count

    # Ελέγχει αν έχει τελειώσει το συγκεκριμένο animation ώστε να ξανά-ξεκινήσει το άλλο.
    def check(self):
        if self.ended:
            return True
        else:
            return False


"""
________________________________________________________________________________________________________________________
                                                GAME TITLE:
________________________________________________________________________________________________________________________
"""


class title(pygame.sprite.Sprite):
    """
        Αρχικοποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite
        και τη μετατροπή τους σε rectangle.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            # Πριν ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/title.gif').convert_alpha(), (400, 200)),

            # Αφότου ο χρήστης βάλει πάνω το ποντίκι.
            pygame.transform.scale(pygame.image.load('images/title.gif').convert_alpha(),
                                   (int(400 * 1.05), int(200 * 1.05)))
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    '''
        Η συνάρτηση update, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο τίτλο του παιχνιδιού και αν το έχει
        τότε η εικόνα του τίτλου μεγαλώνει.
        Όσο δεν το έχει πάνω στον τίτλο τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.          
    '''

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
        else:
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


"""
________________________________________________________________________________________________________________________
                                                PLAYERS BACKGROUND:
________________________________________________________________________________________________________________________
"""


'''
        Player 1 Background:
'''


class player_1_background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites το background του 1ου παίκτη.
        self.sprites = [
            pygame.transform.scale(pygame.image.load('images/SPACE_PLAYER_1.gif').convert_alpha(), (500, 603))
        ]
        self.current_sprite = 0     # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite     # Η εικόνα του background ανάλογα ποιο είναι το τρέχον sprite.
        ]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]   # Η Θέση του background


'''
        Player 2 Background:
'''


class player_2_background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites το background του 1ου παίκτη.
        self.sprites = [
            pygame.transform.scale(pygame.image.load('images/SPACE_PLAYER_2.gif').convert_alpha(), (500, 603))
        ]
        self.current_sprite = 0         # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite         # Η εικόνα του background ανάλογα ποιο είναι το τρέχον sprite.
        ]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]       # Η Θέση του background.
