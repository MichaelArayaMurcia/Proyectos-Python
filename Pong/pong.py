import pygame
import random
#------ Ventana del videojuego -----------
wlargo = 600
wancho = 400
screen = pygame.display.set_mode((wlargo,wancho))
pygame.display.set_caption('Pong')
#------ Colores -------------------------
blanco = (255,255,255)
negro = (0,0,0)
#------ Estado del juego -----------------
gameover = False
speed = 1
#------ Objetos del juego ----------------

class Pong:
	def __init__(self,x,y,largo,ancho):
		self.x = x
		self.y = y
		self.largo = largo
		self.ancho = ancho

class Ball:
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r
		self.dx = 0
		self.dy = 0

pongi = Pong(0,200,50,15)
pongd = Pong(590,200,50,15)
ball = Ball(wlargo / 2,wancho / 2,5)
ball.dx = random.choice([-1,1])
ball.dy = random.choice([-1,1])

def update():
	screen.fill(negro)
	pygame.draw.rect(screen,blanco,(pongi.x,pongi.y,pongi.ancho,pongi.largo))
	pygame.draw.rect(screen,blanco,(wlargo - pongd.ancho,pongd.y,pongd.ancho,pongd.largo))
	pygame.draw.circle(screen,blanco,(int(ball.x),int(ball.y)),ball.r * 2)
	pygame.display.update()

def moverse():
	keys = pygame.key.get_pressed()
	#----------- Pong derecho arriba -------------
	if keys[pygame.K_UP]:
		pongd.y -= speed
		if(pongd.y < 0):
			pongd.y += speed
	#----------- Pong derecho abajo --------------
	elif keys[pygame.K_DOWN]:
		pongd.y += speed
		if(pongd.y + pongd.largo > wancho):
			pongd.y -= speed
	#----------- Pong izquierdo arriba -----------
	elif keys[pygame.K_w]:
		pongi.y -= speed
		if(pongi.y < 0):
			pongi.y += speed
	#----------- Pong izquierdo abajo ------------
	elif keys[pygame.K_s]:
		pongi.y += speed
		if(pongi.y + pongi.largo > wancho):
			pongi.y -= speed	

def rebotar():
	ball.x += ball.dx
	ball.y += ball.dy
	#----------------------------- Rebotes Pong derecho -----------------------------
	if(ball.x > (wlargo - pongd.ancho) and ball.y < (pongd.y + pongd.largo) and ball.y > pongd.y):
		ball.dx -= 1
		ball.dy = random.choice([-1,1])
	#----------------------------- Rebotes Pong izquierdo ----------------------------
	elif(ball.x < (0 + pongi.ancho) and ball.y < (pongi.y + pongi.largo) and ball.y > pongi.y):
		ball.dx += 1
		ball.dy = random.choice([-1,1])
	#----------------------------- Rebotes verticales --------------------------------
	elif(ball.y < 0):
		ball.dy += 1 
	elif(ball.y > wancho):
		ball.dy -= 1 	
	#----------------------------- Reiniciar -----------------------------------------
	elif(ball.x < 0 or ball.x > wlargo):
		ball.x = wlargo / 2
		ball.y = wancho / 2
		ball.dx = random.choice([-1,1])
		ball.dy = random.choice([-1,1])

while gameover != True:
	pygame.mixer.music.play()
	for event in pygame.event.get():
		#----------- Cerrar el juego ----------------------
		if event.type == pygame.QUIT:
			gameover = True
	#------------ Moverse -----------------------------
	moverse()
	#------------ Rebotar -----------------------------
	rebotar()
	#------------ Actualizar la pantalla --------------
	update()
	#--------------------------------------------------

pygame.quit()