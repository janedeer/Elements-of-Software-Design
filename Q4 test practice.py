def combine(a, b, lo, size):
    hi = len(a)
    if lo == hi:
        if len(b) == size and cd_valid(b) and ab_valid(b):
            print(b)
        return
    if len(b) == size and cd_valid(b) and ab_valid(b):
        print(b)
    else:
        c = b[:]
        b.append(a[lo])
        combine(a, c, lo + 1, size)
        combine(a, b, lo + 1, size)

def cd_valid(lst):
    if "c" in lst and "d" in lst:
        return False
    return True
        
def ab_valid(lst):
    if "a" in lst:
        if "b" not in lst:
            return False
    return True

def main():

    lst = ["a", "b", "c", "d", "e", "f"]
    b = []

    combine(lst, b, 0, 3)
    

main()

    
