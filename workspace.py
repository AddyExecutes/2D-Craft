import shapetextimage
import json
import project
import preview


color = {}
path = {}

def refresh_json():

    global color, path

    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]
        path = data["path"]




# allowance for functions - can be controlled by foreign functions to kill the user interface ( setting the value to False )
permission_basic_workspace = False
permission_openproject = False  # default value - True, because the app will start at open / recent page
permission_newproject = False
permission_preview = True


# base workspace

def base_workspace(message: str = ""):

    from app import screen_WIDTH, screen_HEIGHT

    # coordinates
    workspace_X = 50
    workspace_Y = 70
    workspace_screen_ratio = 1.6
    workspace_W = screen_WIDTH / workspace_screen_ratio
    workspace_H = screen_HEIGHT / workspace_screen_ratio

    # workspace
    bdrRad = 2
    shapetextimage.Shape.rect(color["workspace_base"], (workspace_X, workspace_Y, workspace_W, workspace_H), borderRadius = bdrRad)

    # message
    if message != "":
        text_W = shapetextimage.Text.getWidthHeight(message)[0]
        text_H = shapetextimage.Text.getWidthHeight(message)[1]
        text_X = workspace_X + workspace_W / 2 - text_W / 2
        text_Y = workspace_Y + workspace_H / 2 - text_H / 2
        shapetextimage.Text.write(message, (text_X, text_Y), True)




# Offline workspace - No project opened
def offline_workspace():

    global permission_preview, permission_newproject, permission_openproject

    from app import screen_WIDTH, screen_HEIGHT, mx , my, leftclickdown
    import titlebar

    # coordinates
    workspace_X = 50
    workspace_Y = 70
    workspace_screen_ratio = 1.6
    workspace_W = screen_WIDTH / workspace_screen_ratio
    workspace_H = screen_HEIGHT / workspace_screen_ratio

    base_workspace("Live preview of the project is not available. Please create or open a project first")

    # image
    img_W = shapetextimage.Image.getWidthHeight(path["no_preview"])[0]
    img_H = shapetextimage.Image.getWidthHeight(path["no_preview"])[1]
    img_X = workspace_X + workspace_W / 2 - img_W / 2
    img_Y = workspace_Y + workspace_H / 2 - 60
    shapetextimage.Image.show(path["no_preview"], (img_X, img_Y))

    # create new
    cn_text = "Create new project"
    cn_text_W = shapetextimage.Text.getWidthHeight(cn_text)[0]
    cn_text_H = shapetextimage.Text.getWidthHeight(cn_text)[1]
    cn_text_X = workspace_X + workspace_W / 2 - cn_text_W / 2
    cn_text_Y = workspace_Y + workspace_H / 2 + 30

    cn_ul_start_XY = (cn_text_X, cn_text_Y + cn_text_H + 1)
    cn_ul_end_XY = (cn_text_X + cn_text_W, cn_text_Y + cn_text_H + 1)

    shapetextimage.Text.write(cn_text, (cn_text_X, cn_text_Y), textFG = color["secondary_blue"])

    # hover effect
    if mx >= cn_text_X and mx <= cn_text_X + cn_text_W and my >= cn_text_Y and my <= cn_text_Y + cn_text_H:
        shapetextimage.Shape.line(color["secondary_blue"], (cn_ul_start_XY), (cn_ul_end_XY))

        # if clicked
        if leftclickdown:
            titlebar.selected_menu_btn = "New"
            permission_preview, permission_openproject = False, False
            permission_newproject = True







    # open a project
    op_text = "Open a project"
    op_text_W = shapetextimage.Text.getWidthHeight(op_text)[0]
    op_text_H = shapetextimage.Text.getWidthHeight(op_text)[1]
    op_text_X = workspace_X + workspace_W / 2 - op_text_W / 2
    op_text_Y = cn_text_Y + 40

    op_ul_start_XY = (op_text_X, op_text_Y + op_text_H + 1)
    op_ul_end_XY = (op_text_X + op_text_W, op_text_Y + op_text_H + 1)

    shapetextimage.Text.write(op_text, (op_text_X, op_text_Y), textFG = color["secondary_blue"])

    # hover effect
    if mx >= op_text_X and mx <= op_text_X + op_text_W and my >= op_text_Y and my <= op_text_Y + op_text_H:
        shapetextimage.Shape.line(color["secondary_blue"], (op_ul_start_XY), (op_ul_end_XY))

        # if clicked
        if leftclickdown:
            titlebar.selected_menu_btn = "Open"
            permission_preview, permission_newproject = False, False
            permission_openproject = True





    
    








project_name = ""
project_path = "C:/Pancake studio/"

# Manager
class Manager:

    def parse():

        global project_name, project_path

        if permission_basic_workspace:
            base_workspace()

        if permission_openproject:
            project.open_project_gui()

        elif permission_newproject:
            project.create_gui()

        elif permission_preview:
            if project_name != "" and project_path != "":
                preview.workspace(project_name, project_path)
            else:
                offline_workspace()


refresh_json()
