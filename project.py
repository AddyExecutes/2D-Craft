import shapetextimage
import json
import os




exisiting_projects_list = []



def refresh_json():

    global color, path

    # json data

    # app
    with open("database.json", "r") as app_json_file:
        app_data = json.load(app_json_file)
        color = app_data["color"]
        path = app_data["path"]






# making a new project
def create(project_name: str, save_location: str, date: str):

    global project_location_var, project_name_var

    # from workspace import permission_newproject
    import workspace
    import titlebar

    # getting today's date

    # making directories
    folder_list_1 = os.listdir(save_location)
    if project_name not in folder_list_1:
        project_path = os.path.join(save_location, project_name)
        os.mkdir(project_path)

        # new key-value pair to add
        new_data = {project_name: [date, save_location]}

        # reading the existing JSON file
        try:
            with open("Project Assets/paths.json", "r") as file:
                data = json.load(file) # Load existing dictionary
        except:
            data = {} # If file doesn't exist or is empty, start with an empty dictionary

        # updating the dictionary with the new pair
        data.update(new_data)

        # writing the updated dictionary back to the JSON file
        with open("Project Assets/paths.json", "w") as file:
            json.dump(data, file, indent = 4)


        # Closing the new project window and opening the open project window
        workspace.permission_newproject = False
        workspace.permission_openproject = True
        titlebar.selected_menu_btn = "Open"



    # if project already exists
    else:
        project_name_var = project_default_name

    print("Button is working")





# project variables
project_name_entry_active = True # default - true
project_default_name = "Untitled project"
project_name_var = project_default_name

project_location_entry_active = False
project_default_save_location = "C:/Pancake studio"
project_location_var = project_default_save_location + "/"


# create function variable
create_project_function_isCallable = True


# new project - create project gui
def create_gui():

    global project_name_entry_active, project_name_var
    global project_location_entry_active, project_location_var

    from app import screen_WIDTH, screen_HEIGHT, mx, my, leftclickdown, leftclickup, key, todays_date
    from workspace import base_workspace

    base_workspace()


    # coordinates
    workspace_X = 50
    workspace_Y = 70
    workspace_screen_ratio = 1.6
    workspace_W = screen_WIDTH / workspace_screen_ratio
    workspace_H = screen_HEIGHT / workspace_screen_ratio



    # heading - new project
    heading_X = workspace_X + 60
    heading_Y = workspace_Y + 40
    shapetextimage.Text.write("New Project", (heading_X, heading_Y), fontSize = "xl", textFG = color["font_disabled"])





    # project name
    project_name_text = "Project name :"
    project_name_entry_W = workspace_W / 2
    project_name_entry_H = 25
    project_name_entry_X = workspace_X + workspace_W / 2 - project_name_entry_W / 2
    project_name_entry_Y = workspace_Y + 70 + 50 * 1
    project_name_entry_bdrRad = 3
    

    if project_name_entry_active:
        shapetextimage.Shape.rect(color["entry_active"], (project_name_entry_X, project_name_entry_Y, project_name_entry_W, project_name_entry_H), borderWidth = 2, borderRadius = project_name_entry_bdrRad)
        # modifying input var
        if key == "backspace":
            project_name_var = project_name_var[:-1]
        elif key == "enter":...
        else:
            project_name_var += key

    else:
        shapetextimage.Shape.rect(color["entry_inactive"], (project_name_entry_X, project_name_entry_Y, project_name_entry_W, project_name_entry_H), borderWidth = 1, borderRadius = project_name_entry_bdrRad)

    # user input text
    shapetextimage.Text.write(project_name_var, (project_name_entry_X + 5, project_name_entry_Y + 4))


    project_name_X = project_name_entry_X - shapetextimage.Text.getWidthHeight(project_name_text)[0] - 20
    project_name_Y = project_name_entry_Y + 4

    # project name text
    shapetextimage.Text.write(project_name_text, (project_name_X, project_name_Y), textFG = color["font_disabled"])

    # activation and deactivation
    if mx >= project_name_entry_X and mx <= project_name_entry_X + project_name_entry_W and my >= project_name_entry_Y and my <= project_name_entry_Y + project_name_entry_H:
        # activate
        if leftclickdown:
            project_name_entry_active = True
            # deactivating others
            project_location_entry_active = False

    















    # project location
    project_location_text = "Save location :"
    project_location_entry_W = workspace_W / 2
    project_location_entry_H = 25
    project_location_entry_X = workspace_X + workspace_W / 2 - project_name_entry_W / 2
    project_location_entry_Y = workspace_Y + 70 + 50 * 2
    project_location_entry_bdrRad = 3


    if project_location_entry_active:
        shapetextimage.Shape.rect(color["entry_active"], (project_location_entry_X, project_location_entry_Y, project_location_entry_W, project_location_entry_H), borderWidth = 2, borderRadius = project_location_entry_bdrRad)
        # modifying input var
        if key == "backspace":
            project_location_var = project_location_var[:-1]
        elif key == "enter":...
        else:
            project_location_var += key

    else:
        shapetextimage.Shape.rect(color["entry_inactive"], (project_location_entry_X, project_location_entry_Y, project_location_entry_W, project_location_entry_H), borderWidth = 1, borderRadius = project_location_entry_bdrRad)

    # user input text
    shapetextimage.Text.write(project_location_var, (project_location_entry_X + 5, project_location_entry_Y + 4))


    project_location_X = project_location_entry_X - shapetextimage.Text.getWidthHeight(project_location_text)[0] - 20
    project_location_Y = project_location_entry_Y + 4

    # project location text
    shapetextimage.Text.write(project_location_text, (project_location_X, project_location_Y), textFG = color["font_disabled"])

    # activation and deactivation
    if mx >= project_location_entry_X and mx <= project_location_entry_X + project_location_entry_W and my >= project_location_entry_Y and my <= project_location_entry_Y + project_location_entry_H:
        if leftclickdown:
            # activate
            project_location_entry_active = True
            # deactivating others
            project_name_entry_active = False
    






    # Window Settings
    # Window Size (Width × Height) (Input fields - default: 800×600)
    # Resizable Window? (Checkbox: Enable/Disable window resizing)
    # Fullscreen Mode? (Checkbox: Enable/Disable full screen)
    # Background Color (Color Picker - default: White or Light Gray)


    # 2️⃣ Window Settings
    # ✅ Window Size (Width × Height) (Input fields - default: 800×600)
    # ✅ Resizable Window? (Checkbox: Enable/Disable window resizing)
    # ✅ Fullscreen Mode? (Checkbox: Enable/Disable full screen)
    # ✅ Background Color (Color Picker - default: White or Light Gray)


    # 3️⃣ UI Theme & Fonts
    # ✅ Theme (Dropdown: "Light", "Dark", "Custom")
    # ✅ Font Style (Dropdown: Default: "Inter")
    # ✅ Font Size (Slider or input field: Default: 16px)


    # 4️⃣ Initial Components (Optional)
    # (Let users start with pre-added components)
    # ✅ Predefined Templates? (Dropdown: "Basic App", "Dashboard", "Form-based App", etc.)

    # ✅ Start with a Blank Page? (Checkbox: If unchecked, allow selection of pre-added buttons, text fields, etc.)

    # 5️⃣ Functionality & Scripting Options
    # ✅ Enable Custom Scripts? (Checkbox: Allows users to add Python scripts later)
    # ✅ Event Handling Mode (Dropdown: "Basic Drag & Drop", "Advanced Scripting")


    # 6️⃣ Other Settings
    # ✅ Autosave Enabled? (Checkbox: Save progress automatically every X minutes)
    # ✅ Include Example Code? (Checkbox: Add a simple script as a starting point)


    # 💡 Final Buttons:
    # 🔘 "Create Project" (Starts with selected settings)
    # 🔘 "Cancel" (Closes the dialog without making a new project)










    # create project button
    create_project_btn_text = "Create"
    create_project_btn_W = 60
    create_project_btn_H = project_name_entry_H
    create_project_btn_X = project_name_entry_X + project_name_entry_W + 20
    create_project_btn_Y = project_name_entry_Y

    create_project_btn_text_W = shapetextimage.Text.getWidthHeight(create_project_btn_text)[0]
    create_project_btn_text_H = shapetextimage.Text.getWidthHeight(create_project_btn_text)[1]
    create_project_btn_text_X = create_project_btn_X + create_project_btn_W / 2 - create_project_btn_text_W / 2
    create_project_btn_text_Y = create_project_btn_Y + create_project_btn_H / 2 - create_project_btn_text_H / 2

    create_project_btn_bdrRad = 3

    if mx >= create_project_btn_X and mx <= create_project_btn_X + create_project_btn_W and my >= create_project_btn_Y and my <= create_project_btn_Y + create_project_btn_H:
        # binding with function
        if leftclickup:
            create(project_name_var, project_location_var, todays_date)

    shapetextimage.Shape.rect(color["secondary_blue"], (create_project_btn_X, create_project_btn_Y, create_project_btn_W, create_project_btn_H), borderRadius = create_project_btn_bdrRad)
    shapetextimage.Text.write(create_project_btn_text, (create_project_btn_text_X, create_project_btn_text_Y))












def open_project_gui():

    from app import screen_WIDTH, screen_HEIGHT, mx, my, todays_date
    from workspace import base_workspace

    base_workspace()

    # Coordinates
    workspace_X = 50
    workspace_Y = 70
    workspace_screen_ratio = 1.6
    workspace_W = screen_WIDTH / workspace_screen_ratio
    workspace_H = screen_HEIGHT / workspace_screen_ratio


    # heading - new project
    heading_X = workspace_X + 60
    heading_Y = workspace_Y + 40
    shapetextimage.Text.write("Open Project", (heading_X, heading_Y), fontSize = "xl", textFG = color["font_disabled"])



    # Checking for projects in paths.json (These files are only stored locally, files might also be non-existing as user might have removed them)
    try:
        with open("Project assets/paths.json", "r") as existing_projects_json_file:
            data = json.load(existing_projects_json_file)
            exisiting_projects_list = list(data.items())
    except:
        data = {}
        exisiting_projects_list = []


    # if there is no project
    if exisiting_projects_list == []:

        # img_X = shapetextimage.Image.getWidthHeight(path["select_img"])

        text = "No projects have been opened recently"
        text_W = shapetextimage.Text.getWidthHeight(text, True)[0]
        text_H = shapetextimage.Text.getWidthHeight(text, True)[1]
        text_X = workspace_X + workspace_W / 2 - text_W / 2
        text_Y = workspace_Y + workspace_H / 2 - text_H / 2

        shapetextimage.Text.write(text, (text_X, text_Y), True)
    
    # if there is atleast one project
    else:

        for i in range(len(exisiting_projects_list)):

            # boxes
            list_workspcae_W_ratio = 1.2
            list_W = workspace_W / list_workspcae_W_ratio
            list_H = 30
            list_X = workspace_X + workspace_W / 2 - list_W / 2
            list_Y = workspace_Y + 120 + i * list_H + i
            list_bdrRad = 3

            # text - name
            list_name_text = exisiting_projects_list[i][0]
            list_name_text_H = shapetextimage.Text.getWidthHeight(list_name_text)[1]
            list_name_text_X = list_X + 40
            list_name_text_Y = list_Y + list_H / 2 - list_name_text_H / 2

            # text - date
            list_date_text = exisiting_projects_list[i][1][0]
            list_date_text_W = shapetextimage.Text.getWidthHeight(list_date_text)[0]
            list_date_text_H = shapetextimage.Text.getWidthHeight(list_date_text)[1]
            list_date_text_X = list_X + list_W / 2 - list_date_text_W / 2
            list_date_text_Y = list_Y + list_H / 2 - list_date_text_H / 2

            # text - path
            list_path_text = exisiting_projects_list[i][1][1]
            list_path_text_W = shapetextimage.Text.getWidthHeight(list_path_text)[0]
            list_path_text_H = shapetextimage.Text.getWidthHeight(list_path_text)[1]
            list_path_text_X = list_X + list_W / 1.5
            list_path_text_Y = list_Y + list_H / 2 - list_path_text_H / 2

            # configuring the length of name text to adjust into the box
            max_name_length = 40
            if len(list_name_text) > max_name_length:
                list_name_text = list_name_text[:max_name_length] + "..."

            # configuring the length of path text to adjust into the box
            max_path_length = 50
            if len(list_path_text) > max_path_length:
                list_path_text = list_path_text[:max_path_length] + "..."

            # draw the list

            # Hover effect
            if mx >= list_X and mx <= list_X + list_W and my >= list_Y and my <= list_Y + list_H:
                shapetextimage.Shape.rect(color["secondary_blue"], (list_X, list_Y, list_W, list_H), borderRadius = list_bdrRad)




            # discarding effect on text if the project doesn't exists
            if list_name_text not in os.listdir(list_path_text):
                shapetextimage.Text.write(list_name_text, (list_name_text_X, list_name_text_Y), True, textFG = color["red"])
                shapetextimage.Text.write(list_date_text, (list_date_text_X, list_date_text_Y), True, textFG = color["red"])
                shapetextimage.Text.write(list_path_text, (list_path_text_X, list_path_text_Y), True, textFG = color["red"])
                shapetextimage.Shape.line(color["border_line"], (list_name_text_X, list_Y + list_H / 2), (list_path_text_X + list_path_text_W, list_Y + list_H / 2))

            else: # if the project exists
                shapetextimage.Text.write(list_name_text, (list_name_text_X, list_name_text_Y))
                shapetextimage.Text.write(list_date_text, (list_date_text_X, list_date_text_Y))
                shapetextimage.Text.write(list_path_text, (list_path_text_X, list_path_text_Y))























refresh_json()










