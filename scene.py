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
	return sky

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

def createMoon(window):
	moonSize = 35
	moon = Circle(Point(canvasSize + moonSize, (70 / 100) * canvasSize), moonSize)
	moon.setFill("white")
	moon.setOutline("black")
	moon.draw(window)
	return moon

def calculateYCoord(xCoord):
	return 200 - math.sqrt((-xCoord ** 2) + (1000 * xCoord) + 240000)

def diff(c1, c2):
	return c2 - c1

def animateSun(window, sun, moon, background):
	colorArray = {
		1 : "#070605",
		100 : "#ff3f00",
		200 : "#ffc700",
		300 : "lightblue",
		400 : "lightblue",
		500 : "lightblue",
		600 : "lightblue",
		700 : "lightblue",
		800 : "#ffc700",
		900 : "#ff3f00",
		1000 : "#070605"
	}

	background.setFill("lightblue")
	xCoord = canvasSize + 35
	height = (70 / 100) * canvasSize
	heightLeft = (30 / 100) * canvasSize
	width = canvasSize + 70

	heightIncrement =  heightLeft / (width / 2)
	for i in range(0, width):
		if i in colorArray:
			background.setFill(colorArray[i])

		time.sleep(0.01)
		oldX = xCoord
		xCoord = xCoord - 1

		xDiff = diff(oldX, xCoord)
		yDiff = diff(calculateYCoord(oldX), calculateYCoord(xCoord))

		sun.move(xDiff, -yDiff)

	sun.move(width, 0)
	animateMoon(window, moon, sun, background)

def animateMoon(window, moon, sun, background):
	background.setFill("black")
	xCoord = canvasSize + 35
	height = (70 / 100) * canvasSize
	heightLeft = (30 / 100) * canvasSize
	width = canvasSize + 70

	heightIncrement =  heightLeft / (width / 2)
	for i in range(0, width):
		time.sleep(0.01)
		oldX = xCoord
		xCoord = xCoord - 1

		xDiff = diff(oldX, xCoord)
		yDiff = diff(calculateYCoord(oldX), calculateYCoord(xCoord))

		print(calculateYCoord(oldX))
		moon.move(xDiff, -yDiff)

	moon.move(width, 0)
	animateSun(window, sun, moon, background)




def createScene():
	win = GraphWin(width = 600, height = 600) # create a window
	win.setCoords(0, 0, canvasSize, canvasSize) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
	background = createBackground(win, "black", "lightgreen")
	sun = createSun(win)
	moon = createMoon(win)
	createMountains(win, randint(2, 5))
	createForest(win)
	animateSun(win, sun, moon, background)
	win.getMouse()


createScene()

#mySquare = Rectangle(Point(1, 1), Point(99, 99)) # create a rectangle from (1, 1) to (9, 9)
#mySquare.draw(win) # draw it to the window
#win.getMouse() # pause before closing
