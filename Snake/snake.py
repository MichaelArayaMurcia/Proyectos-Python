import pygame

pygame.display.set_caption('Snake')

class Juego:
	def __init__(self):
		self.largo = 400
		self.ancho = 400
		self.gameover = False
		self.screen = pygame.display.set_mode((self.largo,self.ancho))

class Snake:
	pass

juego = Juego()

def update():
	pygame.display.update()


while juego.gameover != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			juego.gameover = True
