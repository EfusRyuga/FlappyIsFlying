# ce code contient ma version du jeu flappy bird, il reprend les bases du dit jeu.
# création du repository : 15/09/21  finalistion du projet : X/X/X
# temps passé sur le projet : Xh ->  2h + 2h + 3h30 + 46min + 2h +2 +2h30

import pygame, sys, random,time  #import des lib random système et pygame

class game:
    #méthode de génération du sol
    def formation_sol():
        screen.blit(floor_surface,(sol_x_pos,900)) # sol_x_pos = variable pour faire défiler le sol et 900 = position sur l'axe y
        screen.blit(floor_surface,(sol_x_pos + 576,900)) # sol_x_pos + 576 pour créer le défilement infini
    #méthode pour les pipes
    def check_col(pipes):
        global can_score
        global game_state
        global GO
        for pipe in pipes: # on utilise le tableau pipes
            if bird_rect.colliderect(pipe): # vérification de collision entre flappy et les pipes grâce à la fonction colliderect de pygame
                death_sound.play()
                can_score = True
                GO = True
                return False
        if bird_rect.top <= -100 or bird_rect.bottom >= 900: #définition du top et du bot où peut évoluer flappy
            can_score = True
            death_sound.play() # son de mort joué si flappy atteint les bornes de hauteur/de bas
            return False
        return True
        #méthode d'affichage du score	
    def afficher_score(game_state):
        if game_state == 'main_game':
            score1_surface = game_font.render(str(int(score)),True,(0,0,0))
            score1_rect = score1_surface.get_rect(center = (293,102))
            screen.blit(score1_surface,score1_rect)
            score_surface = game_font.render(str(int(score)),True,(255,255,255)) # font.render 3 args = text, blend, color
            score_rect = score_surface.get_rect(center = (288,100)) # coordonnées du score
            screen.blit(score_surface,score_rect)
          #méthode d'affichage sur l'écran game over
        if game_state == 'gameover':
            score_surface = game_font.render(f'Score : {int(score)}' ,True,(0,0,0))
            score_rect = score_surface.get_rect(center = (293,102))
            screen.blit(score_surface,score_rect)
            score_surface = game_font.render(f'Score : {int(score)}' ,True,(255,255,255))
            score_rect = score_surface.get_rect(center = (288,100))
            screen.blit(score_surface,score_rect)

            pressO_surface = game_font.render(f'Key press menu :', True, (0,0,0))
            pressO_rect = pressO_surface.get_rect(center = (293,172))
            screen.blit(pressO_surface,pressO_rect)
            press_surface = game_font.render(f'Key press menu :', True, (197,57,57))
            press_rect = press_surface.get_rect(center = (288,170))
            screen.blit(press_surface,press_rect)

            ombre_surface = game_font.render(f'background day = d' ,True,(0,0,0)) # 1 ombre par écritures -> +5 x +2y
            ombre_rect = ombre_surface.get_rect(center = (293,222)) 
            screen.blit(ombre_surface,ombre_rect)
            help_surface = game_font.render(f'background day = d' ,True,(197,57,57))
            help_rect = help_surface.get_rect(center = (288,220))
            screen.blit(help_surface,help_rect)

            ombre1_surface = game_font.render(f'background night = n' ,True,(0,0,0))
            ombre1_rect = ombre1_surface.get_rect(center = (293,272))
            screen.blit(ombre1_surface,ombre1_rect)
            help1_surface = game_font.render(f'background night = n' ,True,(197,57,57))
            help1_rect = help1_surface.get_rect(center = (288,270))
            screen.blit(help1_surface,help1_rect)

            ombre2_surface = game_font.render(f'Flappy yellow = y' ,True,(0,0,0))
            ombre2_rect = ombre2_surface.get_rect(center = (293,322))
            screen.blit(ombre2_surface,ombre2_rect)
            help2_surface = game_font.render(f'Flappy yellow = y' ,True,(197,57,57))
            help2_rect = help2_surface.get_rect(center = (288,320))
            screen.blit(help2_surface,help2_rect)

            ombre3_surface = game_font.render(f'Flappy red = r' ,True,(0,0,0))
            ombre3_rect = ombre3_surface.get_rect(center = (293,372))
            screen.blit(ombre3_surface,ombre3_rect)
            help3_surface = game_font.render(f'Flappy red = r' ,True,(197,57,57))
            help3_rect = help3_surface.get_rect(center = (288,370))
            screen.blit(help3_surface,help3_rect)

            ombre4_surface = game_font.render(f'Flappy blue = b' ,True,(0,0,0))
            ombre4_rect = ombre4_surface.get_rect(center = (293,422))
            screen.blit(ombre4_surface,ombre4_rect)
            help4_surface = game_font.render(f'Flappy blue = b' ,True,(197,57,57))
            help4_rect = help4_surface.get_rect(center = (288,420))
            screen.blit(help4_surface,help4_rect)


            screen.blit(game_over,game_over_pos)


            ombre5_surface = game_font.render(f'pipe red = RIGHT arrow' ,True,(0,0,0))
            ombre5_rect = ombre5_surface.get_rect(center = (293,602))
            screen.blit(ombre5_surface,ombre5_rect)
            help5_surface = game_font.render(f'pipe red = RIGHT arrow' ,True,(197,57,57))
            help5_rect = help5_surface.get_rect(center = (288,600))
            screen.blit(help5_surface,help5_rect)

            ombre6_surface = game_font.render(f'pipe green = LEFT arrow' ,True,(0,0,0))
            ombre6_rect = ombre6_surface.get_rect(center = (293,652))
            screen.blit(ombre6_surface,ombre6_rect)
            help6_surface = game_font.render(f'pipe green = LEFT arrow' ,True,(197,57,57))
            help6_rect = help6_surface.get_rect(center = (288,650))
            screen.blit(help6_surface,help6_rect)

            high_score1_surface = game_font.render(f'Local High Score : {high_score}',True,(0,0,0))
            high_score1_rect = high_score1_surface.get_rect(center = (293,852))
            screen.blit(high_score1_surface,high_score1_rect)
            high_score_surface = game_font.render(f'Local High Score : {high_score}',True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (288,850))
            screen.blit(high_score_surface,high_score_rect)
        #méthode d'affichage pour le menu
        if game_state == 'menu':
            score1_surface = game_font.render(f'Score : {int(score)}' ,True,(0,0,0))
            score1_rect = score1_surface.get_rect(center = (293,102))
            screen.blit(score1_surface,score1_rect)
            score_surface = game_font.render(f'Score : {int(score)}' ,True,(255,255,255))
            score_rect = score_surface.get_rect(center = (288,100))
            screen.blit(score_surface,score_rect)

            high_score1_surface = game_font.render(f'Local High Score : {high_score}',True,(0,0,0))
            high_score1_rect = high_score1_surface.get_rect(center = (293,852))
            screen.blit(high_score1_surface,high_score1_rect)
            high_score_surface = game_font.render(f'Local High Score : {high_score}',True,(255,255,255)) 
            high_score_rect = high_score_surface.get_rect(center = (288,850))
            screen.blit(high_score_surface,high_score_rect)
    # ancienne méthode pour le high score
 #   def update_score(score, high_score):
  #      if score > high_score:
  #          high_score = score
  #      return high_score
#nouvelle méthode, qui permet de l'enregistrer
    def update_scorev2(score, high_score):
        with open("score.txt","r") as f:
            lines = f.readlines()
            high_score = lines[0].strip()

        with open("score.txt","w") as f:
            if int(high_score) > score:
                f.write(str(high_score))
            else:
                f.write(str(score))
        return high_score

class flappy:
    #méthode d'influence de la gravité
    def effet_grav(bird):
        new_bird = pygame.transform.rotozoom(bird,-bird_movement * 4, 2) #4 = vitesse de rota et 2 = image scale
        return new_bird # affichage du skin en rota
    #méthode pour l'animation de flappy
    def flappy_frames():
        new_bird = bird_frames[bird_index]
        new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery)) # centery = center y 
        return new_bird,new_bird_rect

class tuyaux: 
    def score_verif():
        global score # on apelle la variable globale score
        global can_score # on apelle la variable globale can_score
        if pipe_list: 
            for pipe in pipe_list:
                if 95 < pipe.centerx < 105 and can_score: # si les pipes sont bornés tel que 95 < x < 105 et que can_score est vrai :
                    score += 1 # on ajoute 1 à score
                    score_sound.play() # on joue le son du pts
                    can_score = False # on passe can score à faux
                if pipe.centerx < 0: # si x du pipe = 0
                    can_score = True # on passe ca score à vrai
    #méthode de génération de tuyaux
    def crea_tuyaux():
        pipe_height = [400,600,800] #tableau qui définit la position que peuvent prendre les pipes
        random_pipe_pos = random.choice(pipe_height) # pipe prend une des pos dans le tableau pipe_height
        bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos)) # définit le pipe du bas à x = 700 et à y rand
        top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))# définit le pipe du haut à x = 700 et à y rand
        return bottom_pipe,top_pipe # affiche les deux pipes
    #méthode de déplacement des tuyaux
    def deplacement_tuyaux(pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        visible_pipes = [pipe for pipe in pipes if pipe.right > -50] # vérification de pos des pipes pour savoir quand les afficher
        return visible_pipes
    # méthode d'affichage des tuyaux
    def afficher_tuyaux(pipes):
        for pipe in pipes:
            if pipe.bottom >= 1020:  # si le pipe est plus bas que 1020 -> on ne le retourne pas
                screen.blit(pipe_surface,pipe) 
            else:
                flip_pipe = pygame.transform.flip(pipe_surface,False,True) # sinon, on le retourne à 180 pour qu'il ait la tête en bas
                screen.blit(flip_pipe,pipe)


pygame.init() #init de pygame
screen = pygame.display.set_mode((576,1024)) #taille de la fenêtre
clock = pygame.time.Clock() #utilisation de l'horloge, qui servira pour raffraichir l'image
pygame.display.set_caption('Flappy is flying') # titre de la fenêtre
PI = pygame.image.load('./Assets/interface/favicon.ico') # icone de la fenetre + icone de bas de page
pygame.display.set_icon(PI) # on set l'icone
game_font = pygame.font.Font('font.ttf',40) # on définit la police utilisée pour l'écriture
# variables générales de jeu
gravity = 0.35 #définit la vitesse où flappy tombe (force sur le vecteur y)
bird_movement = 0
game_active = False #ini du boolean sur false pour arriver sur le menu au lancement du jeu
score = 0 #ini du score à 0
high_score = 0 #ini du high score à 0 (ne sauvegarde pas les anciens high score)
can_score = True #ini de la possibilité du scoring
GO = False
#choix random du skin de fond pour débuter la partie
randbg = random.choice(['./Assets/background/background-day.png','./Assets/background/background-night.png'])
bg_surface = pygame.image.load(randbg)
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('./Assets/background/base.png')
floor_surface = pygame.transform.scale2x(floor_surface)
sol_x_pos = 0

#choix random de skin de flappy pour débuter la partie
PlayerSkin = random.choice(['bluebird','redbird','yellowbird'])
if PlayerSkin == 'bluebird':
    bird_downflap = pygame.image.load('./Assets/playerskin/bluebird-downflap.png')
    bird_midflap = pygame.image.load('./Assets/playerskin/bluebird-midflap.png')
    bird_upflap = pygame.image.load('./Assets/playerskin/bluebird-upflap.png')
elif PlayerSkin == 'redbird':
    bird_downflap = pygame.image.load('./Assets/playerskin/redbird-downflap.png')
    bird_midflap = pygame.image.load('./Assets/playerskin/redbird-midflap.png')
    bird_upflap = pygame.image.load('./Assets/playerskin/redbird-upflap.png')
elif PlayerSkin == 'yellowbird':
    bird_downflap = pygame.image.load('./Assets/playerskin/yellowbird-downflap.png')
    bird_midflap = pygame.image.load('./Assets/playerskin/yellowbird-midflap.png')
    bird_upflap = pygame.image.load('./Assets/playerskin/yellowbird-upflap.png')


bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index] # on définit l'image de flappy comme les images dans bird_frames image correspondant au bird_index
bird_rect = bird_surface.get_rect(center = (100,512)) # affichage de flappy au centre de l'image, c'est à dire en x = 100 et y = 512

BIRDFLAP = pygame.USEREVENT + 1 # création d'un birdflap qui  est définit comme un évènement pygame différent des autres puisque c'est le +1
pygame.time.set_timer(BIRDFLAP,150) # temps d'animation des frames

rand_tuyaux = random.choice(['./Assets/obstacleskin/pipe-green.png','./Assets/obstacleskin/pipe-red.png']) #choisis un skin random pour débuter
pipe_surface = pygame.image.load(rand_tuyaux)
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = [] # définition d'un tableau (vide)
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200) # 1200 ms entre chaque pipe

game_over = pygame.transform.scale2x(pygame.image.load('./Assets/interface/gameover.png'))
game_over_pos = game_over.get_rect(center = (288,512))

startimage = pygame.transform.scale2x(pygame.image.load('./Assets/interface/start2.png'))
startimagepos = startimage.get_rect(center = (288,512))
rnd_flap_sound = random.choice(['./Assets/audio/wing.wav','./Assets/audio/swoosh.wav'])
flap_sound = pygame.mixer.Sound(rnd_flap_sound)
death_sound = pygame.mixer.Sound('./Assets/audio/hit.wav')
score_sound = pygame.mixer.Sound('./Assets/audio/point.wav')
score_sound_countdown = 100
SCOREEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCOREEVENT,100)

while True: # pour toujours, vérification d'appuie de touche
    for event in pygame.event.get(): # pour quitter le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and game_active: # faire sauter l'oiseau
                bird_movement = 0
                bird_movement -= 10 # -=  fait remonter l'oiseau alors que += le fait descendre
                flap_sound.play() # on joue le son de l'oiseau qui bats des ailes

            if event.key == pygame.K_SPACE and game_active == False: # si espace pressé -> on lance le jeu
                game_active = True # vérification qu'on est pas dans les menus
                GO = False
                pipe_list.clear() # on clear tous les tuyaux
                bird_rect.center = (100,512) # on fait apparaitre flappy
                bird_movement = -5 #définit le mouvement de l'oiseau au lancement du jeu
                score = 0 # on init le score à 0
            if event.key == pygame.K_h and game_active == False:
                print("welcome to menu, here, you will get some help \n  all command, if pressed on menu, will change some parameters : \n y -> flappy is yellow \n r -> flappy is red \n b -> flappy is blue")
#change flappy skin
            if event.key == pygame.K_y and game_active == False:
                bird_downflap = pygame.image.load('./Assets/playerskin/yellowbird-downflap.png')
                bird_midflap = pygame.image.load('./Assets/playerskin/yellowbird-midflap.png')
                bird_upflap = pygame.image.load('./Assets/playerskin/yellowbird-upflap.png')
                bird_frames = [bird_downflap,bird_midflap,bird_upflap]
                bird_index = 0
                bird_surface = bird_frames[bird_index]
                bird_rect = bird_surface.get_rect(center = (100,512))
                print("flappy is now yellow")
            if event.key == pygame.K_b and game_active == False:
                bird_downflap = pygame.image.load('./Assets/playerskin/bluebird-downflap.png')
                bird_midflap = pygame.image.load('./Assets/playerskin/bluebird-midflap.png')
                bird_upflap = pygame.image.load('./Assets/playerskin/bluebird-upflap.png')
                bird_frames = [bird_downflap,bird_midflap,bird_upflap]
                bird_index = 0
                bird_surface = bird_frames[bird_index]
                bird_rect = bird_surface.get_rect(center = (100,512))
                print("flappy is now blue")
            if event.key == pygame.K_r and game_active == False:
                bird_downflap = pygame.image.load('./Assets/playerskin/redbird-downflap.png')
                bird_midflap = pygame.image.load('./Assets/playerskin/redbird-midflap.png')
                bird_upflap = pygame.image.load('./Assets/playerskin/redbird-upflap.png')
                bird_frames = [bird_downflap,bird_midflap,bird_upflap]
                bird_index = 0
                bird_surface = bird_frames[bird_index]
                bird_rect = bird_surface.get_rect(center = (100,512))
                print("flappy is now red")
#change pipe skin
            if event.key == pygame.K_RIGHT and game_active == False:
                pipe_surface = pygame.image.load('./Assets/obstacleskin/pipe-red.png')
                pipe_surface = pygame.transform.scale2x(pipe_surface)
                print("pipe is now red")
            if event.key == pygame.K_LEFT and game_active == False:
                pipe_surface = pygame.image.load('./Assets/obstacleskin/pipe-green.png')
                pipe_surface = pygame.transform.scale2x(pipe_surface)
                print("pipe is now green")
            if event.key == pygame.K_n and game_active == False:
                bg_surface = pygame.image.load('./Assets/background/background-night.png')
                bg_surface = pygame.transform.scale2x(bg_surface)
#change background skin
                print('background is now night')
            if event.key == pygame.K_d and game_active == False:
                bg_surface = pygame.image.load('./Assets/background/background-day.png')
                bg_surface = pygame.transform.scale2x(bg_surface)
                print('background is now day')
                

        if event.type == SPAWNPIPE:
            pipe_list.extend(tuyaux.crea_tuyaux()) #ajout d'un tuyau à la liste grâce à la fonction crea_tuyaux() dans la classe tuyaux

        if event.type == BIRDFLAP: # vérif de l'event BIRDFLAP (USEREVENT + 1) -> en jeu avec l'oiseau d'affiché
            if bird_index < 2:  # si la frame est inférieur à 2 : 
                bird_index += 1 # fait tourner les frames de flappy
            else: 
                bird_index = 0 # sinon on revient à la frame du début !

            bird_surface,bird_rect = flappy.flappy_frames() # définition de l'animation de flappy

    screen.blit(bg_surface,(0,0)) #affiche le fond d'écran

    if game_active: #vérifie le state "game active" -> n'est pas actif si dans le menu

        # Bird
        bird_movement += gravity #ajout de la variable gravité au déplacement de flappy
        rotated_bird = flappy.effet_grav(bird_surface) # ajout de l'effet gravité au skin de flappy
        bird_rect.centery += bird_movement # on ajoute au center y le mouvement de flappy
        screen.blit(rotated_bird,bird_rect) # affichage du skin sous gravité
        game_active = game.check_col(pipe_list) #vérification des collisions 
            
        # Pipes
        pipe_list = tuyaux.deplacement_tuyaux(pipe_list) #déplacement des tuyaux présent dans la liste de tuyaux
        tuyaux.afficher_tuyaux(pipe_list) #affichage des dits tuyaux

        #sol
        sol_x_pos -= 5 #sol ig -> même vitesse que tuyaux pour que ça ne file pas la gerbe
        game.formation_sol() # appel de la méthode formation-sol() dans la class game 
        if sol_x_pos <= -576: # création d'une loop pour que le sol ne disparaisse jamais
            sol_x_pos = 0 #réinitialisation de la position du sol
        
        # Score
        tuyaux.score_verif() #vérification du score (si le score = score +1)
        game.afficher_score('main_game') #affichage du score au state game state = main_game
        
    else: # si dans le menu
        if GO == True:
            game.afficher_score('gameover')
            screen.blit(game_over, game_over_pos)
            high_score = game.update_scorev2(score, high_score)
        else:
            screen.blit(startimage,startimagepos) # affichage de la "startimage" en précisant sa pos
            high_score = game.update_scorev2(score,high_score) # variable high score
            game.afficher_score('menu') #affichage du score au state game state = game_over

        #sol
        sol_x_pos -= 1 # vitesse lente pour avoir un menu chill
        game.formation_sol() # appel de la méthode formation_sol() dans la class game 
        if sol_x_pos <= -576: # création d'une loop pour que le sol ne disparaisse jamais
            sol_x_pos = 0 #réinitialisation de la position du sol
    
    pygame.display.update() # créer l'image
    clock.tick(100) # définit le nombre de fps plus le chiffre est grand plus le rafraichissement est régulier
