from graphics import *

file = open("data.txt")
rawData = file.readlines()

width = 1000
height = 200

data = []

for num in rawData:
    data.append(float(num))

w = GraphWin("Data Visualisation", width, height)

for i, num in enumerate(data):
    c = Circle(Point(((width - 25) / len(data)) * i + 35, height/2), num/2)
    c.draw(w)

w.getMouse()
