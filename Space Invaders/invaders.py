import pygame

pygame.display.set_caption('Space Invaders')


class Juego:
    def __init__(self):
        self.largo = 300
        self.ancho = 300
        self.gameover = False
        self.screen = pygame.display.set_mode((self.largo,self.ancho))
        self.negro = (0,0,0)
        self.blanco = (255,255,255)
        self.azul = (0,0,255)
        self.speed = 1  
        self.balas = 2
        self.enemigos = []
        self.img = pygame.image.load('purple.png') 
    def show(self):
        self.img = pygame.transform.scale(self.img,(self.largo,self.ancho))
        self.screen.blit(self.img,(0,0))
class Jugador:
    def __init__(self):
        self.x = juego.largo / 2
        self.y = juego.ancho - 20
        self.largo = 20
        self.ancho = 20
        self.dx = 0
        self.balas = []
        self.img = pygame.image.load('playerShip1_blue.png')
    def show(self):
        self.img = pygame.transform.scale(self.img,(self.largo,self.ancho))
        juego.screen.blit(self.img,(self.x,self.y))
class Enemigo:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.largo = 20
        self.ancho = 20
        self.img = pygame.image.load('enemyBlack1.png')
    def show(self):
        self.img = pygame.transform.scale(self.img,(self.largo,self.ancho))
        juego.screen.blit(self.img,(self.x,self.y))
class Bala:
    def __init__(self):
        self.x = jugador.x + jugador.ancho / 2
        self.y = jugador.y
        self.largo = 10
        self.ancho = 20
        self.hit = False
        self.img = pygame.image.load('laserBlue03.png')
    def show(self):
        self.img = pygame.transform.scale(self.img,(self.largo,self.ancho))
        juego.screen.blit(self.img,(self.x,self.y))
    def update(self):
        self.y -= juego.speed

juego = Juego()
jugador = Jugador()

def disparar():
    if len(jugador.balas) < juego.balas:
        jugador.balas.append(Bala())
def crearenemigos():
    for j in range(0,2):
        for i in range(0,10):
            juego.enemigos.append(Enemigo()) 
            juego.enemigos[i].x = i * 25
            juego.enemigos[i].y = j * 25
def update():
    juego.show()
    jugador.show()
    for enemigo in juego.enemigos:
        enemigo.show()
    for bala in jugador.balas:
        bala.show()
        bala.update()
    pygame.display.update()
def moverse():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        jugador.x += juego.speed
        if jugador.x == juego.largo - jugador.largo:
            jugador.x -= juego.speed
    elif keys[pygame.K_LEFT]:
        jugador.x -= juego.speed
        if jugador.x == 0:
            jugador.x += juego.speed
    elif keys[pygame.K_UP]:
        disparar()
def destruir():
    i = 0
    j = 0
    for bala in jugador.balas:
        for enemigo in juego.enemigos:
            if bala.y < enemigo.y + enemigo.largo and bala.x < enemigo.x + enemigo.ancho and bala.x > enemigo.x:
                bala.hit = True
                juego.enemigos.pop(i)
            i += 1
        if bala.y + bala.largo < 0:
            bala.hit = True
    for bala in jugador.balas:
        if bala.hit == True:
            jugador.balas.pop(j)
        j += 1
crearenemigos()

while juego.gameover != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego.gameover = True
	#------------- Cerrar el juego --------------------
    moverse()
    destruir()
    update()
#--------------------------- Final -----------------------------------