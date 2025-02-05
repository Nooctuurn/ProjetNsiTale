import pygame
import sys
from random import randint
from player import Player
from perso_nj import Bot
from menu import Menu 

class Game:
    def __init__(self):
        pygame.init()
        self.is_playing = False
        self.largeur, self.hauteur = 1200, 600
        self.clock = pygame.time.Clock()
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Smash Banana")
        self.bg_jeu = pygame.image.load('img/fond2.png').convert()
        self.bg_jeu = pygame.transform.scale(self.bg_jeu, (self.largeur, self.hauteur))
        self.icon = pygame.image.load('img/iconne.webp')
        pygame.display.set_icon(self.icon)

        # Initialiser le menu
        self.menu = Menu(self.ecran, self.largeur, self.hauteur)

        # Initialiser les objets du jeu
        self.player = Player(-60, 500, 0, 0, 10, 100)
        self.bot = Bot("Demon chauve souris", 100, 1, 'img/Bot.png', 700, 400, 0, 0, 4)
        self.direction_bot = -1
        self.keys_pressed = set()
        self.allowed_char = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_a]
        self.continuer = True

    def handle_events(self):
        """Gère les événements globaux (menu et jeu)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.continuer = False
            
            if not self.is_playing:
                if self.menu.in_accueil_2:
                    # Si on est sur le deuxième accueil et qu'on appuie sur une touche, on démarre le jeu
                    if event.type == pygame.KEYDOWN:
                        self.is_playing = True
                else:
                    # Vérifie si le menu détecte un clic sur "Jouer" pour passer au deuxième accueil
                    self.menu.handle_event(event)
            else:
                self.handle_solo_events(event)

    def handle_solo_events(self, event):
        """Gère les événements pour le mode solo."""
        if event.type == pygame.KEYDOWN:
            if event.key in self.allowed_char:
                self.keys_pressed.add(event.key)
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                if event.key == pygame.K_a:
                    self.player.fast_atack()

        elif event.type == pygame.KEYUP:
            if event.key in self.allowed_char:
                self.keys_pressed.discard(event.key)
                if not self.keys_pressed.intersection({pygame.K_RIGHT, pygame.K_LEFT}):
                    self.player.stop()

    def update_solo(self):
        """Met à jour le jeu en mode solo."""
        self.player.update()
        if self.bot and self.bot.pv > 0:
            self.bot_behavior()
        elif self.bot:
            self.bot = None  # Bot détruit

    def bot_behavior(self):
        """Gère le comportement du bot."""
        if self.bot.pv == 100 and self.bot.mouvement == "idle":
            self.bot.velocity[0] = self.direction_bot * self.bot.speed
            self.bot.update()
            if self.bot.position[0] <= 600:
                self.direction_bot = 1
                self.bot.move_left()
            elif self.bot.position[0] >= 800:
                self.direction_bot = -1
                self.bot.move_right()

    def draw_solo(self):
        """Affiche le jeu en mode solo."""
        self.ecran.blit(self.bg_jeu, (0, 0))
        self.player.draw(self.ecran)

        if self.bot:
            self.bot.draw(self.ecran)
        else:
            font = pygame.font.Font(None, 50)
            text = font.render("Bot détruit !", True, (255, 0, 0))
            self.ecran.blit(text, (self.largeur // 2 - 100, self.hauteur // 2))

    def run(self):
        """Boucle principale du jeu."""
        while self.continuer:
            self.handle_events()

            if self.is_playing:
                self.update_solo()
                self.draw_solo()
            else:
                self.menu.draw()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
