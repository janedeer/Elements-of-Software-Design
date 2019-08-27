# checks if box1 fits in box2
# returns bool
def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

def main():

    inf = open("boxes.txt", "r")
    # first line is num of boxes
    line = inf.readline()
    line = line.strip()
    num_boxes = int(line)
    
    # create list of boxes
    box_list = []
    for i in range(num_boxes):
        line = inf.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    inf.close()

    box_list.sort()
    for box in box_list:
        print(box)
    
    sublist = []
    outer_sublist = []
    i = 0
    while i < num_boxes - 1:
        if does_fit(box_list[i], box_list[i + 1]):
            if sublist == []:
                sublist.append(box_list[i])
                sublist.append(box_list[i + 1])
            else:
                sublist.append(box_list[i + 1])
            print(sublist)
            i += 1
        else:
            i +=  1

    print(sublist)
    
            

main()
