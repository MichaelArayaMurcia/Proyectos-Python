import pygame
import random
import numpy

width = 400
height = 400
screen = pygame.display.set_mode((width,height))
#---------------- Colores ---------------------------
negro = (0,0,0)
blanco = (255,255,255)
azul = (0,0,255)
speed = 1
ballimg = pygame.image.load('ball.jpg')
brickimg = pygame.image.load('blue-brick.png')
jugadorimg = pygame.image.load('table.png')
#------------------------------------------------------
w, h = 10, 2
bricks = [[0 for x in range(w)] for y in range(h)]
#------------------------------------------------------
fondo = pygame.image.load('background.png')
#------------------------------------------------------
class Jugador:
	def __init__(self,x,y,largo,ancho):
		self.x = x
		self.y = y
		self.largo = largo
		self.ancho = ancho
		self.dx = 0
		self.img = None
	def show(self):
		self.img = pygame.transform.scale(jugadorimg,(self.largo,self.ancho))
		screen.blit(self.img,(self.x,self.y))
class Bloque:
	def __init__(self,x,y,largo,ancho):
		self.x = x
		self.y = y
		self.largo = largo
		self.ancho = ancho
		self.img = None
	def show(self):
		self.img = pygame.transform.scale(brickimg,(self.largo,self.ancho))
		for j in range(0,2):
			for i in range(0,10):
				screen.blit(self.img,(bricks[j][i].x,bricks[j][i].y))
class Bola:
	def __init__(self,x,y,largo,ancho):
		self.x = x
		self.y = y
		self.largo = largo
		self.ancho = ancho
		self.dx = random.choice([-0.5,0.5])
		self.dy = random.choice([-0.2,0.2])
		self.img = None
	def show(self):
		self.x += self.dx
		self.y += self.dy
		self.img = pygame.transform.scale(ballimg,(self.largo,self.ancho))
		screen.blit(self.img,(self.x,self.y))

jugador = Jugador(150,390,50,10)
bola = Bola(200,200,10,10)
bloque = Bloque(0,0,30,10)

def rebotar():
	#----------------------------- Rebotes Horizontales -----------------------------
	if(bola.x < 0 or bola.x > 400):
		bola.dx = -bola.dx
	#----------------------------- Rebotes verticales --------------------------------
	elif(bola.y <= 0):
		bola.dy = -bola.dy 
	#----------------------------- Rebotes de jugador --------------------------------
	elif(bola.y >= jugador.y and bola.x >= jugador.x and bola.x <= jugador.x + jugador.largo):
		bola.dx = random.choice([-0.5,0.5])
		bola.dy = -bola.dy
	#----------------------------- Reiniciar -----------------------------------------
	elif(bola.y > 400):
		bola.x = 400 / 2
		bola.y = 400 / 2
		bola.dx = random.choice([-0.5,0.5])
		bola.dy = random.choice([-0.2,0.2])
def update():
	#screen.blit(fondo,(0,0))
	jugador.show()
	bloque.show()
	bola.show()
	pygame.display.update()
def moverse():
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		jugador.x += speed
		if jugador.x == 350:
			jugador.x -= speed
	elif keys[pygame.K_LEFT]:
		jugador.x -= speed
		if jugador.x == 0:
			jugador.x += speed
def crear():
	for j in range(0,2):
		for i in range(0,10):
			x = 40 * i
			y = 30 * j
			bricks[j][i] = Bloque(x,y,30,10)
def romper():
	#----------------------------- Rebotes bloques -----------------------------------
	for j in range(0,len(bricks)):
		for i in range(0,len(bricks[0])):
			if(bola.x >= bricks[j][i].x and 
			   bola.x + bola.largo  <= bricks[j][i].x + bricks[j][i].largo and 
			   bola.y + bola.ancho <= bricks[j][i].y + bricks[j][i].ancho):
				bricks[j][i].ancho = 0
				bricks[j][i].largo = 0
				bricks[j][i].x = -1
				bola.dx = -bola.dx
				bola.dy = -bola.dy

