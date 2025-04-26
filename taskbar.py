import shapetextimage
import json


color = {}

def refresh_json():
    global color
    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]


def taskbar():

    from app import screen_WIDTH

    # Coordinates
    taskbar_X = 0 + 40
    taskbar_Y = 35
    taskbar_W = screen_WIDTH - 40
    taskbar_H = 25

    # Bar
    shapetextimage.Shape.rect(color["taskbar"], (taskbar_X, taskbar_Y, taskbar_W, taskbar_H))

    shapetextimage.Shape.line(color["border_line"], (taskbar_X, taskbar_Y + taskbar_H), (taskbar_X + taskbar_W, taskbar_Y + taskbar_H))

refresh_json()
