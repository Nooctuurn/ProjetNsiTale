import pygame
from pygame.locals import *

# Classe représentant le personnage
class Personnage:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def avancer(self):
        self.rect.x += 10

    def reculer(self):
        self.rect.x -= 10

    def sauter(self):
        self.rect.y -= 100  # Monter
        pygame.time.delay(200)  # Pause pour simuler le saut
        self.rect.y += 100  # Redescendre

    def afficher(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Classe principale du jeu
class Jeu:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Jeu avec Personnage")
        self.bg = pygame.image.load('image/bg.jpg')
        self.joueur = Personnage('image/PygameAssets-main/player.png', 100, 300)

    def boucle_principale(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            touches = pygame.key.get_pressed()

            # Gestion des mouvements
            if touches[K_RIGHT]:
                self.joueur.avancer()
            if touches[K_LEFT]:
                self.joueur.reculer()
            if touches[K_UP]:
                self.joueur.sauter()

            # Affichage
            self.screen.blit(self.bg, (0, 0))
            self.joueur.afficher(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# Lancer le jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.boucle_principale()
