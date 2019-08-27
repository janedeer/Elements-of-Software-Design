def linear(a, h):
    for i in range(len(a)):
        idx = a[i] % len(h)
        while h[idx] != None:
            idx += 1
            if idx > (len(h) - 1):
                idx = 0
        if h[idx] == None:
            h[idx] = a[i]
        
    return h

def quadratic(a, h):
    step = 1
    for i in range(len(a)):
        idx = a[i] % len(h)
        while h[idx] != None:
            idx += step ** 2
            step += 1
            if idx > (len(h) - 1):
                idx = 0
        if h[idx] == None:
            h[idx] = a[i]
        
    return h

def double(a, h, c):
    for i in range(len(a)):
        idx = a[i] % len(h)
        while h[idx] != None:
            idx += c - (a[i] % c)
            if idx > (len(h) - 1):
                idx = 0
        if h[idx] == None:
            h[idx] = a[i]
        
    return h

def sep_chain(a, h):
    for i in range(len(a)):
        idx = a[i] % len(h)
        h[idx].append(a[i])
        
    return h

def search(h, key):
    if h[key] is not None:
        return h[key]
    else:
        return None
    
def main():

    #numOfElems = int(input("number of elements in list: ",))

    
    lst = [12, 24, 36]
    
    hashList = [None for i in range(2 * len(lst))]

    table = linear(lst, hashList)
    print(search(table, 12))

    #print(linear(lst, hashList))
    #print(quadratic(lst, hashList))
    #print(double(lst, hashList, 5))
    #print(sep_chain(lst, hashList))

    
    

main()
