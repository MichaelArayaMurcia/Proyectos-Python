import pygame

pygame.display.set_caption('Snake')

class Juego:
	def __init__(self):
		self.largo = 400
		self.ancho = 400
		self.rojo = (255,0,0)
		self.verde = (0,255,0)
		self.gameover = False
		self.screen = pygame.display.set_mode((self.largo,self.ancho))

class Snake:
	def __init__(self):
		self.x = 100
		self.y = 100
		self.largo = 10
		self.ancho = 10
	def show(self):
		pygame.draw.rect(juego.screen,juego.verde,(self.x,self.y,self.largo,self.ancho))

class Comida:
	def __init__(self):
		self.x = 120
		self.y = 120
		self.largo = 10
		self.ancho = 10
	def show(self):
		pygame.draw.rect(juego.screen,juego.rojo,(self.x,self.y,self.largo,self.ancho))

juego = Juego()
snake = Snake()
comida = Comida()

def update():
	snake.show()
	comida.show()
	pygame.display.update()


while juego.gameover != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			juego.gameover = True
	update()