import pygame
import json

pygame.init()


# json data
with open("database.json", "r") as json_file:
    data = json.load(json_file)
    color = data["color"]
    path = data["path"]


# Shape, Text and Image


class Shape:

    @staticmethod
    def rect(rect_color: tuple | str | list, coordinates: tuple, border_bool: bool = False, borderWidth = 0, borderRadius = -1, top_left_radius = -1, top_right_radius = -1, bottom_left_radius = -1, bottom_right_radius = -1):
        import app
        pygame.draw.rect(app.screen, rect_color, coordinates, borderWidth, borderRadius, top_left_radius, top_right_radius, bottom_left_radius, bottom_right_radius)
        if border_bool:
            pygame.draw.rect(app.screen, color["border_line"], coordinates, 1, borderRadius, top_left_radius, top_right_radius, bottom_left_radius, bottom_right_radius)



    @staticmethod
    def line(color: tuple | str | list, startXY: tuple, endXY: tuple, width = 1):
        import app
        pygame.draw.line(app.screen, color, (startXY[0], startXY[1]), (endXY[0], endXY[1]), width)





# Font setup
fontPath = path["font"]
italic_fontPath = path["italic_font"]
bold_fontPath = path["bold_font"]

fontSize = "s"
textFG = color["font_enabled"]
textFG_disabled = color["font_disabled"]
textBG = None

small = 12
medium = 13
large = 16
xlarge = 20
xxlarge = 30

smallfont = pygame.font.Font(fontPath, small)
mediumfont = pygame.font.Font(fontPath, medium)
largefont = pygame.font.Font(fontPath, large)
xlargefont = pygame.font.Font(fontPath, xlarge)
xxlargefont = pygame.font.Font(fontPath, xxlarge)

italic_smallfont = pygame.font.Font(italic_fontPath, small)
italic_mediumfont = pygame.font.Font(italic_fontPath, medium)
italic_largefont = pygame.font.Font(italic_fontPath, large)
italic_xlargefont = pygame.font.Font(italic_fontPath, xlarge)
italic_xxlargefont = pygame.font.Font(italic_fontPath, xxlarge)

bold_smallfont = pygame.font.Font(bold_fontPath, small)
bold_mediumfont = pygame.font.Font(bold_fontPath, medium)
bold_largefont = pygame.font.Font(bold_fontPath, large)
bold_xlargefont = pygame.font.Font(bold_fontPath, xlarge)
bold_xxlargefont = pygame.font.Font(bold_fontPath, xxlarge)


# Text
class Text:

    

    @staticmethod
    def write(text: str, XY: tuple, italic: bool = False, bold: bool = False, fontSize: str = fontSize, textFG: tuple | str | list = textFG, textBG: tuple | str | list = textBG, disabled: bool = False): # font size: s, m, l, xl, xxl
        import app

        # enabled and disabled font colors
        if disabled:
            textFG = textFG_disabled


        # rendering different sizes and styles of text
        if fontSize == "s":
            if italic:
                rendered_text = italic_smallfont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_smallfont.render(text, True, textFG, textBG)
            else:
                rendered_text = smallfont.render(text, True, textFG, textBG)
        
        elif fontSize == "m":
            if italic:
                rendered_text = italic_mediumfont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_mediumfont.render(text, True, textFG, textBG)
            else:
                rendered_text = mediumfont.render(text, True, textFG, textBG)
        
        elif fontSize == "l":
            if italic:
                rendered_text = italic_largefont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_largefont.render(text, True, textFG, textBG)
            else:
                rendered_text = largefont.render(text, True, textFG, textBG)
        
        elif fontSize == "xl":
            if italic:
                rendered_text = italic_xlargefont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_xlargefont.render(text, True, textFG, textBG)
            else:
                rendered_text = xlargefont.render(text, True, textFG, textBG)
        
        elif fontSize == "xxl":
            if italic:
                rendered_text = italic_xxlargefont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_xxlargefont.render(text, True, textFG, textBG)
            else:
                rendered_text = xxlargefont.render(text, True, textFG, textBG)
        
        # Lastly, blitting the text on the screen
        app.screen.blit(rendered_text, (XY[0], XY[1]))


    @staticmethod
    def getWidthHeight(text: str, italic: bool = False, bold: bool = False, fontSize: str = fontSize): # font size: s, m, l, xl, xxl
        import app


        if fontSize == "s":
            if italic:
                rendered_text = italic_smallfont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_smallfont.render(text, True, textFG, textBG)
            else:
                rendered_text = smallfont.render(text, True, textFG, textBG)
        
        elif fontSize == "m":
            if italic:
                rendered_text = italic_mediumfont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_mediumfont.render(text, True, textFG, textBG)
            else:
                rendered_text = mediumfont.render(text, True, textFG, textBG)
        
        elif fontSize == "l":
            if italic:
                rendered_text = italic_largefont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_largefont.render(text, True, textFG, textBG)
            else:
                rendered_text = largefont.render(text, True, textFG, textBG)
        
        elif fontSize == "xl":
            if italic:
                rendered_text = italic_xlargefont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_xlargefont.render(text, True, textFG, textBG)
            else:
                rendered_text = xlargefont.render(text, True, textFG, textBG)
        
        elif fontSize == "xxl":
            if italic:
                rendered_text = italic_xxlargefont.render(text, True, textFG, textBG)
            elif bold:
                rendered_text = bold_xxlargefont.render(text, True, textFG, textBG)
            else:
                rendered_text = xxlargefont.render(text, True, textFG, textBG)
        
        text_width = rendered_text.get_width()
        text_height = rendered_text.get_height()

        return text_width, text_height



# Image
class Image:

    @staticmethod
    def show(image_path, XY: tuple, resize_bool: bool = False, resize_size: tuple = (), rotation_bool: bool = False, rotation_angle: int = 0):
        import app

        img = pygame.image.load(image_path)

        if resize_bool and resize_size != (): img = pygame.transform.scale(img, resize_size)
        if rotation_bool: img = pygame.transform.rotate(img, rotation_angle)

        app.screen.blit(img, (XY[0], XY[1]))
    
    @staticmethod
    def getWidthHeight(image_path: str):

        img = pygame.image.load(image_path)

        img_width = img.get_width()
        img_height = img.get_height()

        return img_width, img_height

