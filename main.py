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
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow =(255, 255, 0)
