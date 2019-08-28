#  File: Work.py 

#  Description: hw 10

#  Student Name:  Melanie Sifen

#  Student UT EID:  MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/4

#  Date Last Modified: 3/4


# binary search for min v value
def binary_search(n, k):
    
    lo = 1
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        v = formula(mid, k) # mid is the v value we're testing
        if  hi == lo:
            if v < n:
                return mid + 1 # need v to be AT LEAST n
            else:
                return mid
        elif v < n: # not enough lines of code
            lo = mid + 1
        elif v > n: # working too hard/not enough sleep
            hi = mid - 1
        else:
            return mid

# applies formula for mid value
def formula(v, k):
    
    # keep going until v // k ** p == 0
    p = 0
    lines = 0
    while (v // k ** p) > 0:
        lines += (v // k ** p)
        p += 1
        
    return lines

# reads file and calls binary search function
def main():

    inf = open("work.txt", "r")
    firstline = int(inf.readline())
    for i in range(firstline): # num of test cases
        line = inf.readline()
        line = line.strip()
        line = line.split()
        n = int(line[0])
        k = int(line[1])
        print(binary_search(n, k))
        
    
main()

    
        
        
        
