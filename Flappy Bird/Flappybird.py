import pygame
import random
#------- Estado del juego ---------
gameover = False
gravedad = 1
screen = pygame.display.set_mode((288,400))
pygame.display.set_caption('Flappy Bird')
onscreen = False
clock = pygame.time.Clock()
#------- Colores ------------------
amarillo = (255,255,0)
verde = (0,255,0)
rojo = (255,0,0)
negro = (0,0,0)
birdimg = pygame.image.load('bird.png')
fondo = pygame.image.load('background-night.png')
pipetop = pygame.image.load('Top_pipe.png')
pipebottom = pygame.image.load('Bottom_pipe.png')
#------- Objetos ------------------
class Bird:
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r
		self.dy = gravedad
	def show(self):
		self.y += self.dy
		screen.blit(birdimg,(self.x,self.y))
class Pipe:
	def __init__(self,x,y,largo,ancho):
		self.x = x
		self.y = y
		self.largo = largo
		self.ancho = ancho
		self.dx = 1
		self.gap = 100
		self.touch = False
		self.topimage = None
		self.bottomimage = None
	def show(self):
		self.x -= self.dx
	#----------- Verificar si esta en pantalla --------------------
		if(self.x + self.largo > 0):
			onscreen = True
		else:
			onscreen = False
	#----------- Verificar si lo tocó ------------------------------
		if(bird.x >= self.x and bird.y <= self.y + self.ancho):
			self.touch = True
		elif(bird.x >= self.x and bird.y >= self.y + self.gap + self.ancho):
			self.touch = True
		else:
			self.touch = False
	#----------- Cambiar acorde a lo detectado ----------------------
		if(onscreen == True and self.touch == False):
			
			self.topimage = pygame.transform.scale(pipetop,(self.largo,self.ancho))
			self.bottomimage = pygame.transform.scale(pipebottom,(self.largo,400 - self.y + self.gap + self.ancho))

			screen.blit(self.topimage,(self.x,self.y))
			screen.blit(self.bottomimage,(self.x,self.y + self.gap + self.ancho))

		if(onscreen == True and self.touch == True):
			self.topimage = pygame.transform.scale(pipetop,(self.largo,self.ancho))
			self.bottomimage = pygame.transform.scale(pipebottom,(self.largo,400 - self.y + self.gap + self.ancho))

			screen.blit(self.topimage,(self.x,self.y))
			screen.blit(self.bottomimage,(self.x,self.y + self.gap + self.ancho))

		if(onscreen == False):
			self.x = 200
			self.ancho = random.randint(100,200)

bird = Bird(25,200,15)
pipe = Pipe(100,0,30,random.randint(100,200))
#------- Funciones ----------------
def update():
	screen.blit(fondo,(0,0))
	bird.show()
	pipe.show()
	pygame.display.update()
#----------------------------------
while gameover != True:
	for event in pygame.event.get():
		#----------- Cerrar el juego ----------------------
		if event.type == pygame.QUIT:
			gameover = True
		#--------------------------------------------------
		keys = pygame.key.get_pressed()
		#----------- Saltar  -------------
		if keys[pygame.K_UP]:
			bird.y -= 60
		#--------------------------------------------------
	update();