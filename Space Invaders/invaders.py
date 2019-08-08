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

juego = Juego()

while juego.gameover != True:
    for event in pygame.event.get():
	#------------- Cerrar el juego --------------------
        if event.type == pygame.QUIT:
            juego.gameover = True
    pygame.display.update()