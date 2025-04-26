import shapetextimage
import json


color = {}

def refresh_json():
    global color
    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]


def widgetbar():
    from app import screen_HEIGHT
    
    # Coordinates
    widgetbar_X = 0
    widgetbar_Y = 35
    widgetbar_W = 40
    widgetbar_H = screen_HEIGHT - 35

    # Bar
    shapetextimage.Shape.rect(color["widgetbar"], (widgetbar_X, widgetbar_Y, widgetbar_W, widgetbar_H))
    shapetextimage.Shape.line(color["border_line"], (widgetbar_X + widgetbar_W, widgetbar_Y), (widgetbar_X + widgetbar_W, widgetbar_Y + widgetbar_H))








refresh_json()