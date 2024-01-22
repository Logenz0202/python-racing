import pygame
from pygame.locals import *
import random

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)

        new_width = sprite.get_rect().width * 2.1
        new_height = sprite.get_rect().height * 2.1

        self.image = pygame.transform.scale(sprite, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Player(Vehicle):
    def __init__(self, sprite, x, y):
        image = pygame.image.load("graphics/white.png")
        super().__init__(image, x, y)

# player start position
player_x = 250
player_y = 400

# vehicle groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# player car
player = Player("graphics/white.png", player_x, player_y)
player_group.add(player)

# other cars
image_filenames = ["red.png", "green.png", "blue.png", "yellow.png", "orange.png", "pink.png", "black.png"]
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load("graphics/" + image_filename)
    vehicle_images.append(image)

# crash
crash = pygame.image.load("graphics/crash.png")
crash_rect = crash.get_rect()
