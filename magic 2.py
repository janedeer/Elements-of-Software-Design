
def permute(a, lo, hi):
    if lo == hi:
        print(a)
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i] # swap
            permute(a, lo + 1, hi) # permute a without first element
            a[i], a[lo] = a[lo], a[i] # swap back to orig. list                
                
def sub_sets(a, b, idxA):
    if idxA  == len(a):
        if len(b) == 4:
            print(b)
    else:
        c = b[:]
        b.append(a[idxA])
        sub_sets(a, b, idxA)
        sub_sets(a, c, idxA)
        
            
    

# turns list into 2d list
def list_2d(a):
    magic = [a[i:i + 4] for i in range(0, len(a), 4)]
    return magic

        
def main():

    # n = int(input("Enter number of magic squares (2 - 20): "))

    # c = 34
    
    n = 16 # 3 by 3 magic square, num of elems is 9
    a = [i for i in range(1, n + 1)] # list of 1-9

    #permute(a, 0, 9) # first elem, last elem
    b = []
    print(sub_sets(a, b, 0))

    


    

main()
    
