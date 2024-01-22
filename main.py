from settings import *
from objects import *

pygame.init()

timer = pygame.time.Clock()
fps = 120
runnig = True

while runnig:

    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

        # player movement
        if event.type == KEYDOWN and not game_over:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

            # check for side collision after changing lane
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    game_over = True

                    # create crash between player and npc
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

    # drawing the grass and road
    window.fill(green)
    pygame.draw.rect(window, grey, road)
    pygame.draw.rect(window, red, left_edge)
    pygame.draw.rect(window, red, right_edge)

    # draw road markers
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

    # tree related stuff
    if len(tree_group) < 100:
        # check if there is enough space to add a new tree
        add_tree = True
        for tree in tree_group:
            if tree.rect.top < tree.rect.height * 1.5:
                add_tree = False

        if add_tree:
            x_side = random.choice(["left", "right"])
            if x_side == "left": x_position = random.randint(20, 80)
            else: x_position = random.randint(420, 480)
            tree_image = pygame.image.load("graphics/tree.png")
            tree = Tree(tree_image, x_position, height / -2)
            tree_group.add(tree)

    for tree in tree_group:
        tree.rect.y += speed * 2

        if tree.rect.top > height:
            tree.kill()

    tree_group.draw(window)

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
        speed = 0

    pygame.display.update()

pygame.quit()
