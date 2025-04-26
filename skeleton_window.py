import pygame
import json

skeleton_permission = True

def parent_function():

    global skeleton_permission

    pygame.init()


    # JSON file data
    with open("database.json", "r") as json_file:
        color = json.load(json_file)["color"]

    # Screen setup
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    theme = color["theme"]

    # Set up title of the window
    pygame.display.set_caption("Skeleton window")

    while skeleton_permission:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                skeleton_permission = False

        # Fill the screen with a color (in this case, black)
        screen.fill(theme)

        # Update the display
        pygame.display.update()
