import importlib
importlib.import_module("graphics")
from graphics import *
from random import randint
import math

canvasSize = 1000


def createStump(window,x,y):
	stump = Rectangle(Point(x-7, y+20), Point(x+7, y))
	stump.setFill("brown")
	stump.draw(window)

def createTriangle(window,x,y,size,color):
	vertices = []
	vertices.append(Point(x-(size/2), y))
	vertices.append(Point(x, y+(size - (size/3))))
	vertices.append(Point(x+(size/2), y))
	triangle = Polygon(vertices)      # Create the triangle
	triangle.setFill(color)
	triangle.draw(window)

def createTree(window, x, y):
	createStump(window, x, y)
	createTriangle(window, x, y+15, 40, "green")
	createTriangle(window, x, y+35, 30, "green")
	createTriangle(window, x, y+55, 20, "green")

def createBackground(window, skyColor, groundColor):
	sky = Rectangle(Point(canvasSize, canvasSize), Point(0, canvasSize/3))
	sky.setFill(skyColor)
	sky.setOutline(skyColor)
	sky.draw(window)

	ground = Rectangle(Point(0, 0), Point(canvasSize, canvasSize/3))
	ground.setFill(groundColor)
	ground.setOutline(groundColor)
	ground.draw(window)

def createMountain(window):
	createTriangle(window, randint(0, canvasSize), (canvasSize/3), randint(0, canvasSize), "grey")

def createForest(window):
	for a in range(1, 10):
		yCoord = (canvasSize / 3) / 10 * (10 - a)
		for b in range(1, 20):
			xCoord =  randint(0, canvasSize)
			createTree(window, xCoord, yCoord)

def createMountains(window, mountain_count):
	for i in range(0, mountain_count):
		createMountain(window)

def createSun(window):
	sunSize = 35
	sun = Circle(Point(canvasSize + sunSize, (70 / 100) * canvasSize), sunSize)
	sun.setFill("yellow")
	sun.setOutline("yellow")
	sun.draw(window)
	return sun

def animateSun(window, sun):
	height = (70 / 100) * canvasSize
	heightLeft = (30 / 100) * canvasSize
	width = canvasSize + 70

	heightIncrement =  heightLeft / (width / 2)
	for i in range(0, width):
		time.sleep(0.01)
		if (i <= (width / 2)):
			sun.move(-1, heightIncrement)
		else:
			sun.move(-1, -heightIncrement)

	sun = createSun(window)
	animateSun(window, sun)




def createScene():
	win = GraphWin(width = 600, height = 600) # create a window
	win.setCoords(0, 0, canvasSize, canvasSize) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
	createBackground(win, "lightblue", "lightgreen")
	sun = createSun(win)
	createMountains(win, randint(2, 5))
	createForest(win)
	animateSun(win, sun)
	win.getMouse()


createScene()











#mySquare = Rectangle(Point(1, 1), Point(99, 99)) # create a rectangle from (1, 1) to (9, 9)
#mySquare.draw(win) # draw it to the window
#win.getMouse() # pause before closing
