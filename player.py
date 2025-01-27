import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('AnimationSheet_Character.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.velocity_y = 0  # Vitesse verticale (gravité)
        self.gravity = 0.5   # Force de gravité
        self.jump_force = -10  
        self.on_ground = False  # Détecte si le joueur est au sol
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5 , 12)
        self.old_position = self.position.copy()
        self.speed = 2

    def save_location(self):
        self.old_position = self.position.copy()

    def apply_gravity(self):
        # Appliquer la gravité uniquement si le joueur n'est pas au sol
        if not self.on_ground:
            self.velocity_y += self.gravity  # Ajuste la gravité
            if self.velocity_y > 10:  # Limite la vitesse de chute
                self.velocity_y = 10
            self.position[1] += self.velocity_y



    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False

    def update(self):
        # Détection des touches pour permettre les déplacements horizontaux
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_LEFT]:
            self.move_left()

        # Mise à jour de la position et des collisions
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


    def move_back(self):
        self.position = self.old_position.copy()
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
