import pygame
from pygame.locals import *
import random

# window
width = 500
height = 500
window_size = (width, height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Szymon Ligenza - Python Project - 01.2024")

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
