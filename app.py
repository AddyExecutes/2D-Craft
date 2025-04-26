import pygame
import json
from datetime import date
import os

import titlebar
import taskbar
import widgetbar
import workspace
import propertyeditor
import eventeditor

import construction_helper



# date and time
todays_date = str(date.today())

# Creating the Pancake studio folder if it doesn't exist
default_title = "Pancake studio"
default_project_folder = f"C:/{default_title}/"
if not os.path.exists(default_project_folder):
    os.mkdir(default_project_folder)



# variables for foreign use
screen = None
FULLSCREEN = True
FPS = 60 # default is 60 FPS
screen_WIDTH = 1600
screen_HEIGHT = 900
xpos = 0
ypos = 0

# permission variables
permission_contruction_helper = False
permission_titlebar = True
permission_taskbar = True
permission_widgetbar = True
permission_workspace = True
permission_property_editor = True
permission_event_editor = True



# initializing the pygame module
pygame.init()

# setting up the FPS
clock = pygame.time.Clock()

# JSON file data
with open("database.json", "r") as json_file:
    json_color_data = json.load(json_file)["color"]


# window variables
def_WIDTH = 1600
def_HEIGHT = 900

running = True
theme = json_color_data["theme"] # rgb



# setting up the 
if not FULLSCREEN: screen = pygame.display.set_mode((def_WIDTH, def_HEIGHT), pygame.RESIZABLE)
else: screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(default_title)


# updating the current screen size
screen_WIDTH = pygame.display.get_window_size()[0]
screen_HEIGHT = pygame.display.get_window_size()[1]






# input variables - mouse
mx = 0
my = 0

leftclickdown = False
leftclickup = False

middleclickdown = False
middleclickup = False

scrollup = False
scrolldown = False
last_scrolled_time = 0
scroll_timeout = 100 # ms

rightclickdown = False
rightclickup = False

# input variables - keyboard
left_ctrl_pressed = False
right_ctrl_pressed = False

left_shift_pressed = False
right_shift_pressed = False

left_alt_pressed = False
right_alt_pressed = False

key = "" # recent pressed key - may also include 'backspace' and other strings which might not be suitable for the input

# event handler
def event_handler():

    # mouse
    global mx, my, rightclickdown, rightclickup, middleclickdown, middleclickup, leftclickdown, leftclickup, scrollup, scrolldown, last_scrolled_time

    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: # left
            leftclickdown = True
            leftclickup = False
        elif event.button == 2: # middle
            middleclickdown = True
            middleclickup = False
        elif event.button == 3: # right
            rightclickdown = True
            rightclickup = False
        elif event.button == 4: # scroll up
            scrollup = True
            last_scrolled_time = pygame.time.get_ticks()
        elif event.button == 5: # scroll down
            scrolldown = True
            last_scrolled_time = pygame.time.get_ticks()


    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1: # left
            leftclickup = True
            leftclickdown = False
        elif event.button == 2: # middle
            middleclickup = True
            middleclickdown = False
        elif event.button == 3: # right
            rightclickup = True
            rightclickdown = False
        


    # keyboard
    global key, left_ctrl_pressed, right_ctrl_pressed, left_shift_pressed, right_shift_pressed, left_alt_pressed, right_alt_pressed

    # keydown
    if event.type == pygame.KEYDOWN:

        # input
        if event.key == pygame.K_BACKSPACE: key = "backspace"
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: key = "enter"
        else: key = event.unicode

        # command keys
        if event.key == pygame.K_LCTRL: left_ctrl_pressed = True
        if event.key == pygame.K_RCTRL: right_ctrl_pressed = True
        
        if event.key == pygame.K_LALT: left_alt_pressed = True
        if event.key == pygame.K_RALT: right_alt_pressed = True

        if event.key == pygame.K_LSHIFT: left_shift_pressed = True
        if event.key == pygame.K_RSHIFT: right_shift_pressed = True



    # keyup
    elif event.type == pygame.KEYUP:

        # command keys
        if event.key == pygame.K_LCTRL: left_ctrl_pressed = False
        if event.key == pygame.K_RCTRL: right_ctrl_pressed = False
        
        if event.key == pygame.K_LALT: left_alt_pressed = False
        if event.key == pygame.K_RALT: right_alt_pressed = False

        if event.key == pygame.K_LSHIFT: left_shift_pressed = False
        if event.key == pygame.K_RSHIFT: right_shift_pressed = False






















# indepedant functions - loop (responsible for outside file which is independant)
def batman():

    # titlebar
    if permission_titlebar:
        titlebar.titlebar()

    # toolbar
    if permission_taskbar:
        taskbar.taskbar()

    # property editor
    if permission_property_editor:
        propertyeditor.propertyeditor()

    # event editor
    if permission_event_editor:
        eventeditor.eventeditor()

    # workspace - over event editor
    if permission_workspace:
        workspace.Manager.parse()
    
    # widgetbar - over workspace
    if permission_widgetbar:
        widgetbar.widgetbar()



    # grids
    if permission_contruction_helper:
        construction_helper.grids(4, 5)







# mainloop
while running:

    # FPS setup
    clock.tick(FPS)

    # current screen size
    screen_WIDTH = pygame.display.get_window_size()[0]
    screen_HEIGHT = pygame.display.get_window_size()[1]

    # basic theme
    screen.fill(theme)

    # event loop
    for event in pygame.event.get():

        # event dependant functions
        event_handler()

        # quitting mechanism
        if event.type == pygame.QUIT:
            running = False



    # event independant functions
    batman()

    # resetting mouse left and right buttons
    leftclickdown, leftclickup = False, False
    rightclickdown, rightclickup = False, False

    # resetting the keyboard variables
    key = ""

    # resetting values of scroll up / down
    # current_time = pygame.time.get_ticks()
    # if scrollup or scrolldown:
    #     if current_time - last_scrolled_time >= scroll_timeout:
    #         scrollup, scrolldown = False, False

    # basic update
    pygame.display.update()
