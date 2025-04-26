import shapetextimage
import json
import workspace

color = {}

def refresh_json():
    global color
    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]


selected_menu_btn = "Editor" # default value - Open, because the app will start at open / recent page

def titlebar():

    global selected_menu_btn

    from app import screen_WIDTH, mx, my, leftclickdown


    # Coordinates
    titlebar_X = 0
    titlebar_Y = 0
    titlebar_W = screen_WIDTH
    titlebar_H = 34

    # Bar
    shapetextimage.Shape.rect(color["titlebar"], (titlebar_X, titlebar_Y, titlebar_W, titlebar_H))

    shapetextimage.Shape.line(color["border_line"], (titlebar_X, titlebar_Y+titlebar_H), (titlebar_X+titlebar_W, titlebar_Y+titlebar_H))


    # Menu buttons

    menu_btn_list = ["New", "Open", "Editor", "Save", "Preview", "Settings", "Profile"]
    menu_btn_X_count = 0

    for i in range (len(menu_btn_list)):

        menu_btn_X_padding = 7

        menu_btn_W = shapetextimage.Text.getWidthHeight(menu_btn_list[i])[0] + menu_btn_X_padding * 2
        menu_btn_H = titlebar_H - 12

        if i != 0:
            menu_btn_X = menu_btn_X_count
            menu_btn_X_count = menu_btn_X + menu_btn_W + 1
        else:
            menu_btn_X = titlebar_X + 35
            menu_btn_X_count = menu_btn_X + menu_btn_W +1

        menu_btn_Y = titlebar_Y + 6

        menu_btn_bdrRad = 3

        menu_text = menu_btn_list[i]
        menu_text_W = shapetextimage.Text.getWidthHeight(menu_btn_list[i])[0]
        menu_text_H = shapetextimage.Text.getWidthHeight(menu_btn_list[i])[1]
        menu_text_X = menu_btn_X + menu_btn_W / 2 - menu_text_W / 2
        menu_text_Y = menu_btn_Y + menu_btn_H / 2 - menu_text_H / 2

        # hover effect
        if mx >= menu_btn_X and mx <= menu_btn_X + menu_btn_W and my >= menu_btn_Y and my <= menu_btn_Y + menu_btn_H:
            shapetextimage.Shape.rect(color["titlebar_button_BG"], (menu_btn_X, menu_btn_Y, menu_btn_W, menu_btn_H), borderRadius = menu_btn_bdrRad)

            # if clicked
            if leftclickdown:

                # new
                if menu_btn_list[i] == "New":
                    selected_menu_btn = "New"
                    workspace.permission_newproject = True
                    workspace.permission_openproject = False
                    workspace.permission_preview = False

                # open
                elif menu_btn_list[i] == "Open":
                    selected_menu_btn = "Open"
                    workspace.permission_openproject = True
                    workspace.permission_newproject = False
                    workspace.permission_preview = False

                # editor
                elif menu_btn_list[i] == "Editor":
                    selected_menu_btn = "Editor"
                    workspace.permission_preview = True
                    workspace.permission_newproject = False
                    workspace.permission_openproject = False

        # if selected - underlines
        if selected_menu_btn == menu_btn_list[i]:
            line_start_XY = (menu_text_X, menu_text_Y + menu_text_H + 2)
            line_end_XY = (menu_text_X + menu_text_W, menu_text_Y + menu_text_H + 2)
            line_thickness = 1
            shapetextimage.Shape.line(color["secondary_blue"], line_start_XY, line_end_XY, line_thickness)



        shapetextimage.Text.write(menu_text, (menu_text_X, menu_text_Y))

    # Resetting the X value for the menu buttons
    menu_btn_X_count = 0


refresh_json()
