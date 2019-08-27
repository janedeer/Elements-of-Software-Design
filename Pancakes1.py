def flip(a, elem):
    i = 0
    while i < elem:
        print("i, elem: ", i, elem)
        print("a before switch: ", a)
        print("a[i] and a[elem]: ", a[i], a[elem])
        a[i], a[elem] = a[elem], a[i]
        print("new a[i], new a[elem]: ", a[i], a[elem])
        print("a after switch: ", a)
        i += 1
        elem -= 1

def getMax(a, n):
    elem = 0
    for i in range(n):
        if a[i] > a[elem]:
            elem = i
    return elem

def sortPancakes(a):
    n = len(a)
    flipped = []
    while n > 1:
        elem = getMax(a, n)
        print("elem: ", elem)
        if elem != (n - 1): # if the largest elem is not last in list
            if elem == 0:
                
            flip(a, elem)
            print("a after first flip: ", a)
            flip(a, n - 1)
            print("a after second flip: ", a)
            
        n -= 1

    return flipped
    

def main():
    a = [6, 4, 2, 3, 5, 1]
    print(a)
    print(sortPancakes(a))

main()
            
