# Description: The company that you work for is moving to a larger building. The new office is rectangular and will be subdivided into cubicles. Your employees want to request particular positions for their cubicles.
# You want to set up a system that lets them make their requests.
# see office.txt and office-3.txt for input file

# Create point class
class Point(object):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    def __eq__ (self, other):
        tol = 1.0e-16
        return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

# Create rectangle class
class Rectangle(object):

    def __init__ (self, ll_x = 0, ll_y = 0, ur_x = 1, ur_y = 1):
        if ((ll_x < ur_x) and (ll_y < ur_y)):
            self.ll = Point (ll_x, ll_y)
            self.ur = Point (ur_x, ur_y)
        else:
            self.ll = Point (0, 0)
            self.ur = Point (1, 1)

    def length(self):
        return (self.ur.x - self.ll.x)

    def width(self):
        return (self.ur.y - self.ll.y)

    def perimeter(self):
        return (2 * self.length() + 2 * self.width())

    def area(self):
        return (self.length() * self.width())

    def point_inside(self, p):
        return (self.ll.x < p.x < self.ur.x) and (self.ur.y > p.y > self.ll.y)

    def rectangle_inside (self, r):
        return self.point_inside(r.ll) and self.point_inside(r.ur)

    def rectangle_outside(self, r):
        if not self.point_inside(r.ll) and not self.point_inside(r.ur) and \
           (r.ll.y > self.ur.y or r.ll.x > self.ur.x or r.ur.y < self.ll.y or r.ur.x < self.ll.x):
            return True
        else:
            return False

    def rectangle_overlap (self, r):
        if self.ll == r.ll and self.ur == r.ur: # if they are the same
            return False
        elif not self.rectangle_inside(r) and not self.rectangle_outside(r):
            return True
        else:
            return False

    def __str__ (self):
        return "LL: " + str(self.ll) + ", UR: " + str(self.ur)

    def __eq__ (self, other):
        tol = 1.0e-16
        return (self.length() - other.length() == 0) and (self.width() - other.width() == 0)

    # finds area of overlap between two rectangles
    def overlap_area(self, r):
        if self.rectangle_overlap(r):
            return (min(self.ur.x, r.ur.x) - max(self.ll.x, r.ll.x))\
                   * (min(self.ur.y, r.ur.y) - max(self.ll.y, r.ll.y))

        
    # return unallocated, contested space, and list of contested as tuple
    # total is office space and n is list of all cubicles
    def unallocated_contested(self, total, n):
        unallocated = total
        total_contested = 0
        guaranteedList = []
        for i, r in enumerate(n):
            unallocated -= r.area()
            guaranteed = r.area()
            for j in range(i + 1, len(n)):
                contested = 0
                if r.rectangle_overlap(n[j]):
                    unallocated += r.overlap_area(n[j])
                    contested += r.overlap_area(n[j])
                elif r.rectangle_inside(n[j]):
                    contested += n[j].area()
                    unallocated += n[j].area()
                elif r.ll == n[j].ll and \
                     r.ur == n[j].ur: # if they are the same
                    contested = r.area()
                total_contested += contested
                guaranteed -= contested
            guaranteedList.append(guaranteed)
            if unallocated < 0:
                unallocated = 0
        return (unallocated, total_contested)

    # finds guaranteed space
    # takes list of all rectangles as argument
    def guaranteed(self, n):
        guaranteed = self.area()
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                if self.rectangle_outside(n[i]):
                    guaranteed = self.area()
                elif self.rectangle_overlap(n[i]):
                    guaranteed = self.area() - self.overlap_area(n[i])
                elif self.rectangle_inside(n[i]):
                    guaranteed = self.area() - n[i].area()
                elif n[i].rectangle_inside(self):
                    guaranteed = 0
        return guaranteed      
        

def main():

    inf = open("office.txt", "r")
    line = inf.readline()
    while line != "":
        coords = line.strip()
        coords = line.split()
        try: # this code is still in progress
            x = int(coords[0])
            y = int(coords[1])
            officeSpace = Rectangle(0, 0 , x, y)

            line = inf.readline()
            line = line.strip()
            num = int(line)

            names = []
            n = []
            for i in range(num):
                line = inf.readline()
                line = line.strip()
                line = line.split()
                name = line[0]
                names.append(name)
                r = Rectangle(int(line[1]), int(line[2]), int(line[3]), int(line[4]))
                n.append(r)
        
            total = officeSpace.area()
            unallocated, contested = n[0].unallocated_contested(total, n)
            print("Total ", total)
            print("Unallocated ", unallocated)
            print("Contested ", contested)

            for i, r in enumerate(n):
                print(names[i], r.guaranteed(n))

            line = inf.readline()
            print()
        except:
            break

    inf.close()
        

main()
