import pygame
from settings import tile_size


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill("red")
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 30
        self.gravity = 0.4
        self.jump_speed = -6
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()
    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
    def appli_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump(self):
        self.direction.y = self.jump_speed
    def import_character_assets(self):
        character_path = "../grafiks/character/"
        self.animations = {
            "fall": [],
            "idle": [],
            "jump": [],
            "run": []
        }
        for animation in self.animations.keys():
            full_path = character_path + animation
