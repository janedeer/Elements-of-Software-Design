from itertools import combinations

# all combinations of 16 choose 4 = 34
# returns list of all valid row, col, diag for 4x4 magic square
def is_subset(a):

    valid = []
    comb = combinations(a, 4)
    for i in list(comb):
        if sum(i) == 34:
            valid.append(list(i))

    b = list_2d(a)

    return all(item in valid for item in a)

    

def permute(a, lo):
    hi = len(a)
    if lo == hi:
        print(a)
    elif lo == 2 and (a[0] + a[1] + a[2] + a[3] == 34):
        pass
    elif lo == 3 and (a[0] + a[1] + a[2] + a[3] == 34):
        pass
    elif lo == 4 and (a[0] + a[1] + a[2] + a[3] == 34):
        pass
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i] # swap
            permute(a, lo + 1)# permute a without first element
            a[i], a[lo] = a[lo], a[i] # swap back to orig. list
        
            


# checks sum of row, col, or diag
# returns bool
def is_magic(a):

    b = list_2d(a)

    diag_sum = 0
    row_sum = 0
    col_sum = 0
    for i in range(4):
        diag_sum = diag_sum + b[i][i]
        row_sum = 0 # reset sum for each sublist
        col_sum = 0 # reset sum for each sublist
        for j in range(4):
            row_sum += b[i][j]
            col_sum += b[j][i]
        if row_sum != 34:
            return False
        elif col_sum != 34:
            return False
    if diag_sum != 34:
        return False
        
    return True
            
# turns list into 2d list
def list_2d(a):
    b = [a[i:i + 4] for i in range(0, len(a), 4)]
    return b
        
    
def main():

    # n = int(input("Enter number of magic squares (2 - 20): "))

    # c = 34

    lst = [i for i in range(1, 17)]

    results = []
    permute(lst, 0)
    

main()

    

    


    
