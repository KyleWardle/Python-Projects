import importlib
from graphics import *
from random import randint

importlib.import_module("graphics")

canvasSize = 1000


def create_stump(window, x, y):
    stump = Rectangle(Point(x - 7, y + 20), Point(x + 7, y))
    stump.setFill("brown")
    stump.draw(window)


def create_triangle(window, x, y, size, color):
    vertices = [Point(x - (size / 2), y), Point(x, y + (size - (size / 3))), Point(x + (size / 2), y)]
    triangle = Polygon(vertices)  # Create the triangle
    triangle.setFill(color)
    triangle.draw(window)


def create_tree(window, x, y):
    create_stump(window, x, y)
    create_triangle(window, x, y + 15, 40, "green")
    create_triangle(window, x, y + 35, 30, "green")
    create_triangle(window, x, y + 55, 20, "green")


def create_background(window, sky_color, ground_color):
    sky = Rectangle(Point(canvasSize, canvasSize), Point(0, canvasSize / 3))
    sky.setFill(sky_color)
    sky.setOutline(sky_color)
    sky.draw(window)

    ground = Rectangle(Point(0, 0), Point(canvasSize, canvasSize / 3))
    ground.setFill(ground_color)
    ground.setOutline(ground_color)
    ground.draw(window)


def create_mountain(window):
    create_triangle(window, randint(0, canvasSize), (canvasSize / 3), randint(0, canvasSize / 2), "grey")


win = GraphWin(width=400, height=400)  # create a window
win.setCoords(0, 0, canvasSize,
              canvasSize)  # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)

create_background(win, "lightblue", "lightgreen")

create_mountain(win)

for a in range(1, 10):
    yCoord = (canvasSize / 3) / 10 * (10 - a)
    for b in range(1, 20):
        xCoord = randint(0, canvasSize)
        create_tree(win, xCoord, yCoord)

win.getMouse()
