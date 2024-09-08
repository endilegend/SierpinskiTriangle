from math import sqrt
from random import choice

class Point():
  def __init__(self, x, y):
    self._x = x
    self._y = y

  def __str__(self):
    return f"({self._x},{self._y})"
  
  def midpt(self, other):
    x = (self._x + other._x) // 2
    y = (self._y + other._y) // 2
    return Point(x, y)
  def dist(self, other):
    return sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

NUM_POINTS = 500

p1 = Point(0, 0)
p2 = Point(24, 0)
p3 = Point(12, 21)

vertices = [ p1, p2, p3 ]

midpoints = []

def generate():
  for p in range(NUM_POINTS):
    # pick a random vertex
    v = choice(vertices)

    # the first time, pick another random vertex
    if (p == 0):
      m = choice(vertices)
      # make sure not to pick the same vertex
      while (m == v):
        m = choice(vertices)

    # calculate the midpoint
    m = v.midpt(m)
    # add the point
    midpoints.append(m)

generate()

HEIGHT = 25
WIDTH = 25

def getPlot():
  # create a blank canvas
  canvas = [ ]

  # add the rows
  for h in range(HEIGHT):
    row = [ " " ] * WIDTH
    canvas.append(row)
  # print(canvas)

  # plot the midpoints
  for m in midpoints:
    canvas[m._x][m._y] = "*"
  # plot the vertices
  for v in vertices:
    canvas[v._x][v._y] = "@"

  return canvas

def display(canvas):
  for row in canvas:
    for col in row:
      print(col, end=" ")
    print()

canvas = getPlot()
display(canvas)
