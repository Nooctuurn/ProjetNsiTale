import pygame
import pytmx
import pyscroll
from player import Player
from perso_nj import Bot

pygame.init()

class Game:
    def __init__(self):
        # Fenêtre de jeu
        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("platformer - smash odyssey")

        # Charger la map
        tmx_data = pytmx.util_pygame.load_pygame('Assets/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Générer le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # Générer le mob
        mob_position = tmx_data.get_object_by_name("mob")
        self.bot = Bot("Demon chauve souris", 100, 1,mob_position.x, mob_position.y, 1)

        # Liste des collisions
        self.walls = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects if obj.type == "collision"]

        # Groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(self.player)
        #self.group.add(self.bot)

        # Timer pour la vérification de "is_on_ground"
        self.time_since_last_check = 0
        self.check_interval = 250  # seconde en millisecondes

    def is_on_ground(self):
        """Vérifie s'il y a un bloc de collision sous le joueur."""
        feet_rect = pygame.Rect(self.player.feet.x, self.player.feet.y + 2, self.player.feet.width, 2)
        return feet_rect.collidelist(self.walls) > -1

    def apply_gravity(self):
        """Applique la gravité uniquement si le joueur n'est pas sur le sol."""
        if not self.is_on_ground():
            self.player.velocity_y += 0.3  # Appliquer la gravité
            self.player.position.y += self.player.velocity_y
            self.player.on_ground = False
        else:
            self.player.on_ground = True
            self.player.velocity_y = 0
            
        # Mise à jour de la hitbox
        self.player.rect.y = int(self.player.position.y)
        self.player.feet.y = self.player.rect.bottom

    def handle_collisions(self):
        """Gère les collisions après le déplacement du joueur."""
        for wall in self.walls:
            if self.player.rect.colliderect(wall):
                if self.player.velocity_y > 0:  # Tombe
                    self.player.position.y = wall.top - self.player.rect.height
                    self.player.velocity_y = 0
                    self.player.on_ground = True
                elif self.player.velocity_y < 0:  # Monte
                    self.player.position.y = wall.bottom
                    self.player.velocity_y = 0
                
                if self.player.old_position.x < self.player.position.x:  # Va à droite
                    self.player.position.x = wall.left - self.player.rect.width
                elif self.player.old_position.x > self.player.position.x:  # Va à gauche
                    self.player.position.x = wall.right

        # Mise à jour de la position réelle
        self.player.rect.topleft = self.player.position

    def update(self, delta_time):
        self.player.save_location()

        self.time_since_last_check += delta_time
        if self.time_since_last_check >= self.check_interval:
            self.time_since_last_check = 0
            self.player.on_ground = self.is_on_ground()

        if not self.player.on_ground or self.player.velocity_y != 0:
            self.apply_gravity()
        self.handle_collisions()
        
        if self.bot and self.bot.pv > 0:
            self.bot.behavior(self.player.rect, 765, 965)  # Appel à la méthode behavior avec les limites gauche et droite

        self.group.update()
        self.bot.update()  


    def handle_input(self):
        """Gère les entrées clavier"""
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and self.player.on_ground:  # Correction du saut
            self.player.jump()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        if pressed[pygame.K_a]:
            self.player.dash()


    def run(self):
        """Boucle du jeu"""
        running = True
        clock = pygame.time.Clock()

        while running:
            delta_time = clock.tick(60)  # Temps écoulé en millisecondes
            self.handle_input()
            self.update(delta_time)
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            self.bot.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()