# ce code contient ma version du jeu flappy bird, il reprend les bases du dit jeu.
# création du repository : 15/09/21  finalistion du projet : X/X/X
# temps passé sur le projet : Xh ->  2h + 2h + 3h30 + 46min + 2h

import pygame, sys, random  #import des lib random système et pygame

class game:
#méthode de génération du sol
	def formation_sol():
		screen.blit(floor_surface,(sol_x_pos,900))
		screen.blit(floor_surface,(sol_x_pos + 576,900))
#méthode pour les pipes
	def check_col(pipes):
		global can_score
		for pipe in pipes:
			if bird_rect.colliderect(pipe):
				death_sound.play()
				can_score = True
				return False
		if bird_rect.top <= -100 or bird_rect.bottom >= 900: #définition du top et du bot où peut évoluer flappy
			can_score = True
			death_sound.play()
			return False
		return True
#méthode d'affichage du score	
	def afficher_score(game_state):
		if game_state == 'main_game':
			score_surface = game_font.render(str(int(score)),True,(255,255,255))
			score_rect = score_surface.get_rect(center = (288,100))
			screen.blit(score_surface,score_rect)
		if game_state == 'game_over':
			score_surface = game_font.render(f'Score: {int(score)}' ,True,(255,255,255))
			score_rect = score_surface.get_rect(center = (288,100))
			screen.blit(score_surface,score_rect)

			high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
			high_score_rect = high_score_surface.get_rect(center = (288,850))
			screen.blit(high_score_surface,high_score_rect)
#méthode pour le high score
	def update_score(score, high_score):
		if score > high_score:
			high_score = score
		return high_score

class flappy:
#méthode d'influence de la gravité
	def effet_grav(bird):
		new_bird = pygame.transform.rotozoom(bird,-bird_movement * 4, 2) #4 = vitesse de rota et 1 = image scale
		return new_bird
#méthode pour l'animation de flappy
	def flappy_frames():
		new_bird = bird_frames[bird_index]
		new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
		return new_bird,new_bird_rect

class tuyaux:
	def score_verif():
		global score, can_score 
		if pipe_list:
			for pipe in pipe_list:
				if 95 < pipe.centerx < 105 and can_score: # reste à définir l'utilité des bornes
					score += 1
					score_sound.play()
					can_score = False
				if pipe.centerx < 0: # vérification de l'allignement de flappy avec les tuyaux
					can_score = True
#méthode de génération de tuyaux
	def crea_tuyaux():
		random_pipe_pos = random.choice(pipe_height)
		bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
		top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
		return bottom_pipe,top_pipe
#méthode de déplacement des tuyaux
	def deplacement_tuyaux(pipes):
		for pipe in pipes:
			pipe.centerx -= 5
		visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
		return visible_pipes
# méthode d'affichage des tuyaux
	def afficher_tuyaux(pipes):
		for pipe in pipes:
			if pipe.bottom >= 1024: 
				screen.blit(pipe_surface,pipe)
			else:
				flip_pipe = pygame.transform.flip(pipe_surface,False,True)
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

#choix random du skin de fond pour débuter la partie
randbg = random.choice(['./Assets/background/background-day.png','./Assets/background/background-night.png'])
bg_surface = pygame.image.load(randbg).convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('./Assets/background/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
sol_x_pos = 0

 #choix random de skin de flappy pour débuter la partie
PlayerSkin = random.choice(['bluebird','redbird','yellowbird'])
if PlayerSkin == 'bluebird':
    bird_downflap = pygame.image.load('./Assets/playerskin/bluebird-downflap.png').convert_alpha()
    bird_midflap = pygame.image.load('./Assets/playerskin/bluebird-midflap.png').convert_alpha()
    bird_upflap = pygame.image.load('./Assets/playerskin/bluebird-upflap.png').convert_alpha()
elif PlayerSkin == 'redbird':
    bird_downflap = pygame.image.load('./Assets/playerskin/redbird-downflap.png').convert_alpha()
    bird_midflap = pygame.image.load('./Assets/playerskin/redbird-midflap.png').convert_alpha()
    bird_upflap = pygame.image.load('./Assets/playerskin/redbird-upflap.png').convert_alpha()
elif PlayerSkin == 'yellowbird':
	bird_downflap = pygame.image.load('./Assets/playerskin/yellowbird-downflap.png').convert_alpha()
	bird_midflap = pygame.image.load('./Assets/playerskin/yellowbird-midflap.png').convert_alpha()
	bird_upflap = pygame.image.load('./Assets/playerskin/yellowbird-upflap.png').convert_alpha()


bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

rand_tuyaux = random.choice(['./Assets/obstacleskin/pipe-green.png','./Assets/obstacleskin/pipe-red.png']) #choisis un skin random pour débuter
pipe_surface = pygame.image.load(rand_tuyaux)
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('./Assets/interface/start2.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))
rnd_flap_sound = random.choice(['./Assets/audio/wing.wav','./Assets/audio/swoosh.wav'])
flap_sound = pygame.mixer.Sound(rnd_flap_sound)
death_sound = pygame.mixer.Sound('./Assets/audio/hit.wav')
score_sound = pygame.mixer.Sound('./Assets/audio/point.wav')
score_sound_countdown = 100
SCOREEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCOREEVENT,100)

while True: # pour toujours, vérification d'appuie de touche
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement -= 12
				flap_sound.play()

			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100,512)
				bird_movement = 0
				score = 0
			if event.key == pygame.K_h and game_active == False:
				print("welcome to menu, here, you will get some help \n  all command, if pressed on menu, will change some parameters : \n y -> flappy is yellow \n r -> flappy is red \n b -> flappy is blue")
#change flappy skin
			if event.key == pygame.K_y and game_active == False:
				bird_downflap = pygame.image.load('./Assets/playerskin/yellowbird-downflap.png').convert_alpha()
				bird_midflap = pygame.image.load('./Assets/playerskin/yellowbird-midflap.png').convert_alpha()
				bird_upflap = pygame.image.load('./Assets/playerskin/yellowbird-upflap.png').convert_alpha()
				bird_frames = [bird_downflap,bird_midflap,bird_upflap]
				bird_index = 0
				bird_surface = bird_frames[bird_index]
				bird_rect = bird_surface.get_rect(center = (100,512))
				print("flappy is now yellow")
			if event.key == pygame.K_b and game_active == False:
				bird_downflap = pygame.image.load('./Assets/playerskin/bluebird-downflap.png').convert_alpha()
				bird_midflap = pygame.image.load('./Assets/playerskin/bluebird-midflap.png').convert_alpha()
				bird_upflap = pygame.image.load('./Assets/playerskin/bluebird-upflap.png').convert_alpha()
				bird_frames = [bird_downflap,bird_midflap,bird_upflap]
				bird_index = 0
				bird_surface = bird_frames[bird_index]
				bird_rect = bird_surface.get_rect(center = (100,512))
				print("flappy is now blue")
			if event.key == pygame.K_r and game_active == False:
				bird_downflap = pygame.image.load('./Assets/playerskin/redbird-downflap.png').convert_alpha()
				bird_midflap = pygame.image.load('./Assets/playerskin/redbird-midflap.png').convert_alpha()
				bird_upflap = pygame.image.load('./Assets/playerskin/redbird-upflap.png').convert_alpha()
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
				bg_surface = pygame.image.load('./Assets/background/background-night.png').convert()
				bg_surface = pygame.transform.scale2x(bg_surface)
#change background skin
				print('background is now night')
			if event.key == pygame.K_d and game_active == False:
				bg_surface = pygame.image.load('./Assets/background/background-day.png').convert()
				bg_surface = pygame.transform.scale2x(bg_surface)
				print('background is now day')
                

		if event.type == SPAWNPIPE:
			pipe_list.extend(tuyaux.crea_tuyaux()) #ajout d'un tuyau à la liste

		if event.type == BIRDFLAP: #fait tourner les frames de flappy pour créer son animation de vol
			if bird_index < 2:
				bird_index += 1
			else:
				bird_index = 0

			bird_surface,bird_rect = flappy.flappy_frames()

	screen.blit(bg_surface,(0,0)) #affiche le fond d'écran

	if game_active: #vérifie le state "game active" -> n'est pas actif si dans le menu

		# Bird
		bird_movement += gravity #ajout de la variable gravité au déplacement de flappy
		rotated_bird = flappy.effet_grav(bird_surface) # ajout de l'effet gravité au skin de flappy
		bird_rect.centery += bird_movement # ?????????
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
		screen.blit(game_over_surface,game_over_rect)
		high_score = game.update_score(score,high_score)
		game.afficher_score("game_over") #affichage du score au state game state = game_over

		#sol
		sol_x_pos -= 1 # vitesse lente pour avoir un menu chill
		game.formation_sol() # appel de la méthode formation_sol() dans la class game 
		if sol_x_pos <= -576: # création d'une loop pour que le sol ne disparaisse jamais
			sol_x_pos = 0 #réinitialisation de la position du sol

	# Floor
	
	

	pygame.display.update() # créer l'image
	clock.tick(100) # définit le nombre de fps plus le chiffre est grand plus le rafraichissement est régulier
