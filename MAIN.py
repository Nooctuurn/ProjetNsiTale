import pygame

class Bot:
    def __init__(self, nom, pv, porter, degat, image_path):
        self.nom = nom # le nom du mob 
        self.pv = pv # les pv du mob
        self.porter = porter # la porter des coups du mob
        self.degat = degat # les degats qu'inflige le mob
        self.image = pygame.image.load(image_path).convert_alpha()  # charger l'image
        self.width, self.height = self.image.get_size() # recuperer la taille de l'image
        self.image = pygame.transform.scale(self.image, (self.width // 2, self.height // 2))  # redimensionnement l'imagge car elle est beaucoup trop grande
        self.width //= 2 # on met a jour la redimension de l'image pour l'utiliser plus tard (largeur)
        self.height //= 2 # on met a jour la redimension de l'image pour l'utiliser plus tard (longueur)

    def prend_des_degat(self, damage):
        self.pv -= damage
        if self.pv <= 0: # si le bot a plus de vie alors il est détruit
            return True
        return False  # le bot a toujours de la vie

pygame.init()
fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Affichage du Bot")

bot_de_pierre = Bot("Bot de pierre", 100, 50, 10, 'img/Bot.png') # initialisation du mob

x_bot, y_bot = 500, 200  # position de départ
direction = -1  # direction dans laquelle va aller le mob

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mise à jour des coordonnées du mouvement du bot
    if bot_de_pierre:  # si le bot est encore en vie
        x_bot += direction
        if x_bot <= 300:  # si le bot atteint la position 300
            direction = 1
        elif x_bot >= 500:  # si le bot atteint la position 500
            direction = -1

    fenetre.fill((255, 255, 255)) # Fond blanc

    # Appliquer les dégâts si le bot est encore vivant
    if bot_de_pierre :
        detruit = bot_de_pierre.prend_des_degat(1)  # inflige 1 dégât
        if detruit:
            print(f"{bot_de_pierre.nom} a perdu")
            bot_de_pierre = None  # supprimer le bot

    # Dessiner le bot et son carrer rouge si le bot est enore vivant
    if bot_de_pierre:
        rect = pygame.Rect(x_bot, y_bot, bot_de_pierre.width, bot_de_pierre.height)  # creer le rectangle autour du bot
        pygame.draw.rect(fenetre, (255, 0, 0), rect, 2)  # bordure rouge autour de l'image
        fenetre.blit(bot_de_pierre.image, (x_bot, y_bot))  # dessiner le bot

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(60)

pygame.quit()