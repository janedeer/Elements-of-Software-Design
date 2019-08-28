def permute(a, lo, hi):
    if lo == hi:
        print(a)
    else:
        for i in range(lo, hi):
            print("i, lo: ", i, lo)
            print("a[i], a[lo]: ", a[i], a[lo])
            a[i], a[lo] = a[lo], a[i] # swap
            print("new a[i], a[lo]: ", a[i], a[lo])
            permute(a, lo + 1, hi) # permute a without first element
            a[i], a[lo] = a[lo], a[i] # swap back to orig. list
            print("third a[i], a[lo]: ", a[i], a[lo])
                
                

# checks sum of row, col, or diag
# returns bool
def is_magic(i):
    return sum(i) == 34

# turns list into 2d list
def list_2d(a):
    magic = [a[i:i + 4] for i in range(0, len(a), 4)]
    return magic

        
        
    
def main():

    # n = int(input("Enter number of magic squares (2 - 20): "))

    # c = 34

    lst = [i for i in range(1, 5)]
    print("list: ", lst)

    permute(lst, 0, 4)


    

main()
    
