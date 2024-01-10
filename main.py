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
left_edge = pygame.Rect(100, 0, marker_width, height)
right_edge = pygame.Rect(400, 0, marker_width, height)

# lane coordinates
left_lane = 150
middle_lane = 250
right_lane = 350

# lane markers animation
marker_move_y = 0

# game loop
timer = pygame.time.Clock()
fps = 60
runnig = True

while runnig:

    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

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

    pygame.display.update()

pygame.quit()
