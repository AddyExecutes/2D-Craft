import shapetextimage
import json

def propertyeditor():

    from app import screen_WIDTH, screen_HEIGHT

    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]
    
    # Coordinates
    propertyeditor_screen_W_ratio = 3
    propertyeditor_screen_H_ratio = 1.6
    propertyeditor_W = screen_WIDTH / propertyeditor_screen_W_ratio + 15
    propertyeditor_H = screen_HEIGHT / propertyeditor_screen_H_ratio
    propertyeditor_X = 0 + 40 + 10 + screen_WIDTH / 1.6 + 10
    propertyeditor_Y = 70

    bdrRad = 2

    # Bar
    shapetextimage.Shape.rect(color["propertyeditor"], (propertyeditor_X, propertyeditor_Y, propertyeditor_W, propertyeditor_H), borderRadius = bdrRad, border_bool = True)
