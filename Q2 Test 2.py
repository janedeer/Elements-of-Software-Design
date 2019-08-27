# permute, print only if position is valid
def permute(a, lo, hi):
    if lo == hi:
        for b in a:
            permute(b, 0, 2)
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i] # swap
            permute(a, lo + 1, hi) # permute a without first element
            a[i], a[lo] = a[lo], a[i] # swap back to orig. list

    
def main():
    
    lst = [["War and Peace", "Anna Karenina"],
           ["Magic Mountain", "Death in Venice"],
           ["Amrs and the Man", "Candida"]]

    #for book in lst:
        #permute(book, 0, 2)

    permute(lst, 0, 3)
  

main()

