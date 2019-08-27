# determines if letter goes into wrong envelope
# returns true if letter in position is valid (not in correct env.)
def is_valid(a):

    envelope = ["A", "B", "C", "D"]

    if a[0] == envelope[0]:
        return False
    elif a[1] == envelope[1]:
        return False
    elif a[2] == envelope[2]:
        return False
    elif a[3] == envelope[3]:
        return False

    return True

# permute, print only if position is valid
def permute(a, lo, hi):
    if lo == hi:
        if is_valid(a):
            print(a)
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i] # swap
            permute(a, lo + 1, hi) # permute a without first element
            a[i], a[lo] = a[lo], a[i] # swap back to orig. list


def main():

    lst = ["A", "B", "C", "D"]

    permute(lst, 0, 4)

main()
