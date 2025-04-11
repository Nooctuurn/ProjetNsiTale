import pygame

sprites = {
    "ninja_peasent": {
        "idle": (pygame.image.load("Sprite/Ninja_Peasant/Idle.png"), 6),
        "run": (pygame.image.load("Sprite/Ninja_Peasant/Run.png"), 6),
        "jump": (pygame.image.load("Sprite/Ninja_Peasant/Jump.png"), 8),
        "dash": (pygame.image.load("Sprite/Ninja_Peasant/Dash.png"), 3),
    },
    "ninja_monk": {
        "idle": (pygame.image.load("Sprite/Ninja_Monk/Idle.png"),7),
        "run": (pygame.image.load("Sprite/Ninja_Monk/Run.png"), 8),
        "jump": (pygame.image.load("Sprite/Ninja_Monk/Jump.png"), 9),
        "dash": (pygame.image.load("Sprite/Ninja_Monk/Attack_1.png"), 5),
    },
}

player_selected = str(input("choisir le personnage"))  # Choix du joueur, peut être "ninja_peasent" ou "ninja_monk"

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # Découpe des frames pour chaque animation
        self.frames = {
            "idle": self.extract_frames(sprites[player_selected]["idle"][0], sprites[player_selected]["idle"][1]),
            "run": self.extract_frames(sprites[player_selected]["run"][0], sprites[player_selected]["run"][1]),
            "jump": self.extract_frames(sprites[player_selected]["jump"][0], sprites[player_selected]["jump"][1]),
            "dash": self.extract_frames(sprites[player_selected]["dash"][0], sprites[player_selected]["dash"][1]),
        }
        self.animation_frame = 0
        self.image = self.frames["idle"][self.animation_frame]
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(x, y)
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)

        self.cote = "droite"
        self.speed = 4
        self.old_position = self.position.copy()
        self.velocity_y = 0
        self.jump_strength = -7
        self.on_ground = False

        # Flags de mouvement
        self.is_jumping = False
        self.last_jump_time = 0
        self.jump_cooldown = 825  # en millisecondes

        # Dash
        self.is_dashing = False
        self.dash_speed = 8
        self.dash_duration = 180
        self.dash_cooldown = 3000
        self.last_dash_time = 0

        # État général
        self.is_moving = False
        self.current_animation = "idle"
        self.last_update_time = pygame.time.get_ticks()

    def extract_frames(self, spritesheet, num_frames):
        frame_width = spritesheet.get_width() // num_frames
        frame_height = spritesheet.get_height()
        frames = []
        for i in range(num_frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (128, 128))
            frames.append(frame)
        return frames

    def save_location(self):
        self.old_position = self.position.copy()

    def move_right(self):
        self.position[0] += self.speed
        self.cote = "droite"
        self.is_moving = True

    def move_left(self):
        self.position[0] -= self.speed
        self.cote = "gauche"
        self.is_moving = True

    def jump(self):
        now = pygame.time.get_ticks()
        if now - self.last_jump_time > self.jump_cooldown:
            self.velocity_y = self.jump_strength
            self.on_ground = False
            self.is_jumping = True
            self.last_jump_time = now

    def end_jump(self):
        self.is_jumping = False

    def dash(self):
        now = pygame.time.get_ticks()
        if self.is_moving and not self.is_dashing and now - self.last_dash_time > self.dash_cooldown:
            self.is_dashing = True
            self.dash_start_time = now
            self.last_dash_time = now

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

        if self.is_jumping and pygame.time.get_ticks() - self.last_jump_time > 800:
            self.end_jump()

        # Dash mouvement
        if self.is_dashing and self.is_moving:
            if pygame.time.get_ticks() - self.dash_start_time < self.dash_duration:
                if self.cote == "droite":
                    self.position[0] += self.dash_speed
                else:
                    self.position[0] -= self.dash_speed
            else:
                self.is_dashing = False

        # Choisir les frames et nom d'animation
        if self.is_dashing:
            current_frames = self.frames["dash"]
            current_anim = "dash"
        elif self.is_jumping:
            current_frames = self.frames["jump"]
            current_anim = "jump"
        elif self.is_moving:
            current_frames = self.frames["run"]
            current_anim = "run"
        else:
            current_frames = self.frames["idle"]
            current_anim = "idle"

        # Reset animation si changement
        if current_anim != self.current_animation:
            self.animation_frame = 0
            self.current_animation = current_anim

        # Affichage du sprite selon la direction
        if self.cote == "gauche":
            self.image = pygame.transform.flip(current_frames[self.animation_frame], True, False)
        else:
            self.image = current_frames[self.animation_frame]

        # Vitesse de l’animation
        animation_speed = 60 if current_anim == "dash" else (80 if self.is_moving else (120 if self.is_jumping else 120))

        if pygame.time.get_ticks() - self.last_update_time > animation_speed:
            self.animation_frame += 1
            if self.animation_frame >= len(current_frames):
                if current_anim == "jump":
                    self.animation_frame = len(current_frames) - 1
                else:
                    self.animation_frame = 0
            self.last_update_time = pygame.time.get_ticks()

        self.is_moving = False
