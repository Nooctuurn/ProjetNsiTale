import pygame
import pytmx
import pyscroll
from player import Player

pygame.init()

class Game:
    def __init__(self):
        # fenêtre de jeu
        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("platfomer - smash odysse")

        #charger la maps
        tmx_data = pytmx.util_pygame.load_pygame('Assets/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        #generer
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        #definir une liste qui va stocker les trucs collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        self.group.add(self.player)

    def apply_gravity(self):
        """Applique la gravité au joueur"""
        if self.player.feet.collidelist(self.walls) > -1:
            self.player.velocity_y = 0  # Arrête la chute
            self.player.position.y = self.walls[self.player.feet.collidelist(self.walls)].top - self.player.rect.height
            self.player.rect.y = int(self.player.position.y)
            self.player.feet.y = self.player.rect.bottom
            self.player.on_ground = True  # Le joueur est au sol
        else: 
            self.player.on_ground = False
            self.player.velocity_y +=0.3  # Le joueur est en l'air
            self.player.position[1] += self.player.velocity_y

    def update(self):
        """Mettre à jour les sprites"""
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

            self.apply_gravity()  # Applique la gravité au joueur

        # Actualiser la position réelle de la hitbox
        self.player.rect.topleft = self.player.position

    def handle_input(self):
        """Gère les entrées du clavier"""
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.jump()
            
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()


    def run(self):
        """Boucle du jeu"""
        running = True
        clock = pygame.time.Clock()

        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        pygame.quit()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
