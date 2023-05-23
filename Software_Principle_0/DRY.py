# DRY(Don't Repeat Yourself)

def calculate_area_of_rectangle(width, height):
    area = width * height
    print("Alan:", area)


def calculate_area_of_square(side_length):
    area = side_length * side_length
    print("Alan:", area)


def calculate_area(shape, *args):
    if shape == "rectangle":
        width, height = args
        area = width * height
    elif shape == "square":
        side_length = args[0]
        area = side_length * side_length
    else:
        area = 0

    print("Alan:", area)

calculate_area("rectangle", 5, 10)
calculate_area("square", 4)
