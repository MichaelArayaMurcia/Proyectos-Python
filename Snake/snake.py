import pygame
import random
#-------------- Ventana del juego ---------
width = 400
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake')
#-------------- Estado del juego ----------
pygame.init()
gameover = False
#-------------- Colores -------------------
negro = (0,0,0)
blanco = (255,255,255)
rojo = (255,0,0)
verde = (0,255,0)
#-------------- Objetos -------------------
class Snake:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
def update():
	screen.fill(negro)
#-------------- Funciones -----------------
while gameover != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = True
	update()

pygame.quit()
