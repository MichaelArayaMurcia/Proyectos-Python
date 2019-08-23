import pygame
import random

pygame.init()
pygame.display.set_caption('Snake')

class Juego:
	def __init__(self):
		self.largo = 400
		self.ancho = 400
		self.rojo = (255,0,0)
		self.verde = (0,255,0)
		self.azul = (0,0,255)
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
		self.largo = 20
		self.ancho = 20
		self.cola = []
	def show(self):
		pygame.draw.rect(juego.screen,juego.azul,(self.x,self.y,self.largo,self.ancho))
		for cola in self.cola:
			pygame.draw.rect(juego.screen,juego.verde,(cola.x,cola.y,cola.largo,cola.ancho))
	def update(self):
		for cola in self.cola:
			i = 0
			self.cola[0].x += juego.speedx
			self.cola[0].y += juego.speedy
			if i > 0:
				cola.x = self.cola[i - 1].x
				cola.y = self.cola[i - 1].y
			i += 1
	def comer(self):
		if self.cola[0].x == comida.x and self.cola[0].y == comida.y:
			comida.x = random.randrange(0,40) * 10
			comida.y = random.randrange(0,40) * 10
			cola = Snake()
			self.cola.append(cola)
class Comida:
	def __init__(self):
		self.x = 120
		self.y = 120
		self.largo = 20
		self.ancho = 20
	def show(self):
		pygame.draw.rect(juego.screen,juego.rojo,(self.x,self.y,self.largo,self.ancho))

juego = Juego()
snake = Snake()
snake.cola.append(snake)
comida = Comida()

def update():
	juego.show()
	snake.show()
	snake.update()
	snake.comer()
	comida.show()
	pygame.display.update()

def moverse():
	if keys[pygame.K_RIGHT]:
		juego.speedx = 5
		juego.speedy = 0
	elif keys[pygame.K_LEFT]:
		juego.speedx = -5
		juego.speedy = 0
	elif keys[pygame.K_UP]:
		juego.speedy = -5
		juego.speedx = 0
	elif keys[pygame.K_DOWN]:
		juego.speedy = 5
		juego.speedx = 0

while juego.gameover != True:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			juego.gameover = True
	moverse()
	update()

#--------------------- Final -------------------