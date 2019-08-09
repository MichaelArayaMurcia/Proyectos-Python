import pygame
import random
import Objetos
#---------------- Ventana del juego -----------------
init()
pygame.display.set_caption('Arkanoid')
#---------------- Estado del juego ------------------
gameover = False
#---------------- Objetos del juego -----------------
#--------------------------------------------------
Objetos.crear()

while gameover != True:
	for event in pygame.event.get():
	#------------- Cerrar el juego --------------------
		if event.type == QUIT:
			gameover = True
	#--------------------------------------------------
	Objetos.update()
	#--------------------------------------------------
	Objetos.rebotar()
	#--------------------------------------------------
	Objetos.romper()
	#--------------------------------------------------
	Objetos.moverse()
	#--------------------------------------------------
pygame.quit()