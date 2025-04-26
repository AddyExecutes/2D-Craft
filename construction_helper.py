import shapetextimage

def grids(x_axis_count: int = 4, y_axis_count: int = 4):

    from app import screen_WIDTH, screen_HEIGHT

    x_axis_color = (100, 100, 100)
    y_axis_color = (100, 100, 100)

    for x in range(1, x_axis_count+1):
        shapetextimage.Shape.line(x_axis_color, (0, x*(screen_HEIGHT/(y_axis_count+1))), (screen_WIDTH, x*(screen_HEIGHT/(y_axis_count+1))))
    
    for y in range(1, y_axis_count+1):
        shapetextimage.Shape.line(y_axis_color, (y*(screen_WIDTH/(y_axis_count+1)), 0), (y*(screen_WIDTH/(y_axis_count+1)), screen_HEIGHT))