from graphics import *

file = open("data.txt")
rawData = file.readlines()

width = 1000
height = 200

data = []

def map(number, minOld, maxOld, minNew, maxNew):
    deltaOld = maxOld - minOld
    deltaNew = maxNew - minNew
    ratio = deltaNew / deltaOld
    return ratio * number


for num in rawData:
    data.append(float(num))

print map (3, min(data), max(data), 0, 255)

w = GraphWin("Data Visualisation", width, height)

xOffset = width/len(data)

for i, num in enumerate(data):
    c = Circle(Point(xOffset + xOffset * i, height/2), 25)
    b = int(map(data[i], min(data), max(data), 0, 255))
    color = color_rgb(b, b, b)
    c.setFill(color)
    c.setOutline(color)

    c.draw(w)

w.getMouse()

