"""
       ΒΙΒΛΙΟΘΗΚΕΣ:
"""
# Από έτοιμο script παίρνει όλες τις αρχικές μεταβλητές του Παιχνιδιού.
import pygame.sprite
from Game_Variables import *

'''
                ΚΕΝΤΡΙΚΗ LOOPA:
    Η κεντρική loopa εκτελείται συνεχώς μέχρι να κλείσει ο χρήστης το αρχικό παράθυρο. 
    Η συγκεκριμένη loopa περιέχει μια loopa που εμφανίζει το αρχικό menu, μια άλλη που εμφανίζει το menu με τα skins
    και μία ακόμα που εμφανίζει το κύριο παιχνίδι.  

'''

while MAIN_LOOP:
    """
    ____________________________________________________________________________________________________________________
                                                                    MENU:
    ____________________________________________________________________________________________________________________
                Δήλωση του πρώτου animation:
            Επειδή στο πρώτο animation εμφανίζονται όλα τα διαφορετικά διαστημόπλοια το ένα μετά απο το άλλο,
            τότε προσθέτεται μόνο μία class στο group του animation 1, 
            που αποτελείτε από 5 διαφορετικά sprites αλλάζοντας το ένα μετά το άλλο.
    """
    animation1_group = pygame.sprite.Group()
    spaceships_1 = animation_1(-20, 100)
    animation1_group.add(spaceships_1)
    allow_animation_1 = True
    '''
            Δήλωση του δεύτερου animation:
        Επειδή στο δεύτερο animation εμφανίζονται όλα τα διαστημόπλοιο την ίδια στιγμή,   
        μία λίστα που περιέχει ως στοιχεία την ίδια κλάση 5 φορές αλλά με διαφορετικές παραμέτρους,
        προσθέτεται στο group του animation 2.
    '''
    animation2_group = pygame.sprite.Group()
    spaceships_2 = [
        animation_2(-20, 100, 70, 'images/Spaceship_1.gif'),
        animation_2(-20, 200, 170, 'images/Spaceship_2.gif'),
        animation_2(-20, 300, 270, 'images/Spaceship_3.gif'),
        animation_2(-20, 400, 370, 'images/Spaceship_4.gif'),
        animation_2(-20, 500, 470, 'images/Spaceship_5.gif')
    ]
    for elem in range(5):
        animation2_group.add(spaceships_2[elem])
    allow_animation_2 = False
    animation_count = 0  # O αριθμός των animations που έχουν τελειώσει αρχικοποιείται σε μηδέν
    # music
    mixer.music.load('music/menu_music.mp3')
    mixer.music.play(-1)  # Το -1 είναι για να παίζει τη μουσική επ' άπειρον.
    mixer.music.set_volume(0.5)
    while menu:

        '''
                                        DRAW MENU:
            Εκτελεί τη συνάρτηση που δημιουργεί το παράθυρο που εμφανίζει το αρχικό menu:
        '''
        draw_menu(  # Παράμετροι:
            wn, MENU_picture, title_group, High_score,  # Menu.
            font_high_score, font_current_skin,  # Fonts.
            animation1_group, animation2_group, current_skin_group,  # Groups.
            exit_button_group, play_button_group, co_op_button_group, skins_button_group  # Buttons.
        )
        '''
                                        CLASS UPDATES:
        '''
        current_skin_group.update(current_sprite)
        title_group.update()
        '''
        ----------------------------------------------------------------------------------------------------------------
                                                            ANIMATION:
            Το menu έχει δύο animations. Πιο συγκεκριμένα, μόλις τελειώσει το πρώτο τότε ξεκινάει το δεύτερο και μόλις 
            τελειώσει το δεύτερο ξανά ξεκινάει το πρώτο πάλι κλπ.
        ----------------------------------------------------------------------------------------------------------------
        '''
        '''
                   ANIMATION 1:   
        '''

        if spaceships_2[0].check():
            allow_animation_2 = False
            allow_animation_1 = True
            animation_count = spaceships_2[0].Animation_count()
        if allow_animation_1:
            animation1_group.update(width, allow_animation_1, animation_count)

        '''
                ANIMATION 2
        '''
        if spaceships_1.check():
            allow_animation_2 = True
            allow_animation_1 = False
            animation_count = spaceships_1.Animation_count()
        if allow_animation_2:
            animation2_group.update(width, allow_animation_2, animation_count)
        '''
        ----------------------------------------------------------------------------------------------------------------
                                                BUTTONS:
        ----------------------------------------------------------------------------------------------------------------
        '''

        if CO_OP_button.check_button_clicked():
            # Αν πατηθεί το κουμπί CO-OP τότε ξεκινάει CO-OP:
            CO_OP = True
            Game = False
            menu = False
            skins = False

        if Skins_button.check_button_clicked():
            # Αν πατηθεί το κουμπί με τα skins τότε ανοίγει το menu με τα skins:
            Game = False
            menu = False
            skins = True
            CO_OP = False

        if Play_button.check_button_clicked():
            # Αν πατηθεί το κουμπί play τότε ξεκινάει το παιχνίδι:
            Game = True
            menu = False
            skins = False
            CO_OP = False

        if Exit_button.check_button_clicked():
            # Αν πατηθεί το κουμπί exit, τότε κλείνει το παράθυρο:
            Game = False
            MAIN_LOOP = False
            menu = False
            skins = False
            CO_OP = False
        '''
            Μόλις ο Χρήστης κάνει "click" εκεί που κλείνει το παράθυρο τότε θέτει όλες 
            τις loopes σε False και κλείνει η εφαρμογή:
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False
                CO_OP = False

        pygame.display.update()
    mixer.music.stop()  # Σταματάει τη μουσική του menu.

    '''
    ____________________________________________________________________________________________________________________
                                                        SKIN ΜΕΝU:
    ____________________________________________________________________________________________________________________
    '''

    # Δηλώνει τη class με το κουμπί που επιστρέφει στο αρχικό menu:
    menu_button_group.remove(Menu_button)
    Menu_button = menu_button(500, 500)
    menu_button_group.add(Menu_button)
    while skins:
        # Καλεί τη συνάρτηση που εμφανίζει το menu με τα skins:
        draw_skin_menu(
            # Παράμετροι Συνάρτησης:
            wn,  # Παράθυρο.
            font_skins,  # Fonts.
            skin_1_group, skin_2_group, skin_3_group, skin_4_group, skin_5_group, menu_button_group  # Buttons.
        )

        '''
                    Σε αυτό το menu δίνονται στον χρήστη 5 επιλογές για το τι skin θα επιλέξει για το διαστημόπλοιο
                    και ανάλογα ποιο skin θα επιλέξει, τότε θα ξεκινάει το κεντρικό παιχνίδι με αυτό.
        '''
        if Skin_1.check_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
            current_sprite = 0
        if Skin_2.check_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
            current_sprite = 2
        if Skin_3.check_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
            current_sprite = 4
        if Skin_4.check_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
            current_sprite = 6
        if Skin_5.check_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
            current_sprite = 8

        # Αν πατηθεί το κουμπί που λέει menu τότε επιστρέφει τον χρήστη στο αρχικό menu.
        if Menu_button.check_menu_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
        '''
            Μόλις ο Χρήστης κάνει "click" εκεί που κλείνει το παράθυρο τότε θέτει όλες 
            τις loopes σε False και κλείνει η εφαρμογή:
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False
                CO_OP = False

    """
    ____________________________________________________________________________________________________________________
                                                        GAME:
    ____________________________________________________________________________________________________________________
    
    """

    ''' 
        GAME_ENDING:
    '''
    STOP_GAME = False  # Σταματάει το παιχνίδι αν γίνει True.
    GAME_OVER = False  # Αν γίνει True σημαίνει οτι έχασε ο παίκτης

    ''' 
     MUSIC AND SOUND EFFECTS:
    '''
    mixer.music.load('music/space_music.wav')  # Φορτώνει τη μουσική του παιχνιδιού.
    death_sound_effect = mixer.Sound('sounds/death_sound.wav')  # Φορτώνει τον ήχο που κάνει όταν χάνει.
    death_sound = True  # Δεν ξανά-επαναλαμβάνεται ο ήχος που κάνει όταν χάνει ο χρήστης
    death_sound_effect.set_volume(0.2)  # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.

    '''
     ΠΥΡΑΥΛΟΣ:
    '''
    charge = False  # Απαγορεύει να επιτεθεί ο πύραυλος στο διαστημόπλοιο
    spawn = True  # Επιτρέπει να εμφανιστεί πύραυλος στην οθόνη
    rocket_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε τους πυραύλους

    '''
     ΕΜΠΟΔΙΑ:
    '''
    pipe_frequency = 1500  # Συχνότητα εμποδίων σε milliseconds
    last_pipe = - pipe_frequency
    pipe_counter = 0  # Αρχικό νούμερο εμποδίων
    pipe_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε τα εμπόδια
    missing_pipe_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε για το υπόλοιπο των εμποδίων

    ''' 
     ΔΙΑΣΤΗΜΟΠΛΟΙΟ:
    '''
    spaceship_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε το διαστημόπλοιο
    Spaceship = spaceship(100, 80)  # Φορτώνει την κλάση του διαστημοπλοίου σε sprite
    spaceship_group.add(Spaceship)  # Βάζει το sprite διαστημόπλοιο μέσα στο group

    '''
     BACKGROUND:
    '''
    background_image = pygame.image.load('images/SPACE.jpg')  # Φορτώνει την εικόνα του background
    # Μετατρέπει το μέγεθος της εικόνας του background στο μέγεθος του παραθύρου:
    background = pygame.transform.scale(background_image, (width, height))
    background_rect = pygame.Rect(0, 0, 0, 0)  # Οι αρχικές συντεταγμένες του background και το μέγεθος του ως Rectangle

    '''
     ΕΔΑΦΟΣ:
    '''
    # Φορτώνει την εικόνα του Εδάφους:
    ground_image = pygame.image.load('images/ground.gif')
    # Μετατρέπει το μέγεθος της εικόνας του Εδάφους στο μέγεθος του παραθύρου
    ground = pygame.transform.scale(ground_image, (width, height + 33))
    ground_rect = pygame.Rect(0, -30, 0, 0)  # Οι αρχικές συντεταγμένες του εδάφους και το μέγεθος του ως Rectangle.

    '''
      POWER_UP:
    '''
    power_up = False  # Το power up είναι ανενεργό
    power_up_used = False  # Δεν έχει χρησιμοποιηθεί power up
    SPACE_pressed = False  # Δηλώνει ότι δεν πατήθηκε το κουμπί SPACE
    power_up_text_disappear = False  # Εμφανίζεται το κείμενο με τον μετρητή των power ups
    seconds_text_disappear = True  # Δεν εμφανίζεται το κείμενο με τα seconds
    power_up_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε τα power ups
    power_ups = 1  # Αρχικό νούμερο των power ups
    power_up_seconds = 0  # Αρχικοποίηση δευτερολέπτων που κρατάει το κάθε power up

    '''
     ΕΞΩΓΗΙΝΟΙ:
    '''
    alien_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε τους εξωγήινους
    '''
     TIME:
    '''
    clock = pygame.time.Clock()  # Δημιουργεί ένα αντικείμενο ρολογιού που μετρά την ώρα.
    starting = pygame.time.get_ticks()

    '''
     SCORE:
    '''
    score = 0  # Αρχικοποιεί τον μετρητή του score σε μηδέν.
    '''
     SKIN:
    '''
    Spaceship.change_sprite(current_sprite)  # Το διαστημόπλοιο ξεκινάει με το skin που προ-επέλεξε ο παίκτης.

    if retry_button_clicked:
        Game = True
        retry_button_clicked = False
    if Game:
        mixer.music.play(-1)  # Το -1 είναι για να παίζει τη μουσική επ' άπειρον.
    # Ξανά δηλώνει τη class με το κουμπί που επιστρέφει στο αρχικό menu:
    menu_button_group.remove(Menu_button)
    Menu_button = menu_button(80, 30)
    menu_button_group.add(Menu_button)
    # όσο είναι True μπορεί να ξεκινήσει το παιχνίδι
    while Game:
        # Σε περίπτωση που το διαστημόπλοιο ακουμπήσει το έδαφος τότε χάνει ο παίκτης
        if spaceship_group.sprites()[0].rect.y >= 450:
            GAME_OVER = True
        clock.tick(60)  # αλλάζει 60 frames ανά δευτερόλεπτο
        '''
                    window DRAWING:
        '''

        # Εκτελεί τη συνάρτηση που δημιουργεί το παράθυρο του κύριου παιχνιδιού:
        draw_game(
            # Παράμετροι Συνάρτησης:
            wn, ground, ground_rect, background, background_rect, width,  # Window
            score, power_ups, power_up_seconds,  # Texts
            pipe_group, spaceship_group, power_up_group, missing_pipe_group, alien_group, rocket_group,  # Groups
            power_up_text_disappear, seconds_text_disappear,  # Έλεγχος εμφάνισης κειμένων.
            font_score, font_seconds, font_power_ups, font_guide  # Fonts
        )

        '''
        
                           ΔΗΜΙΟΥΡΓΙΑ ΠΟΛΛΑΠΛΩΝ ΕΜΠΟΔΙΩΝ:
        
        '''

        time_now = pygame.time.get_ticks()  # Μετράει την τρέχον χρονική στιγμή σε milliseconds
        ''' 
            
                Όταν το αποτέλεσμα της αφαίρεσης της τρέχον χρονικής στιγμή,
                με το πότε εμφανίστηκε το προηγούμενο εμπόδιο, 
                είναι μεγαλύτερο απο τη συχνότητα εμφάνισης των εμποδίων τότε εμφανίζεται ένα νέο εμπόδιο.
                
        '''
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)  # Δημιουργεί ένα τυχαίο ακέραιο αριθμό για το ύψος των εμποδίων
            btm_pipe = pipe(width, int(height / 2) + pipe_height - 70, -1)  # Κάτω μέρος του εμποδίου με τυχαίο ύψος.
            tp_pipe = pipe(width, int(height / 2) + pipe_height - 50, 1)  # Πάνω μέρος του εμποδίου με τυχαίο ύψος.
            pipe_group.add(btm_pipe)  # Βάζει το κάτω μέρος του εμποδίου στο group με τα εμπόδια
            pipe_group.add(tp_pipe)  # Βάζει το πάνω μέρος του εμποδίου στο group με τα εμπόδια
            missing_pipe = restpipe(width - 1, 485)  # Είναι για να φαίνεται ότι το εμπόδιο ακουμπάει το έδαφος.
            missing_pipe_group.add(missing_pipe)  # Το βάζει σε ειδικό group από sprites.
            last_pipe = time_now  # Δηλώνει τη χρονική στιγμή που εμφανίστηκε το τελευταίο εμπόδιο.
            pipe_counter += 1  # Μετράει πόσα εμπόδια έχουν δημιουργηθεί
            '''
                
                ΣΥΧΝΟΤΗΤΑ ΕΜΦΑΝΙΣΗΣ ΚΑΘΕ ΕΞΩΓΗΙΝΟΥ:
                
                Αρχικά σε αυτό κομμάτι αυτό του κώδικά μας, έχουμε δημιουργήσει ένα μετρητή,
                που μετρά πόσα εμπόδια έχουν εμφανιστεί, μετά θα παράγουμε συνεχώς έναν τυχαίο αριθμό 
                σε βρόχο 20 επαναλήψεων. Ο τυχαίος αριθμός αυτός θα παίρνει τιμές 
                από τη μεταβλητή num1 μέχρι τη μεταβλητή num2, όπου θα ξεκινάνε με τιμές 1 και 10 αντίστοιχα και 
                στο τέλος κάθε επανάληψης του βρόχου θα αυξάνονται κατά 10 και οι δύο. 
                Τέλος, σε κάθε επανάληψη του βρόχου θα ελέγχει αν ο τυχαίος αριθμός που παρήγαγε είναι ίσος
                με τον μετρητή εμποδίων, αν ο έλεγχος αυτός βγει αληθής τότε εμφανίζεται ένας εξωγήινος.
                    
            '''
            num1 = 1  # Αρχικοποίησης 1ης μεταβλητής ή αλλιώς num1 σε 1
            num2 = 10  # Αρχικοποίησης 2ης μεταβλητής ή αλλιώς num2 σε 10
            for i in range(20):  # Βρόχος 20 επαναλήψεων
                if pipe_counter == random.randint(num1, num2):  # Έλεγχος μεταξύ μετρητή εμποδίων και τυχαίου αριθμού.
                    '''
                     Το ύψος στο οποίο θα εμφανίζεται κάθε εξωγήινος θα έχει μια τυχαία τιμή απο 50 εώς 300.
                     Ο κάθε εξωγήινος θα πρέπει να εμφανίζεται δίπλα σε κάθε εμπόδιο και όχι πάνω σε αυτό. 
                    Το πόσο δίπλα θα εμφανίζεται, θα είναι μία τυχαία τιμή από 190 μέχρι 300.
                     Τέλος όλοι οι εξωγήινοι βρίσκονται σε ένα group απο sprites.
                    '''
                    alien_y = random.randint(50, 300)
                    alien_x = random.randint(190, 300)
                    alien = Alien(width + alien_x, alien_y)
                    alien_group.add(alien)
                num1 = num1 + 10  # Αύξηση 1ης μεταβλητής num1 κατά 10
                num2 = num2 + 10  # Αύξηση 2ης μεταβλητής num2 κατά 10
            '''
            
                ΣΥΧΝΟΤΗΤΑ ΕΜΦΑΝΙΣΗΣ ΚΑΘΕ POWER UP:
        
                    Αρχικά, θα παράγουμε συνεχώς έναν τυχαίο αριθμό σε βρόχο 20 επαναλήψεων. 
                    Ο τυχαίος αριθμός αυτός θα παίρνει τιμές από τη μεταβλητή num1 μέχρι τη μεταβλητή num2, 
                    όπου θα ξεκινάνε με τιμές 1 και 20 αντίστοιχα, 
                    και στο τέλος κάθε επανάληψης του βρόχου θα αυξάνονται κατά 20 και οι δύο. 
                    Τέλος, σε κάθε επανάληψη του βρόχου θα ελέγχει αν ο τυχαίος αριθμός που παρήγαγε είναι ίσος
                    με τον μετρητή εμποδίων, αν ο έλεγχος αυτός βγει αληθής τότε εμφανίζεται ένα power_up.
            
            '''
            num3 = 1  # Αρχικοποίησης 1ης μεταβλητής ή αλλιώς num1 σε 1
            num4 = 20  # Αρχικοποίησης 2ης μεταβλητής ή αλλιώς num2 σε 40
            for i in range(20):  # Βρόχος 20 επαναλήψεων
                if pipe_counter == random.randint(num3, num4):  # Έλεγχος μεταξύ μετρητή εμποδίων και τυχαίου αριθμού.
                    '''
                     Το ύψος στο οποίο θα εμφανίζεται κάθε power_up θα έχει μια τυχαία τιμή απο 50 εώς 300.
                     To κάθε power_up θα πρέπει να εμφανίζεται δίπλα σε κάθε εμπόδιο και όχι πάνω σε αυτό. 
                     Το πόσο δίπλα θα εμφανίζεται, θα είναι μία τυχαία τιμή από 190 μέχρι 300.
                     Τέλος όλα τα power_ups βρίσκονται σε ένα group απο sprites.
                   '''
                    power_up_y = random.randint(50, 300)
                    power_up_x = random.randint(190, 300)
                    POWER_UP = PowerUp(width + power_up_x, power_up_y)
                    power_up_group.add(POWER_UP)
                num3 = num3 + 20  # Αύξηση 1ης μεταβλητής num1 κατά 40
                num4 = num4 + 20  # Αύξηση 2ης μεταβλητής num2 κατά 40

        ''' 
            
            Ελέγχει αν έχει χάσει ο παίκτης ή όχι για να δει αν χρειάζεται να σταματήσει το παιχνίδι: 
            
        '''
        if GAME_OVER:
            STOP_GAME = True
            ''' 
            Αν έχει χάσει ο παίκτης τότε εμφανίζεται ένα κουμπί στην οθόνη που τον ρωτάει αν θέλει να ξαναπροσπαθήσει.
            Αν το πατήσει τότε ξανά ξεκινάει το παιχνίδι από την αρχή.
                
            '''
            retry_button_group.draw(wn)
            if Retry_button.check_retry_button_clicked():
                retry_button_clicked = True
                menu = False
                Game = False
                skins = False
                CO_OP = False
            mixer.music.stop()  # Σταματάει τη μουσική, αν σταματήσει το παιχνίδι.
            '''
                 Η μεταβλητή death_sound είναι για να μην επαναλαμβάνεται συνέχεια το death_sound_effect
            '''
            if death_sound:
                death_sound_effect.play(0)
                death_sound = False

        ''' 
            
        Σταματάει το παιχνίδι σε περίπτωση που γίνει το STOP_GAME True 
        και το διαστημόπλοιο αρχίζει και πέφτει μέχρι να βρει έδαφος: 
            
        '''
        if not STOP_GAME:
            # Αν το διαστημόπλοιο ακουμπήσει κάποιο εμπόδιο ή κάποιον πύραυλο, ο χρήστης χάνει:
            if not power_up:
                if len(pipe_group) > 0:
                    if pygame.sprite.collide_mask(Spaceship, pipe_group.sprites()[0]):
                        GAME_OVER = True
                    if pygame.sprite.collide_mask(Spaceship, pipe_group.sprites()[1]):
                        GAME_OVER = True
                if len(rocket_group) > 0:
                    if pygame.sprite.collide_mask(Spaceship, rocket_group.sprites()[0]):
                        GAME_OVER = True
            '''
                
                                Κινούμενο έδαφος και κινούμενο background:
                   
                Δηλαδή έχουμε 2 ίδια εδάφοι τα οποία τα εμφανίζουμε το ένα δίπλα στο άλλο 
                και κινούνται και τα δύο ταυτόχρονα δίνοντας την ψευδαίσθηση ότι κουνιέται ο παίκτης.
                Μόλις το ένα από τα δύο πάρει το χ του το μέγεθος του 
                πλάτους του παραθύρου σε αρνητική τιμή, τότε το χ του αποκτά την τιμή μηδέν. Αυτό, επαναλαμβάνεται 
                μέχρι να τελειώσει το παιχνίδι και το ίδιο ισχύει και για το background.
            '''
            # ΕΔΑΦΟΣ (ground):
            ground_rect.x -= 4
            if ground_rect.x == -width:
                ground_rect.x = 0
            # BACKGROUND:
            background_rect.x -= 2
            if background_rect.x == -width:
                background_rect.x = 0

            '''
            ΚΑΛΕΙ ΤΗ ΣΥΝΑΡΤΗΣΗ UPDATE ΑΠΟ ΤΙΣ ΚΛΑΣΕΙΣ:
            '''
            alien_group.update()  # 1.Των εξωγήινων
            pipe_group.update(4)  # 2.Των εμποδίων
            missing_pipe_group.update()  # 3.Του υπολοίπου των εμποδίων
            power_up_group.update()  # 4.Των power ups
            spaceship_group.update(GAME_OVER)  # 5.Του διαστημοπλοίου
            '''
                            ΠΥΡΑΥΛΟΣ:
                Καταρχάς, το ύψος στο οποίο θα εμφανίζεται κάθε πύραυλος θα έχει μια τυχαία τιμή από 50 εώς 400
                και η αρχική του θέση θα είναι από τα δεξιά αλλά εκτός της οθόνης. Έπειτα, όσο το score 
                έχει τιμές 10,20,30,40 δηλαδή διαιρείται ακριβώς με το 10 τότε αν η μεταβλητή spawn, 
                είναι αληθής, εμφανίζεται πύραυλος στην οθόνη και η spawn παίρνει κατευθείαν την τιμή False
                για να μην εμφανίζεται ταυτόχρονα πάνω από ένας πύραυλος, στην οθόνη. Μετά, δίνει στη μεταβλητή
                charge την τιμή True, η οποία ελέγχει το πότε να κινηθεί ο πύραυλος από δεξιά προς τα αριστερά μέσω της 
                συνάρτησης update της κλάσης rocket. 
                Με λίγα λόγια αν ο μετρητής του σκορ έχει τιμή που τελειώνει σε 9 (π.χ 9,19,29 κλπ) τότε και ΜΟΝΟ τότε
                εμφανίζεται ΈΝΑΣ μόνο πύραυλος στη οθόνη. Τέλος, αν το πύραυλος ακουμπήσει το διαστημόπλοιο, 
                ο χρήστης χάνει.  
                    
            '''

            rocket_height = random.randint(50, 400)  # Η τιμή του y του πυραύλου με τυχαίο ακέραιο από το 50 εώς το 400.
            Rocket = rocket(width, rocket_height)  # Οι αρχικές συντεταγμένες του πυραύλου.
            if (score + 1) % 10 == 0:  # Γίνεται True μόνο αν το score έχει τιμές 10,20,30,40,50 κλπ.
                if spawn:  # Ελέγχει αν μπορεί να εμφανίσει πύραυλο στην οθόνη
                    rocket_group.add(Rocket)  # Αν μπορεί τότε εμφανίζει τον πύραυλο στην οθόνη
                    spawn = False  # Απαγορεύει στον πύραυλο να ξαναεμφανιστεί μέχρι το spawn να γίνει True
                charge = True  # Επιτρέπει στον πύραυλο να επιτεθεί στον διαστημόπλοιο
            if charge:  # Ελέγχει αν επιτρέπετε να επιτεθεί ο πύραυλος στο διαστημόπλοιο
                rocket_group.update()  # Καλεί τη συνάρτηση update από την κλάση rocket
                ''' 
                Αν ο μετρητής του σκορ έχει τιμή που τελειώνει σε 9 (π.χ 9,19,29 κλπ), 
                επιτρέπει το να εμφανιστεί πύραυλος στην οθόνη.                           
                '''
                if score % 10 == 0:
                    spawn = True
            '''
                
                    POWER UP
                        
            '''
            # Αν τα power ups έχουν τελειώσει τότε απαγορεύει στον παίκτη να τα ξαναχρησιμοποιήσει
            if power_ups > 0:
                power_up_used = False
            keys = pygame.key.get_pressed()  # Μεταβλητή που ελέγχει αν έχει πατηθεί κάποιο κουμπί από το πληκτρολόγιο.
            if not power_up_used:  # Όσο δεν έχει χρησιμοποιηθεί το τρέχον power up
                '''
                    Όσο το κουμπί SPACE δεν έχει πατηθεί ακόμα τότε:
                        1.ξεκινάει ο μετρητής του χρόνου για το power up
                        2.δηλώνει ότι πατήθηκε για να μη γίνεται τίποτα όσο μένει πατημένο.
                        3.δηλώνει οτι ένα power up χρησιμοποιήθηκε
                        4.εξαφανίζεται το κείμενο που εξηγεί πως να χρησιμοποιηθεί το power up
                '''
                if not SPACE_pressed:
                    if keys[pygame.K_SPACE]:
                        start_ticks = pygame.time.get_ticks()
                        SPACE_pressed = True
                        power_ups -= 1
                        power_up_text_disappear = True
                else:  # ΑΛΛΙΩΣ
                    ''' 
                    Όσο ο μετρητής του χρόνου δεν ξεπερνά τα 4 δευτερόλεπτα ή αλλιώς τα 4000 milliseconds 
                    ή όσο το διαστημόπλοιο ακουμπάει κάποιο εμπόδιο κατά την διάρκεια που λειτουργεί το power up τότε:
                    '''
                    power_up_seconds = (pygame.time.get_ticks() - start_ticks)
                    if power_up_seconds <= 4000 or pygame.sprite.spritecollideany(Spaceship, pipe_group):
                        power_up = True  # 1.δηλώνεται ότι το power up είναι ενεργό
                        Spaceship.change_sprite(current_sprite + 1)  # 2.αλλάζει η εμφάνιση το διαστημόπλοιο
                        seconds_text_disappear = False  # 3.όσο το power_up είναι ενεργό, εμφανίζονται τα seconds
                    else:  # ΑΛΛΙΩΣ αν τα ξεπεράσει ή το διαστημόπλοιο δεν ακουμπάει κάποιο εμπόδιο τότε:
                        power_up = False  # 1.δηλώνεται ότι το power up είναι ανενεργό
                        seconds_text_disappear = True  # 2.και όσο είναι ανενεργό εξαφανίζεται το κείμενο με τα seconds
                        Spaceship.change_sprite(current_sprite)  # 3.το διαστημόπλοιο παίρνει την αρχική του εμφάνιση
                        SPACE_pressed = False  # 4.δηλώνεται ότι το κουμπί SPACE σταματάει να είναι πατημένο
                        power_up_used = True  # 5.δηλώνεται ότι το τρέχον power έχει χρησιμοποιηθεί
        else:
            # Καλεί την εντολή fall από την κλάση spaceship όπου κάνει το διαστημόπλοιο να πέφτει
            Spaceship.fall()

        '''
                Μετρητής του SCORE και μετρητής των power_ups:
            Όσο ο μετρητής των εμποδίων που έχουν δημιουργηθεί είναι πάνω από μηδέν 
            τότε αν το διαστημόπλοιο ακουμπήσει έναν οποιοδήποτε power_up,
            ελέγχει αν έχει ήδη αυξήσει τον μετρητή των power_ups κατά 1 
            ή αν το διαστημόπλοιο ακουμπήσει έναν οποιοδήποτε εξωγήινο,    
            ελέγχει αν έχει ήδη αυξήσει τον μετρητή του score κατά 5.      
            Αυτό το κάναμε για να μην παίρνει άπειρους πόντους όσο ακουμπάει κάποιον εξωγήινο ή
            να μην παίρνει άπειρα power_ups όσο ακουμπάει κάποιο power_up. 
            Επίσης αν το διαστημόπλοιο περάσει ανάμεσα από ένα εμπόδιο τότε προσθέτετε 1 πόντος στο score.
                 
        '''

        if pipe_counter > 0:  # Ελέγχει αν ο μετρητής των εμποδίων είναι πάνω απο μηδέν
            '''
                Μετρητής των power_ups:
            '''
            # Για κάθε ξεχωριστό power_up που ακουμπά το διαστημόπλοιο προσθέτεται μόνο 1 power_up.
            if len(power_up_group) > 0:
                if pygame.sprite.collide_mask(Spaceship, power_up_group.sprites()[0]):
                    add_power_up = True
                    if add_power_up:
                        power_ups += 1
                        add_power_up = False
                    # Κάθε power_up που ακουμπά το διαστημόπλοιο αφαιρείται από το group των power_ups
                    power_up_group.sprites()[0].kill()
            '''
                Μετρητής του SCORE:
            '''
            # Για κάθε ξεχωριστό εξωγήινο που ακουμπά το διαστημόπλοιο προσθέτονται μόνο 5 πόντοι στο score τη φορά
            if pygame.sprite.spritecollideany(Spaceship, alien_group):
                add_score = True
                if add_score:
                    score += 5
                    add_score = False
                # Κάθε εξωγήινος που ακουμπά το διαστημόπλοιο αφαιρείται από το group των εξωγήινων
                alien_group.sprites()[0].kill()
            '''
            Όταν η τετμημένη του διαστημοπλοίου και η τετμημένη του πρώτου εμποδίου είναι ίσες, 
            δηλαδή αν το διαστημόπλοιο περάσει ανάμεσα από το συγκεκριμένο εμπόδιο τότε προσθέτετε 1 πόντος στο score.
            '''
            if spaceship_group.sprites()[0].rect.x == pipe_group.sprites()[0].rect.x and not STOP_GAME:
                score += 1
        # Μετά από 4 δευτερόλεπτα εξαφανίζεται το κείμενο που εξηγεί στον παίκτη πως να χρησιμοποιήσει τα power ups του.
        secs = (pygame.time.get_ticks() - starting)
        if secs >= 4000:
            power_up_text_disappear = True
        '''
        Αν το τρέχον score του παίκτη ξεπεράσει το προηγούμενο high score τότε εκείνο γίνεται το νέο high score
         και το γράφει στο αρχείο highscore.txt
        '''
        if High_score < score:
            High_score = score
            with open('files/highscore.txt', 'w') as f:
                f.write(str(High_score))
        '''
            Αν ο χρήστης πατήσει το κουμπί menu τότε επιστρέφει στο αρχικό menu.
        '''
        menu_button_group.draw(wn)
        if Menu_button.check_menu_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
        '''
            
        Μόλις ο Χρήστης κάνει "click" εκεί που κλείνει το παράθυρο τότε θέτει όλες 
        τις loopes σε False και κλείνει η εφαρμογή: 
            
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False
                CO_OP = False

        pygame.display.update()  # Κάνει update την οθόνη.
    pipe_group.remove()  # αφαιρεί από το group με τα εμπόδια όλα τα εμπόδια
    mixer.music.stop()  # Σταματάει τη μουσική, αν σταματήσει το παιχνίδι.
    """
    --------------------------------------------------------------------------------------------------------------------
                                                            CO - OP:
    """
    mixer.music.load('music/CO_OP_music.mp3')  # Φορτώνει τη μουσική του παιχνιδιού.
    stop_game = False
    game_over = False
    blue_pipe_group = pygame.sprite.Group()
    red_pipe_group = pygame.sprite.Group()
    pipe_frequency = 1500  # Συχνότητα εμποδίων σε milliseconds
    last_pipe_1 = - pipe_frequency
    last_pipe_2 = - pipe_frequency
    player_1_group = pygame.sprite.Group()
    Player_1 = player_1(100, 80)
    player_1_group.add(Player_1)
    player_2_group = pygame.sprite.Group()
    Player_2 = player_2(600, 80)
    player_2_group.add(Player_2)
    start = pygame.time.get_ticks()

    # Ελέγχει αν πρέπει να ξανά ξεκινήσει το CO-OP από την αρχή.
    if retry_COOP_clicked:
        CO_OP = True
        retry_COOP_clicked = False
    '''
     Results:
    '''
    player_2_winner = False
    player_1_winner = False
    DRAW = False
    '''
        Music and sound effects (CO-OP):
    '''
    # Αν η loopa του CO-OP είναι αληθές τότε ξεκινάει παίζει τη μουσική του CO-OP:
    if CO_OP:
        mixer.music.play(-1)
    player_1_won_sound_effect = mixer.Sound('sounds/win_1.wav')  # Φορτώνει τον ήχο "win" του player 1.
    player_2_won_sound_effect = mixer.Sound('sounds/win_2.wav')  # Φορτώνει τον ήχο "win" του player 2.
    player_won_sound = True  # Δεν ξανά-επαναλαμβάνεται ο ήχος που κάνει όταν χάνει ο χρήστης
    draw_sound = True  # Δεν ξανά-επαναλαμβάνεται ο ήχος που κάνει όταν χάνει ο χρήστης
    draw_sound_effect = mixer.Sound('sounds/death_sound.wav')
    player_2_won_sound_effect.set_volume(0.2)
    while CO_OP:
        draw_co_op(
            # Παράμετροι Συνάρτησης:
            wn, player_1_background_group, player_2_background_group, border,  # Παράθυρο
            red_pipe_group, blue_pipe_group,  # Εμπόδια
            menu_button_group,  # Buttons
            player_1_group, player_2_group  # Players
        )
        if game_over:
            stop_game = True
            mixer.music.stop()  # Σταματάει τη μουσική, αν σταματήσει το παιχνίδι.
            retry_button_group.draw(wn)
            if Retry_button.check_retry_button_clicked():
                retry_COOP_clicked = True
                menu = False
                Game = False
                skins = False
                CO_OP = False

        clock.tick(60)  # αλλάζει 60 frames ανά δευτερόλεπτο
        '''
                        PIPES:
        '''
        seconds = pygame.time.get_ticks() - start
        if not stop_game:
            time_now = pygame.time.get_ticks()  # Μετράει την τρέχον χρονική στιγμή σε milliseconds
            if seconds > 3000:
                if time_now - last_pipe_1 > pipe_frequency:
                    pipe_height = random.randint(-100, 100)  # Δημιουργεί ένα τυχαίο ακέραιο για το y των εμποδίων
                    btm_pipe_1 = blue_pipe(width / 2, int(height / 2) + pipe_height - 70,
                                           -1)  # Κάτω μέρος του εμποδίου
                    tp_pipe_1 = blue_pipe(width / 2, int(height / 2) + pipe_height - 50, 1)  # Πάνω μέρος του εμποδίου
                    blue_pipe_group.add(btm_pipe_1)  # Βάζει το κάτω μέρος του εμποδίου στο group με τα εμπόδια
                    blue_pipe_group.add(tp_pipe_1)  # Βάζει το πάνω μέρος του εμποδίου στο group με τα εμπόδια
                    last_pipe_1 = time_now  # Δηλώνει τη χρονική στιγμή που εμφανίστηκε το τελευταίο εμπόδιο.

                if time_now - last_pipe_2 > pipe_frequency:
                    pipe_height = random.randint(-100, 100)  # Δημιουργεί ένα τυχαίο ακέραιο για το ύψος των εμποδίων
                    btm_pipe_2 = red_pipe(width, int(height / 2) + pipe_height - 70, -1)  # Κάτω μέρος του εμποδίου
                    tp_pipe_2 = red_pipe(width, int(height / 2) + pipe_height - 50, 1)  # Πάνω μέρος του εμποδίου
                    red_pipe_group.add(btm_pipe_2)  # Βάζει το κάτω μέρος του εμποδίου στο group με τα εμπόδια
                    red_pipe_group.add(tp_pipe_2)  # Βάζει το πάνω μέρος του εμποδίου στο group με τα εμπόδια
                    last_pipe_2 = time_now  # Δηλώνει τη χρονική στιγμή που εμφανίστηκε το τελευταίο εμπόδιο.
                blue_pipe_group.update(4)  # Κάνει update τη συνάρτηση της κλάσης με τα εμπόδια του 1ου player.
                red_pipe_group.update(4)  # Κάνει update τη συνάρτηση της κλάσης με τα εμπόδια του 2ου player.
            else:
                draw_player_1_guide(wn, font_players)  # Εξηγεί πως να χειριστεί τον χαρακτήρα του ο player 1
                draw_player_2_guide(wn, font_players)  # Εξηγεί πως να χειριστεί τον χαρακτήρα του ο player 2
                draw_game_starts(wn, seconds, font_score)  # Δείχνει πότε ξεκινάει το CO-OP.
            if len(red_pipe_group) > 1 and len(blue_pipe_group) > 1:
                # Αν ο player 2 ακουμπήσει εμπόδιο αλλά ο player 1 δεν ακουμπάει εμπόδιο τότε νικάει ο player 1
                if pygame.sprite.collide_mask(Player_2, red_pipe_group.sprites()[0]) or pygame.sprite.collide_mask(
                        Player_2, red_pipe_group.sprites()[1]):
                    if not (pygame.sprite.collide_mask(Player_1,
                                                       blue_pipe_group.sprites()[0]) or pygame.sprite.collide_mask(
                            Player_1, blue_pipe_group.sprites()[1])):
                        game_over = True
                        player_1_winner = True
                        player_2_winner = False
                        DRAW = False
                # Αν ο player 1 ακουμπήσει εμπόδιο αλλά ο player 2 δεν ακουμπάει εμπόδιο τότε νικάει ο player 2
                if pygame.sprite.collide_mask(Player_1, blue_pipe_group.sprites()[0]) or pygame.sprite.collide_mask(
                        Player_1, blue_pipe_group.sprites()[1]):
                    if not (pygame.sprite.collide_mask(Player_2,
                                                       red_pipe_group.sprites()[0]) or pygame.sprite.collide_mask(
                            Player_2, red_pipe_group.sprites()[1])):
                        game_over = True
                        player_2_winner = True
                        player_1_winner = False
                        DRAW = False
                # Αν ο player 1 και ο player 2 ακουμπήσουν κάποιο εμπόδιο ταυτόχρονα τότε βγαίνει Ισοπαλία:
                if pygame.sprite.spritecollideany(Player_2, red_pipe_group) \
                        or pygame.sprite.spritecollideany(Player_2, red_pipe_group):
                    if pygame.sprite.spritecollideany(Player_1, blue_pipe_group) or pygame.sprite.spritecollideany(
                            Player_1, blue_pipe_group):
                        game_over = True
                        player_2_winner = False
                        player_1_winner = False
                        DRAW = True
            player_1_group.update(game_over)
            player_2_group.update(game_over)
        """
                    Αποτελέσματα παιχνιδιού:
            1η Περίπτωση: 1ος Παίκτης Νικητής.
                Αν νικήσει ο 1ος παίκτης, τότε ακούγεται μόνο μία φορά, ένας συγκεκριμένος ήχος
                και εμφανίζεται ένα μήνυμα στην οθόνη ότι Νίκησε player 1. 
                
            2η Περίπτωση: 2ος Παίκτης Νικητής.
                Αν νικήσει ο 2ος παίκτης, τότε ακούγεται μόνο μία φορά, ένας συγκεκριμένος ήχος 
                και εμφανίζεται ένα μήνυμα στην οθόνη ότι Νίκησε player 2.
                    
            3η Περίπτωση: Ισοπαλία.
                Αν βγει ισοπαλία, τότε ακούγεται μόνο μία φορά, ένας συγκεκριμένος ήχος 
                και εμφανίζεται ένα μήνυμα στην οθόνη ότι βγήκε ισοπαλία.  
        """
        if player_1_winner:
            if player_won_sound:
                player_1_won_sound_effect.play(0)
                player_won_sound = False
            player_1_win(wn, font_CO_OP)
        if player_2_winner:
            if player_won_sound:
                player_2_won_sound_effect.play(0)
                player_won_sound = False
            player_2_win(wn, font_CO_OP)
        if DRAW:
            if draw_sound:
                draw_sound_effect.play(0)
                draw_sound = False
            Draw(wn, font_CO_OP)
        # Αν πατηθεί το κουμπί πο γράφει menu τότε επιστρέφει στο αρχικό menu.
        if Menu_button.check_menu_button_clicked():
            Game = False
            skins = False
            menu = True
            CO_OP = False
        '''
            Μόλις ο Χρήστης κάνει "click" εκεί που κλείνει το παράθυρο τότε θέτει όλες 
            τις loopes σε False και κλείνει η εφαρμογή:
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CO_OP = False
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False
        pygame.display.update()
    # Αφαιρεί από το group με τα εμπόδια κάθε παίκτη όλα τα εμπόδια που είχαν προστεθεί:
    blue_pipe_group.remove()
    red_pipe_group.remove()
    # Σταματάει τη μουσική, αν σταματήσει το CO-OP.
    mixer.music.stop()
pygame.quit()
