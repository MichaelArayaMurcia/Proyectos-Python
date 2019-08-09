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
        self.img = pygame.image.load('playerShip1_blue.png')
    def show(self):
        self.img = pygame.transform.scale(self.img,(self.largo,self.ancho))
        juego.screen.blit(self.img,(self.x,self.y))
juego = Juego()
jugador = Jugador()
def update():
    juego.show()
    jugador.show()
    pygame.display.update()

while juego.gameover != True:
    for event in pygame.event.get():
	#------------- Cerrar el juego --------------------
        if event.type == pygame.QUIT:
            juego.gameover = True
    update()