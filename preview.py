import shapetextimage
import json
import os
import pygame

color = {}
path = {}

def refresh_json():

    global color, path

    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]
        path = data["path"]

refresh_json()





virtual_X = 0
virtual_Y = 0

workspace_freeze = True
graph_freeze_points = [960, 540] # follows the original X and Y coordinates

permission_grids = True

def grids():

    global virtual_X, virtual_Y, workspace_freeze, graph_freeze_points

    from app import screen_WIDTH, screen_HEIGHT, mx, my, leftclickdown, rightclickdown

    # Coordinates
    workspace_X = 50
    workspace_Y = 70
    workspace_screen_ratio = 1.6
    workspace_W = screen_WIDTH / workspace_screen_ratio
    workspace_H = screen_HEIGHT / workspace_screen_ratio

    if not workspace_freeze: # if workspace is not frozen

        if mx >= workspace_X and mx <= workspace_X + workspace_W and my >= workspace_Y and my <= workspace_Y + workspace_H:

            # Hiding the cursor
            pygame.mouse.set_visible(False)

            # vertical
            vertical_start_XY = (mx, workspace_Y)
            vertical_end_XY = (mx, workspace_Y + workspace_H - 1)
            shapetextimage.Shape.line(color["graph_line"], vertical_start_XY, vertical_end_XY)

            # horizontal
            horizontal_start_XY = (workspace_X, my)
            horizontal_end_XY = (workspace_X + workspace_W - 1, my)
            shapetextimage.Shape.line(color["graph_line"], horizontal_start_XY, horizontal_end_XY)


            # showing positions
            virtual_X = int((mx - workspace_X) * workspace_screen_ratio)
            virtual_Y = int((my - workspace_Y) * workspace_screen_ratio)

            postxt = f"({str(virtual_X)}, {str(virtual_Y)})"
            postxt_X = mx + 10
            postxt_Y = my + 10
            postxt_W = shapetextimage.Text.getWidthHeight(postxt)[0]
            postxt_H = shapetextimage.Text.getWidthHeight(postxt)[1]

            posbox_X = postxt_X - 2
            posbox_Y = postxt_Y - 2
            posbox_W = postxt_W + 4
            posbox_H = postxt_H + 4
            posbox_bdr_Rad = 2
            shapetextimage.Shape.rect(color["fade_black"], (posbox_X, posbox_Y, posbox_W, posbox_H), True, borderRadius = posbox_bdr_Rad)
            shapetextimage.Text.write(postxt, (postxt_X, postxt_Y))

            # updating the graph freeze points
            graph_freeze_points = [mx, my]

            # freezing graph mechanism
            if rightclickdown:
                workspace_freeze = True
        
        else:
            pygame.mouse.set_visible(True)


    else: # if workspace is frozen

        # Unhiding the cursor
        pygame.mouse.set_visible(True)

        # vertical
        vertical_start_XY = (graph_freeze_points[0], workspace_Y)
        vertical_end_XY = (graph_freeze_points[0], workspace_Y + workspace_H - 1)
        shapetextimage.Shape.line(color["graph_line"], vertical_start_XY, vertical_end_XY)

        # horizontal
        horizontal_start_XY = (workspace_X, graph_freeze_points[1])
        horizontal_end_XY = (workspace_X + workspace_W - 1, graph_freeze_points[1])
        shapetextimage.Shape.line(color["graph_line"], horizontal_start_XY, horizontal_end_XY)

        # showing positions
        virtual_X = int((graph_freeze_points[0] - workspace_X) * workspace_screen_ratio)
        virtual_Y = int((graph_freeze_points[1] - workspace_Y) * workspace_screen_ratio)

        postxt = f"({str(virtual_X)}, {str(virtual_Y)})"
        postxt_X = graph_freeze_points[0] + 10
        postxt_Y = graph_freeze_points[1] + 10
        postxt_W = shapetextimage.Text.getWidthHeight(postxt)[0]
        postxt_H = shapetextimage.Text.getWidthHeight(postxt)[1]

        posbox_X = postxt_X - 2
        posbox_Y = postxt_Y - 2
        posbox_W = postxt_W + 4
        posbox_H = postxt_H + 4
        posbox_bdr_Rad = 2


        shapetextimage.Shape.rect(color["fade_black"], (posbox_X, posbox_Y, posbox_W, posbox_H), borderRadius = posbox_bdr_Rad)
        shapetextimage.Text.write(postxt, (postxt_X, postxt_Y))

        # unfreezing graph mechanism - only when the cursor is hovering on the workspace
        if mx >= workspace_X and mx <= workspace_X + workspace_W and my >= workspace_Y and my <= workspace_Y + workspace_H:
            if leftclickdown:
                workspace_freeze = False
        






# properties of selected window
_bg_color = []


def window_property_json(project_path, project_name, window_name):

    global _bg_color

    properties_file_path = os.path.join(project_path, project_name, "Windows", window_name) + "/properties.json"

    # json data
    with open(properties_file_path, "r") as properties_json_file:
        properties = json.load(properties_json_file)


    # background color
    _bg_color = properties["background-color"]













window_name = "Page 1"

workspace_active = True

def workspace(project_name, project_path):

    from app import screen_WIDTH, screen_HEIGHT

    # Getting properties of the window
    window_property_json(project_path, project_name, window_name)

    
    # coordinates
    workspace_X = 50
    workspace_Y = 70
    workspace_screen_ratio = 1.6
    workspace_W = screen_WIDTH / workspace_screen_ratio
    workspace_H = screen_HEIGHT / workspace_screen_ratio

    bdrRad = 2

    # preview workspace
    shapetextimage.Shape.rect(_bg_color, (workspace_X, workspace_Y, workspace_W, workspace_H), borderRadius = bdrRad)




    # grid function - always call in the last to make it stay on the top of the workspace
    if permission_grids:
        grids()
