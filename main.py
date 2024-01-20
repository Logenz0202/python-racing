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

# vehicle groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# player car
player = Player("graphics/player.png", player_x, player_y)
player_group.add(player)

# other cars todo: add more variety to npc cars
image_filenames = ["npc1.png", "npc2.png"]
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load("graphics/" + image_filename)
    vehicle_images.append(image)

# crash
crash = pygame.image.load("graphics/crash.png")
crash_rect = crash.get_rect()

# game loop
timer = pygame.time.Clock()
fps = 120
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

            # check for side collision after changing lane
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):

                    # todo: introduce lives
                    game_over = True

                    # create crash between player and npc
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

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

    # draw other cars
    if len(vehicle_group) < 2:

        # check if there is enough space to add a new vehicle
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False

        if add_vehicle:
            lane = random.choice(lanes)
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

    # move and draw other cars
    for vehicle in vehicle_group:
        vehicle.rect.y += speed

        # remove cars that are out of the screen
        if vehicle.rect.top > height:
            vehicle.kill()

            # increase score for each car that is safely passed
            score += 1

            # increase speed for every 5 points
            if score > 0 and score % 3 == 0:
                speed += 0.25

    # draw vehicles
    vehicle_group.draw(window)

    # display score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 20)
    window.blit(text, text_rect)

    # check for headbutt
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        game_over = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    # game over
    if game_over:
        window.blit(crash, crash_rect)
        pygame.draw.rect(window, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render("GAME OVER", True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        window.blit(text, text_rect)

        # todo set speed to 0 and disable movement
        speed = 0

    pygame.display.update()

pygame.quit()
