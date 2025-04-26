import shapetextimage
import json

def eventeditor():

    from app import screen_WIDTH, screen_HEIGHT

    # json data
    with open("database.json", "r") as json_file:
        data = json.load(json_file)
        color = data["color"]
    
    # Coordinates
    eventeditor_W = screen_WIDTH - 40
    eventeditor_H = screen_HEIGHT - 34 - 25 - 10 - (screen_HEIGHT / 1.6) - 10
    eventeditor_X = 40 + 0
    eventeditor_Y = 0 + 34 + 25 + 10 + screen_HEIGHT / 1.6 + 10

    # Bar
    shapetextimage.Shape.rect(color["eventeditor"], (eventeditor_X, eventeditor_Y, eventeditor_W, eventeditor_H), border_bool = True)
