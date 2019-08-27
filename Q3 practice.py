def permute (a, lo, hi):
    if (lo == hi):
        if ab_valid(a) and cd_valid(a):
            print(a)
    else:
        for i in range (lo, hi):
            a[i], a[lo] = a[lo], a[i]
            permute (a, lo + 1, hi)
            a[i], a[lo] = a[lo], a[i]

      
def ab_valid(a):
    for i in range(len(a) - 1):
        if ((a[i] == "a") and (a[i + 1] == "b")) or \
           ((a[i] == "b") and (a[i + 1] == "a")):
            return True
    return False

def cd_valid(a):
    for i in range(len(a) - 1):
        if (a[i] == "c") and (a[i + 1] == "d"):
            return False
        elif (a[i] == "d") and (a[i + 1] == "c"):
            return False
    return True
        
        
    
def main():

    a = ["a", "b", "c", "d", "e"]

    permute(a, 0, 5)
    
main()
