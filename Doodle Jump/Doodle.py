import pygame
import random
#------------------------- Estado de juego -------------
gameover = False
gravedad = 1
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Doodle Jump')
onscreen = False
bricks = []
gap = [-40,40]
#------- Colores ------------------
amarillo = (255,255,0)
verde = (0,255,0)
rojo = (255,0,0)
negro = (0,0,0)
#------- Objetos ------------------
class Ball:
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r
		self.dy = gravedad
		self.dx = 0
	def show(self):
		self.y += self.dy
		self.x += self.dx
		pygame.draw.circle(screen,amarillo,(self.x,self.y),self.r)
		if(self.y > 400):
			self.y = 100
class Pipe:
	def __init__(self,x,y,largo,ancho):
		self.x = x
		self.y = y
		self.largo = largo
		self.ancho = ancho
		self.dy = 1
		self.touch = False
	def show(self):
		self.y -= self.dy
	#----------- Verificar si esta en pantalla --------------------
		if(self.y > 0):
			onscreen = True
		else:
			onscreen = False
	#----------- Verificar si lo tocó ------------------------------
		if(ball.x >= self.x and ball.x <= self.x + self.largo and ball.y >= self.y and ball.y < self.y + self.ancho):
			self.touch = True
		else:
			self.touch = False
	#----------- Cambiar acorde a lo detectado ----------------------
		if(onscreen == True and self.touch == False):
			ball.dy = 1
			pygame.draw.rect(screen,verde,(self.x,self.y,self.largo,self.ancho))
		
		if(onscreen == True and self.touch == True):
			ball.y -= 2
			pygame.draw.rect(screen,rojo,(self.x,self.y,self.largo,self.ancho))
		
		if(onscreen == False):
			self.x = random.randrange(0,300)
			self.y = random.randrange(ball.y + 100,ball.y + 150)
			pygame.draw.rect(screen,verde,(self.x,self.y,self.largo,self.ancho))
#----------------------- Bucle principal ----------------
ball = Ball(200,300,10)
pipe = Pipe(200,400,50,10)
#----------------------- Funciones ----------------------
def crear():
	for i in range(0,10):
		if(i > 0):
			x = random.choice(gap)
			y = random.choice(gap)
		else:
			x = random.randrange(0,300)
			y = random.randrange(300,400)
		bricks.append(i) 
		bricks[i] = Pipe(x,y,40,10)
crear()
def update():
	screen.fill(negro)
	ball.show()
	for i in range(0,10):
		bricks[i].show()
	pygame.display.update()
#----------------------------------
while gameover != True:
	for event in pygame.event.get():
		#----------- Cerrar el juego ----------------------
		if event.type == pygame.QUIT:
			gameover = True
		#--------------------------------------------------
		keys = pygame.key.get_pressed()
		#--------------------------------------------------
		if(keys[pygame.K_RIGHT]):
			ball.dx = 1
		elif(keys[pygame.K_LEFT]):
			ball.dx = -1
		else:
			ball.dx = 0
		#--------------------------------------------------
	update()