import math
import turtle

class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y
    
  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c overlaps this circle (non-zero area of overlap)
  # but neither is completely inside the other
  # the only argument c is a Circle object
  # returns a boolean
  def circle_overlap (self, c):
    if not self.circle_inside(c) and not self.circle_outside(c) and not self.circle_intersect(c):
      return True
    else:
        return False

  def circle_outside(self, c):
    distance = self.center.dist(c.center)
    return (distance > max(self.radius, c.radius))

  def circle_intersect(self, c):
      distance = math.abs(self.center.dist(c.center))
      differenceOfRadii = self.radius - c.radius
      return distance == differenceOfRadii
      
  def __eq__(self, other):
      tol = 1.0e-16
      return abs(self.radius - other.radius) < tol

  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

  def circle_circumscribe(self, r):
    self.radius = 0.5 * math.sqrt(r.length() ** 2 + r.width() ** 2)
    self.center = (r.length() // 2, r.width() // 2)
    return str(self)
    

class Rectangle(object):

  def __init__(self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
      if ((ul_x < lr_x) and (ul_y > lr_y)):
          self.ul = Point (ul_x, ul_y)
          self.lr = Point (lr_x, lr_y)
      else:
          self.ul = Point (0, 1)
          self.lr = Point (1, 0)

  def length(self):
      return (self.lr.x - self.ul.x)
  def width(self):
      return (self.ul.y - self.lr.y)
  def perimeter(self):
      return (2 * self.length() + 2 * self.width())
  def area(self):
      return (self.length() * self.width())

  def point_inside (self, p):
      return (self.ul.x < p.x < self.lr.x) and (self.ul.y > p.y > self.lr.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    return self.point_inside(r.ul) and self.point_inside(r.lr)

  def rectangle_outside(self, r):
    if not self.point_inside(r.ul) and not self.point_inside(r.lr) and \
       (r.lr.y > self.ul.y or r.ul.x > self.lr.x or r.ul.y < self.lr.y or r.lr.x < self.ul.x):
      return True
    else:
      return False
  def rectangle_overlap(self, r):
    if not self.rectangle_inside(r) and not self.rectangle_outside(r):
      return True
    else:
      return False

  def __eq__(self, other):
    tol = 1.0e-16
    return (self.length() - other.length() == 0) and (self.width() - other.width() == 0)
    
    
def main():

 G = Rectangle(0, 10, 10, 1)
 H = Rectangle(1, 9, 8, 3)
 #print(G.rectangle_inside(H))

 officeSpace = Rectangle(0, 0, 1, 1)
 print(str(G))



main()
