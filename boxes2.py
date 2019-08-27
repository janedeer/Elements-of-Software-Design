# checks if box1 fits in box2
# returns bool
def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

# box list as argument
# returns bool
def boxes_fit(a):
    fit = True
    for i in range (len(a) - 1):
        fit = does_fit(a[i], a[i+1])
        if fit == False:
            return fit
    return fit
 
def subsets(a, b, idxA):
    lst = []
    hi = len(a)
    if idxA == hi:
        if len(b) >= 2:
            lst.append(b)
    else:
        c = b[:]
        b.append(a[idxA])
        if boxes_fit(b):
            subsets(a, b, idxA + 1)
        elif boxes_fit(c):
            subsets(a, c, idxA + 1)
        else:
            idxA += 1

    largest = 0
    sub = []
    for i in range(len(lst)):
        if len(lst[i]) > largest:
            largest = len(lst[i])
        elif len(lst[i]) == largest:
            for j in range(len(lst[i])):
                sub.append(lst[i][j])
    return largest, sub

def main():
  
    inf = open('boxes.txt', 'r')
    line = inf.readline()
    line = line.strip()
    num_boxes = int(line)

    # empty list of boxes
    box_list = []
  
    # add all the boxes to the box_list
    for i in range (num_boxes):
        line = inf.readline()
        line = line.strip()
        box = line.split()
        for i in range (len(box)):
            box[i] = int(box[i])
        box.sort()
        box_list.append(box)

    inf.close()
    
    box_list.sort()
    b = []
    largest, sub = subsets(box_list, b, 0)
    if largest == 0:
        print('No Nesting Boxes')
    else:
        print('Largest Subset of Nesting Boxes')
        print(sub, end = "\n")
        print()


main()
