def cycleSort(a):
    writes = 0

    for i in range(len(a) - 1):
        item = a[i]
        pos = i
        num_changes = 0
        for j in range(i + 1, len(a)):
            if a[j] < item:
                pos += 1
        if pos == i:
            continue
        while item == a[pos]:
            pos += 1
            a[pos], item = item, a[pos]
            writes += 1

        while pos != i:
            pos = i
            for j in range(i + 1, len(a)):
                if a[j] < item:
                    pos += 1
            while item == a[pos]:
                pos += 1
            a[pos], item = item, a[pos]
            writes += 1

    return writes

def main():

    a = [8, 4, 6, 7, 5, 2]
    print(a)
    cycleSort(a)
    print(a)

main()
        
