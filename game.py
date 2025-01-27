import pygame
import pytmx
import pyscroll
from player import Player

pygame.init()

class Game:
    def __init__(self):
        # fenêtre de jeu
        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("platfomer - smash banana")

        #charger la maps
        tmx_data = pytmx.util_pygame.load_pygame('image/Free.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.5

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

    def update(self):
        # Mettre à jour les sprites
        self.group.update()

        # Appliquer la gravité au joueur
        self.player.apply_gravity()

        # Vérification des collisions avec les murs
        self.player.on_ground = False  # Par défaut, le joueur n'est pas au sol
        for wall in self.walls:  # Parcours des murs
            if self.player.feet.colliderect(wall):  # Si les pieds touchent un mur
                if self.player.velocity_y > 0:  # Si le joueur tombe
                    self.player.on_ground = True
                    self.player.velocity_y = 0

                    # Évite les vibrations en appliquant une marge
                    delta = abs(self.player.position[1] - (wall.top - self.player.rect.height))
                    if delta > 1:  # Seulement si le décalage est significatif
                        self.player.position[1] = wall.top - self.player.rect.height
                    break  # Sortir de la boucle une fois qu'une collision est traitée

        # Actualiser la position réelle de la hitbox
        self.player.rect.topleft = self.player.position


    def draw_debug(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.player.feet, 2)  # Pieds du joueur en vert
        for wall in self.walls:
            pygame.draw.rect(self.screen, (255, 0, 0), wall, 2)  # Zones de collision en rouge



    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.jump()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()

            

    def run(self):
        # boucle du jeu
        running = True
        clock = pygame.time.Clock()

        while running:
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)

            # Active le mode débogage
            #self.draw_debug()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        pygame.quit()
