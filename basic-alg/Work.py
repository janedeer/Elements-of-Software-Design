# Background: Vyasa has to complete a programming assignment overnight. 
# This is how he plans to write the program. He will write the first v lines of code, then drink his first cup of coffee. Since his productivity has gone down by a factor of k he will write v // k lines of code. He will have another cup of coffee and then write v // k**2 lines of code. He will have another cup of coffee and write v // k**3 lines of code and so on. He will collapse and fall asleep when v // k ** p becomes 0.
# Now Vyasa does want to complete his assignment and maximize on his sleep. So he wants to figure out the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines of code before he falls asleep.
# see input file work.txt

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

    
        
        
        
