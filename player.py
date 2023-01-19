import pygame
from settings import tile_size
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 30
        self.gravity = 0.4
        self.jump_speed = -6
        self.facing_right = True
        self.status = "idle"
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()
    def update(self):
        self.get_input()
        self.get_status()
        self.rect.x += self.direction.x * self.speed
        self.animate()
    def appli_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump(self):
        self.direction.y = self.jump_speed
    def import_character_assets(self):

        character_path = "grafiks/character/"
        self.animations = {
            "fall": [],
            "idle": [],
            "jump": [],
            "run": []
        }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
            print(self.animations)
    def animate(self):
        animate = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animate):
            self.frame_index = 0
        image = animate[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(self.image,True,False)
    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"