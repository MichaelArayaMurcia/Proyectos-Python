import pygame

pygame.display.set_caption('Snake')

class Juego:
	def __init__(self):
		self.largo = 400
		self.ancho = 400
		self.rojo = (255,0,0)
		self.verde = (0,255,0)
		self.speedx = 0
		self.speedy = 0
		self.img = pygame.image.load('purple.png')
		self.gameover = False
		self.screen = pygame.display.set_mode((self.largo,self.ancho))
	def show(self):
		self.img = pygame.transform.scale(self.img,(self.largo,self.ancho))
		self.screen.blit(self.img,(0,0))	
class Snake:
	def __init__(self):
		self.x = 100
		self.y = 100
		self.largo = 10
		self.ancho = 10
	def show(self):
		pygame.draw.rect(juego.screen,juego.verde,(self.x,self.y,self.largo,self.ancho))
	def update(self):
		self.x += juego.speedx
		self.y += juego.speedy

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
	juego.show()
	snake.show()
	snake.update()
	comida.show()
	pygame.display.update()

def moverse():
	if keys[pygame.K_RIGHT]:
		juego.speedx = 1
		juego.speedy = 0
	elif keys[pygame.K_LEFT]:
		juego.speedx = -1
		juego.speedy = 0
	elif keys[pygame.K_UP]:
		juego.speedy = -1
		juego.speedx = 0
	elif keys[pygame.K_DOWN]:
		juego.speedy = 1
		juego.speedx = 0

while juego.gameover != True:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			juego.gameover = True
	moverse()
	update()

#--------------------- Final -------------------