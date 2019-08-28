#  Description: This program can collapse overlapping intervals into a single interval.
# Additionally, it prints the smallest set of non-intersecting intervals in ascending order of the lower end of the interval.
# The input data will be in a file called intervals.txt. 
# see test input data intvervals1-5.text

# this function collapses the intervals from main function
def collapse(myList):

    collapsed = []
    for tup in myList:
        while collapsed == []:
            collapsed.append(tup)
        last_tup = collapsed.pop()
        if last_tup[1] >= tup[0]:
            if last_tup[1] >= tup[1]:
                new_tup = last_tup
                collapsed.append(new_tup)
            else:
                new_tup = tuple([last_tup[0], tup[1]])
                collapsed.append(new_tup)
        else:
            collapsed.append(last_tup)
            collapsed.append(tup)
    return collapsed

# this function puts intervals into order by size (extra credit)
def order(myList):
    
    difference = []
    for tup in myList:
        tup_difference = [tup[1] - tup[0], tup]
        difference.append(tup_difference)
        
    ordered = sorted(difference)
    return ordered
        
        
    
# create a list of tuples from in file and call collapse function
def main():

    inf = open("intervals.txt", "r")
    data = [tuple(line.split()) for line in inf] # create list of tuples
    for line in data:
        if line == tuple():
            data.remove(line)
    data = [tuple(int(num) for num in tup) for tup in data] # change numbers from strings to integers
    sorted_data = sorted(data) # sort list of tuples
    collapsed_data = collapse(sorted_data)
    ordered_data = order(collapsed_data)
    
    print("Non-intersecting Intervals:")
    for interval in collapsed_data:
        print(interval)

    print()
    print("Non-intersecting Intervals in order of size:")
    for num in ordered_data:
        print(num[1])
    
    inf.close()


main()


        


