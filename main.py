import pygame
from pygame.locals import *
import random

pygame.init()

# window
width = 500
height = 500
window_size = (width, height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pro Racer")

# colors
red = (236, 45, 61)
green = (115, 173, 1)
blue = (53, 40, 215)
yellow =(255, 216, 0)

white = (255, 255, 255)
black = (0, 0, 0)
grey = (160, 160, 160)

# game settings
game_over = False
speed = 2
score = 0

# road markers size
marker_width = 10
marker_height = 40

# road and edges
road = pygame.Rect(100, 0, 300, height)
left_edge = pygame.Rect(95, 0, marker_width, height)
right_edge = pygame.Rect(395, 0, marker_width, height)

# lane coordinates
left_lane = 150
middle_lane = 250
right_lane = 350
lanes = [left_lane, middle_lane, right_lane]

# lane markers animation
marker_move_y = 0

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)

        sprite_scale = 100 / sprite.get_rect().height
        new_width = sprite.get_rect().width * sprite_scale
        new_height = sprite.get_rect().height * sprite_scale

        self.image = pygame.transform.scale(sprite, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Player(Vehicle):
    def __init__(self, sprite, x, y):
        image = pygame.image.load("graphics/player.png")
        super().__init__(image, x, y)

# player start position
player_x = 250
player_y = 400

# player car
player_group = pygame.sprite.Group()
player = Player("graphics/player.png", player_x, player_y)
player_group.add(player)

# game loop
timer = pygame.time.Clock()
fps = 100
runnig = True

while runnig:

    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

        # player movement
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

    # drawing the track
    window.fill(green)

    pygame.draw.rect(window, grey, road)

    pygame.draw.rect(window, red, left_edge)
    pygame.draw.rect(window, red, right_edge)

    marker_move_y += speed * 2
    if marker_move_y >= marker_height * 2:
        marker_move_y = 0

    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(window, white, (left_lane + 45, y + marker_move_y, marker_width, marker_height))
        pygame.draw.rect(window, white, (middle_lane + 45, y + marker_move_y, marker_width, marker_height))

    # draw player car
    player_group.draw(window)

    pygame.display.update()

pygame.quit()
