import pygame


class Menu:
    def __init__(self, ecran=None, largeur=1200, hauteur=600, game=None):
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur
        self.game = game
        self.in_accueil_1 = True
        self.in_accueil_2 = False
        self.in_settings = False
        self.in_choix_mod = False
        self.in_smash = False
        self.in_aventure = False
        self.transition_alpha = 0
        self.in_transition = False
        self.in_fade_in = False
        self.next_screen = None
        self.is_sliding = False
        

        # Charger les images des fonds
        self.bg_menu = pygame.image.load('img/fondacceuil1.png').convert()
        self.bg_menu = pygame.transform.scale(self.bg_menu, (self.largeur, self.hauteur))

        self.bg_accueil_2 = pygame.image.load('img/fondacceuil2.png').convert()
        self.bg_accueil_2 = pygame.transform.scale(self.bg_accueil_2, (self.largeur, self.hauteur))

        self.bg_settings = pygame.image.load('img/fondsettings-smo.png').convert()
        self.bg_settings = pygame.transform.scale(self.bg_settings, (self.largeur, self.hauteur))

        self.bg_choix_mod = pygame.image.load('img/fondchosen.png').convert()
        self.bg_choix_mod = pygame.transform.scale(self.bg_choix_mod, (self.largeur, self.hauteur))

        self.bg_smash = pygame.image.load('img/fondacceuilsmash.png').convert()
        self.bg_smash = pygame.transform.scale(self.bg_smash, (self.largeur, self.hauteur))

        self.bg_aventure = pygame.image.load('img/fondaventure.png').convert()
        self.bg_aventure = pygame.transform.scale(self.bg_aventure, (self.largeur, self.hauteur))

        # Charger les images des boutons
        self.bouton_jouer = pygame.image.load('img/boutonjouer.png').convert_alpha()
        self.bouton_jouer_hover = pygame.image.load('img/boutonjouer_hover.png').convert_alpha()
        self.bouton_play = pygame.image.load('img/boutonplay1-smo.png').convert_alpha()
        self.bouton_play_hover = pygame.image.load('img/boutonplay1hover-smo.png').convert_alpha()
        self.bouton_settings = pygame.image.load('img/boutonpara-smo.png').convert_alpha()
        self.bouton_settings_hover = pygame.image.load('img/boutonparahover-smo.png').convert_alpha()
        self.bouton_back = pygame.image.load('img/boutonback-smo.png').convert_alpha()
        self.bouton_back_hover = pygame.image.load('img/boutonbackhover-smo.png').convert_alpha()
        self.bouton_choixmod_gauche = pygame.image.load('img/boutonchosengauche.png').convert_alpha()
        self.bouton_choixmod_gauche_hover = pygame.image.load('img/boutonchosengauche_hover.png').convert_alpha()
        self.bouton_choixmod_droite = pygame.image.load('img/boutonchosendroit.png').convert_alpha()
        self.bouton_choixmod_droite_hover = pygame.image.load('img/boutonchosendroit_hover.png').convert_alpha()

        # Ajuster la taille des boutons
        self.bouton_jouer = pygame.transform.scale(self.bouton_jouer, (150, 100))
        self.bouton_jouer_hover = pygame.transform.scale(self.bouton_jouer_hover, (175, 125))
        self.bouton_play = pygame.transform.scale(self.bouton_play, (150, 75))
        self.bouton_play_hover = pygame.transform.scale(self.bouton_play_hover, (150, 75))
        self.bouton_settings = pygame.transform.scale(self.bouton_settings, (150, 75))
        self.bouton_settings_hover = pygame.transform.scale(self.bouton_settings_hover, (150, 75))
        self.bouton_back = pygame.transform.scale(self.bouton_back, (85, 85))
        self.bouton_back_hover = pygame.transform.scale(self.bouton_back_hover, (85, 85))
        self.bouton_choixmod_gauche = pygame.transform.scale(self.bouton_choixmod_gauche, (600, 600))
        self.bouton_choixmod_gauche_hover = pygame.transform.scale(self.bouton_choixmod_gauche_hover, (600, 600))
        self.bouton_choixmod_droite = pygame.transform.scale(self.bouton_choixmod_droite, (600, 600))
        self.bouton_choixmod_droite_hover = pygame.transform.scale(self.bouton_choixmod_droite_hover, (600, 600))

        # Définir la position des boutons
        self.bouton_x = (self.largeur - 150) // 2
        self.bouton_y = (self.hauteur - 100) // 1.2
        self.bouton_hover_x = (self.largeur - 175) // 2
        self.bouton_hover_y = (self.hauteur - 125) // 1.18
        self.bouton_play_x = (self.largeur - 100) // 2.1
        self.bouton_play_y = (self.hauteur - 100) // 1.7
        self.bouton_settings_x = (self.largeur - 100) // 2.1
        self.bouton_settings_y = (self.hauteur - 100) // 1.3
        self.bouton_back_x = 1100
        self.bouton_back_y = 18

        # Définir les rectangles pour la détection des clics
        self.bouton_rect = pygame.Rect(self.bouton_x, self.bouton_y, 150, 100)
        self.bouton_play_rect = pygame.Rect(self.bouton_play_x, self.bouton_play_y, 150, 75)
        self.bouton_settings_rect = pygame.Rect(self.bouton_settings_x, self.bouton_settings_y, 150, 75)
        self.bouton_back_rect = pygame.Rect(self.bouton_back_x, self.bouton_back_y, 85, 85)
        self.bouton_choixmod_gauche_rect = pygame.Rect(0, 0, 600, 600)
        self.bouton_choixmod_droite_rect = pygame.Rect(600, 0, 600, 600)

        # Surface pour gérer la transition
        self.transition_surface = pygame.Surface((self.largeur, self.hauteur))
        self.transition_surface.fill((0, 0, 0))

        # Variables pour le slider de luminosité
        self.brightness = 1.0 
        self.slider_x = 340
        self.slider_y = 445
        self.slider_width = 200
        self.slider_height = 40
        self.slider_rect = pygame.Rect(self.slider_x, self.slider_y, self.slider_width, self.slider_height)
        self.slider_handle_rect = pygame.Rect(self.slider_x, self.slider_y, 20, self.slider_height)

        # Surface pour la luminosité
        self.brightness_surface = pygame.Surface((self.largeur, self.hauteur))
        self.brightness_surface.fill((0, 0, 0))

    def draw(self):
        """Affiche le menu et gère la transition."""
        

        mouse_pos = pygame.mouse.get_pos()
        if self.in_aventure:
            self.ecran.blit(self.bg_aventure, (0, 0))
            if not self.in_transition and not self.in_fade_in:
                if self.bouton_back_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_back_hover, (self.bouton_back_x, self.bouton_back_y))
                else:
                    self.ecran.blit(self.bouton_back, (self.bouton_back_x, self.bouton_back_y))
                if self.bouton_play_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_play_hover, (self.bouton_play_x, self.bouton_play_y))
                else:
                    self.ecran.blit(self.bouton_play, (self.bouton_play_x, self.bouton_play_y))
        if self.in_smash:
            self.ecran.blit(self.bg_smash, (0, 0))
            if not self.in_transition and not self.in_fade_in:
                if self.bouton_back_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_back_hover, (self.bouton_back_x, self.bouton_back_y))
                else:
                    self.ecran.blit(self.bouton_back, (self.bouton_back_x, self.bouton_back_y))
        if  self.in_choix_mod:
            self.ecran.blit(self.bg_choix_mod, (0, 0))
            if not self.in_transition and not self.in_fade_in:
                if self.bouton_choixmod_gauche_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_choixmod_gauche_hover, (0, 0))
                else:
                    self.ecran.blit(self.bouton_choixmod_gauche, (0, 0))
                if self.bouton_choixmod_droite_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_choixmod_droite_hover, (600, 0))
                else:
                    self.ecran.blit(self.bouton_choixmod_droite, (600, 0))
                if self.bouton_back_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_back_hover, (self.bouton_back_x, self.bouton_back_y))
                else:
                    self.ecran.blit(self.bouton_back, (self.bouton_back_x, self.bouton_back_y))
        if self.in_settings:
            self.ecran.blit(self.bg_settings, (0, 0))
            if not self.in_transition and not self.in_fade_in:
                if self.bouton_back_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_back_hover, (self.bouton_back_x, self.bouton_back_y))
                else:
                    self.ecran.blit(self.bouton_back, (self.bouton_back_x, self.bouton_back_y))
                # Dessiner le slider de luminosité
                pygame.draw.rect(self.ecran, (200, 173, 127), self.slider_rect)
                pygame.draw.rect(self.ecran, (91, 60, 17), self.slider_handle_rect)
        elif self.in_accueil_2:
            self.ecran.blit(self.bg_accueil_2, (0, 0))
            if not self.in_transition and not self.in_fade_in:
                if self.bouton_play_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_play_hover, (self.bouton_play_x, self.bouton_play_y))
                else:
                    self.ecran.blit(self.bouton_play, (self.bouton_play_x, self.bouton_play_y))
                if self.bouton_settings_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_settings_hover, (self.bouton_settings_x, self.bouton_settings_y))
                else:
                    self.ecran.blit(self.bouton_settings, (self.bouton_settings_x, self.bouton_settings_y))
        elif self.in_accueil_1:
            self.ecran.blit(self.bg_menu, (0, 0))
            if not self.in_transition and not self.in_fade_in:
                if self.bouton_rect.collidepoint(mouse_pos):
                    self.ecran.blit(self.bouton_jouer_hover, (self.bouton_hover_x, self.bouton_hover_y))
                else:
                    self.ecran.blit(self.bouton_jouer, (self.bouton_x, self.bouton_y))

        # Gestion de la transition
        if self.in_transition:
            self.transition_surface.set_alpha(self.transition_alpha)
            self.ecran.blit(self.transition_surface, (0, 0))
            if self.transition_alpha < 255:
                self.transition_alpha += 5
            else:
                self.in_transition = False
                if self.next_screen == "accueil_2":
                    self.in_accueil_2 = True
                    self.in_settings = False
                    self.in_accueil_1 = False
                elif self.next_screen == "settings":
                    self.in_settings = True
                    self.in_accueil_2 = False
                elif self.next_screen == "choix_mod":
                    self.in_choix_mod = True
                    self.in_accueil_2 = False
                elif self.next_screen == "smash":
                    self.in_smash = True
                    self.in_choix_mod = False
                    self.in_aventure = False
                elif self.next_screen == "aventure":
                    self.in_aventure = True
                    self.in_choix_mod = False
                    self.in_smash = False
                self.in_fade_in = True
                self.transition_alpha = 255

        # Gestion du fondu d'arrivée
        if self.in_fade_in:
            self.transition_surface.set_alpha(self.transition_alpha)
            self.ecran.blit(self.transition_surface, (0, 0))
            if self.transition_alpha > 0:
                self.transition_alpha -= 5
            else:
                self.in_fade_in = False
        # Appliquer la luminosité
        self.brightness_surface.set_alpha(int((1 - self.brightness) * 255))
        self.ecran.blit(self.brightness_surface, (0, 0))
        pygame.display.flip()  # Met à jour l'affichage
        
    def run(self):
        """Boucle principale du menu."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Arrête la boucle principale
                self.handle_event(event)
            self.draw()

    def handle_event(self, event):
        """Gère les événements du menu."""
        if event.type == pygame.QUIT:
            # Arrête proprement le programme
            pygame.quit()
            return  # Arrête proprement sans forcer la fermeture
        
        if self.in_transition or self.in_fade_in:
            return  # Désactive les événements tant que la transition n'est pas terminée
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.in_aventure:
                if self.bouton_play_rect.collidepoint(event.pos):
                    # Mettre à jour la luminosité dans Game avant de lancer le jeu
                    self.game.brightness = self.brightness
                    self.game.run()
                    return
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.in_aventure:
                if self.bouton_play_rect.collidepoint(event.pos):
                    # Lancer la boucle du jeu
                    self.game.run()
                    return
                    
            if self.in_settings:
                if self.slider_rect.collidepoint(event.pos):
                    self.is_sliding = True  # Commence à glisser
                    self.update_brightness(event.pos[0])  # Met à jour la luminosité
                elif self.in_settings and self.bouton_back_rect.collidepoint(event.pos):
                    self.in_transition = True
                    self.transition_alpha = 0
                    self.next_screen = "accueil_2"
                return

            if self.in_accueil_2:
                if self.bouton_back_rect.collidepoint(event.pos):  
                    return

                if self.bouton_play_rect.collidepoint(event.pos):
                    self.in_transition = True
                    self.transition_alpha = 0
                    self.next_screen = "choix_mod"
                elif self.bouton_settings_rect.collidepoint(event.pos):
                    self.in_transition = True
                    self.transition_alpha = 0
                    self.next_screen = "settings"

            elif self.in_choix_mod and self.bouton_back_rect.collidepoint(event.pos):
                self.in_transition = True
                self.transition_alpha = 0
                self.next_screen = "accueil_2"

            elif self.in_smash and self.bouton_back_rect.collidepoint(event.pos):
                self.in_transition = True
                self.transition_alpha = 0
                self.next_screen = "choix_mod"
            
            elif self.in_aventure and self.bouton_back_rect.collidepoint(event.pos):
                self.in_transition = True
                self.transition_alpha = 0
                self.next_screen = "choix_mod"

            elif self.in_accueil_1 and self.bouton_rect.collidepoint(event.pos):
                self.in_transition = True
                self.transition_alpha = 0
                self.next_screen = "accueil_2"

            elif self.in_choix_mod and self.bouton_choixmod_droite_rect.collidepoint(event.pos):
                    self.in_transition = True
                    self.transition_alpha = 0
                    self.next_screen = "smash"

            elif self.in_choix_mod and self.bouton_choixmod_gauche_rect.collidepoint(event.pos):
                    self.in_transition = True
                    self.transition_alpha = 0
                    self.next_screen = "aventure"

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.is_sliding:
                    self.is_sliding = False  # Arrête de glisser

            elif event.type == pygame.MOUSEMOTION:
                if self.is_sliding:  # Si l'utilisateur glisse le curseur
                    self.update_brightness(event.pos[0])  # Met à jour la luminosité

    def update_brightness(self, mouse_x):
        """Met à jour la luminosité en fonction de la position de la souris sur le slider."""
        relative_x = mouse_x - self.slider_x
        self.brightness = max(0.1, min(1.0, relative_x / self.slider_width))
        self.slider_handle_rect.x = self.slider_x + int(self.brightness * self.slider_width)