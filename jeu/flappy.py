# ce code contient ma version du jeu flappy bird, il reprend les bases du dit jeu.
# création du repository : 15/09/21  finalistion du projet : X/X/X
# temps passé sur le projet : Xh ->  2h + 2h

import pygame
from pygame.locals import * 
import sys
import random
pygame.init()
pygame.display.set_caption('Flappy is flying')
PI = pygame.image.load('./Assets/interface/favicon.ico')
pygame.display.set_icon(PI)
fenetre=pygame.display.set_mode((288, 512)) # taile de la fenetre
background=pygame.image.load('./Assets/background/background-day.png') #atttribution d'une image à background


#sol
sol = pygame.image.load('./Assets/background/base.png') #attribution d'une image à sol
sol_x_pos = 0
sol = pygame.transform.scale2x(sol) #augmentation de la taille de l'image du sol, question graphique
def formation_sol():
	fenetre.blit(sol, (sol_x_pos,400)) #on affiche sol avec x = 0 (mais change plus tard) et y = 400
	
#flappy
class flappy:
    def __init__(self):
        skin = './Assets/playerskin/bluebird-downflap.png'
        self.pygame.image.load(skin)
	
while True:
    for event in pygame.event.get():
        if event.type==KEYUP : fenetre=pygame.quit()
        fenetre.blit(background, (0,0)) #affichage du fond
        formation_sol() #on lance la fonction sol
        sol_x_pos = sol_x_pos - 1 # on change la valeur de la position du sol pour le faire défiler
        if sol_x_pos <= -380: # vérification du défilement de l'image pour que le sol forme un espèce de gif
            sol_x_pos = 0     # (sinon le sol finit par disparaitre)
        pygame.time.delay(1)   # rafraichissement de l'image toute les secondes 
        pygame.display.flip()  # //


