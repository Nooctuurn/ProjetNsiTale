import pygame

# Chargement des sprites
sprite_sheet_IDLE = pygame.image.load("Sprite/Ninja_Peasant/Idle.png")
sprite_sheet_RUN = pygame.image.load("Sprite/Ninja_Peasant/Run.png")
sprite_sheet_Jump = pygame.image.load("Sprite/Ninja_Peasant/Jump.png")
sprite_sheet_Dash = pygame.image.load("Sprite/Ninja_Peasant/Dash.png")


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # Découpe des frames
        self.IDLE_frame = self.extract_frames(sprite_sheet_IDLE, 6)
        self.RUN_frame = self.extract_frames(sprite_sheet_RUN, 6)
        self.Jump_frame = self.extract_frames(sprite_sheet_Jump, 8)
        self.Dash_frame = self.extract_frames(sprite_sheet_Dash, 3)

        self.animation_frame = 0
        self.image = self.IDLE_frame[self.animation_frame]
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

        #jump
        self.jump_cooldown = 825  # en millisecondes

        # Dash
        self.is_dashing = False
        self.dash_speed = 12
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
            current_frames = self.Dash_frame
            current_anim = "dash"
        elif self.is_jumping:
            current_frames = self.Jump_frame
            current_anim = "jump"
        elif self.is_moving:
            current_frames = self.RUN_frame
            current_anim = "run"
        else:
            current_frames = self.IDLE_frame
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
        animation_speed = 60 if current_anim == "dash" else (80 if self.is_moving else(120 if self.is_jumping else 120))

        if pygame.time.get_ticks() - self.last_update_time > animation_speed:
            self.animation_frame += 1
            if self.animation_frame >= len(current_frames):
                if current_anim == "jump":
                    self.animation_frame = len(current_frames) -1
                else:
                    self.animation_frame = 0
            self.last_update_time = pygame.time.get_ticks()

        self.is_moving = False
