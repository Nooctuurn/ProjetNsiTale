import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('AnimationSheet_Character.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        #self.rect_camera = self.image.get_rect()*2
        self.position = [x, y]
        self.velocity_y = 0
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5 , 12)
        self.position = pygame.Vector2(x, y)
        self.gravity = 0.3  # Force de gravité
        self.jump_strength = -7
        self.on_ground = False  # Est-ce que le joueur est au sol ?
        self.old_position = self.position.copy()
        self.speed = 4
    '''
    def move_cam(self):
        self.rect_camera
    '''

    def save_location(self):
        self.old_position = self.position.copy()

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def jump(self):
        """Permet de sauter uniquement si le joueur est au sol"""
        if self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False  # Désactive le double saut

    def update(self):
        """Met à jour la position et les collisions"""
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        #self.apply_gravity()

    def move_back(self):
        """Annule le dernier mouvement en cas de collision"""
        self.position = self.old_position.copy()
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
