# Description: Manipulating basic geometry
import math

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
    distance = self.center.dist(c.center)
    differenceOfRadii = abs(self.radius - c.radius)
    return distance == differenceOfRadii
 
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribe (self, r):
    self.radius = 0.5 * math.sqrt(r.length() ** 2 + r.width() ** 2)
    self.center = (r.length() / 2 + r.ul.x, r.width() / 2 + r.lr.y)
    return str(self)

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: " + str(self.center)
 
  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return abs(self.radius - other.radius) < tol
    
class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return (self.lr.x - self.ul.x)

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return (self.ul.y - self.lr.y)
  
  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    return (2 * self.length() + 2 * self.width())
   
  # determine the area
  # takes no arguments, returns a float
  def area (self):
    return (self.length() * self.width())

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
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
  
  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
    if not self.rectangle_inside(r) and not self.rectangle_outside(r):
      return True
    else:
      return False
 
  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rectangle_circumscribe (self, c):
    self.ul.x = c.center.x - c.radius
    self.ul.y = c.center.y - c.radius
    self.lr.x = c.center.x + c.radius
    self.lr.y = c.center.y + c.radius
    return str(self)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (self.length() - other.length() == 0) and (self.width() - other.width() == 0)

def main():
  
  # open the file geom.txt
  inf = open("geom.txt" ,"r")
  
  # create Point objects P and Q
  line = inf.readline()
  line = line.strip()
  coords = line.split()
  x = float(coords[0])
  y = float(coords[1])
  P = Point(x, y)
  print("Coordinates of P: " + str(P))
  
  # print the coordinates of the points P and Q
  line = inf.readline()
  line = line.strip()
  coords = line.split()
  x = float(coords[0])
  y = float(coords[1])
  Q = Point(x, y)
  print("Coordinates of Q: " + str(Q))

  # find the distance between the points P and Q
  distance = Point.dist(P, Q)
  print("Distance between P and Q: ", distance)
 
  # create two Circle objects C and D
  line = inf.readline()
  line = line.strip()
  coords = line.split()
  radius = float (coords[0])
  x = float (coords[1])
  y = float (coords[2])
  C = Circle (radius, x, y)
  print ("Circle C: " + str(C))

  line = inf.readline()
  line = line.strip()
  coords = line.split()
  radius = float (coords[0])
  x = float (coords[1])
  y = float (coords[2])
  D = Circle (radius, x, y)
  print ("Circle D: " + str(D))

  # compute the circumference of C
  print("Circumference of C: ", + C.circumference())

  # compute the area of D
  print("Area of D: ", + D.area())

  # determine if P is strictly inside C
  if C.point_inside(P):
    print("P is inside C")
  else:
    print("P is not inside C")

  # determine if C is strictly inside D
  if D.circle_inside(C):
    print("C is inside D")
  else:
    print("C is not inside D")
    
  # determine if C and D intersect (non zero area of intersection)
  if C.circle_intersect(D):
    print("C does intersect D")
  else:
    print("C does not intersect D")

  # determine if C and D are equal (have the same radius)
  if C == D:
    print("C is equal to D")
  else:
    print("C is not equal to D")

  # create two rectangle objects G and H
  line = inf.readline()
  line = line.strip()
  coords = line.split()
  x1 = float (coords[0])
  y1 = float (coords[1])
  x2 = float (coords[2])
  y2 = float (coords[3])
  G = Rectangle (x1, y1, x2, y2)
  print ("Rectangle G: " + str(G))

  line = inf.readline()
  line = line.strip()
  coords = line.split()
  x1 = float (coords[0])
  y1 = float (coords[1])
  x2 = float (coords[2])
  y2 = float (coords[3])
  H = Rectangle (x1, y1, x2, y2)
  print ("Rectangle H: " + str(H))

  # determine the length of G (distance along x axis)
  print("Length of G: ", G.length())

  # determine the width of H (distance along y axis)
  print("Width of H: ", H.length())

  # determine the perimeter of G
  print("Perimeter of G: ", G.perimeter())

  # determine the area of H
  print("Area of H: ", H.area())

  # determine if point P is strictly inside rectangle G
  if G.point_inside(P):
    print("P is inside G")
  else:
    print("P is not inside G")
    
  # determine if rectangle G is strictly inside rectangle H
  if H.rectangle_inside(G):
    print("G is inside H")
  else:
    print("G is not inside H")

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if G.rectangle_overlap(H):
    print("G does overlap H")
  else:
    print("G does not overlap H")

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  newCircle = Circle(1, 1, 1)
  print("Circle that circumscribes G: ", newCircle.circle_circumscribe(G))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  newRectangle = Rectangle(1, 1, 1, 1)
  print("Rectangle that circumscribes D:", newRectangle.rectangle_circumscribe(D))

  # determine if the two rectangles have the same length and width
  if G == H:
    print("Rectangle G is equal to H")
  else:
    print("Rectangle G is not equal to H")

  # close the file geom.txt
  inf.close()


if __name__ == "__main__":
  main()

  
