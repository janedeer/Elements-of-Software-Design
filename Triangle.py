#  File: Triangle.py

#  Description: HW 16

#  Student's Name: Melanie Sifen

#  Student's UT EID: MS69768

#  Course Name: CS 313E 

#  Unique Number: 50725

#  Date Created: 4/6

#  Date Last Modified: 4/8

from timeit import timeit



def divide_conquer(grid):
    
    if len(grid) == 1:
       return grid[0][0]
    else:
        return recurse(grid, 0)
        
        
# helper function for divide and conquer
def recurse(grid, col):

    row = 0
    if row == len(grid) - 1:
        return grid[row][col]
    else:
        return grid[row][col] + \
               max(recurse(grid[1:], col), recurse(grid[1:], col + 1))


         
        
def greedy(grid):    
    idx = 0
    solution = [grid[0][0]]
    for i in range(1, len(grid)):
        if grid[i][idx] > grid[i][idx + 1]: # choose bigger
            pass
        else:
            idx += 1
        next_item = grid[i][idx]
        solution.append(next_item)
    return sum(solution)

def dynamic_prog(grid):
    all_solutions = []
    idxA = 0 # index of all_solution list
    gridcopy = grid[:] # make copy of grid in order to change it
    for i in range(len(gridcopy) - 1, 0, -1):
        idxG = 0 # index of col of grid
        solution = [] # reset solution list for each loop
        while idxG <= len(gridcopy[i]) - 2:
            if gridcopy[i][idxG] > gridcopy[i][idxG + 1]:
                solution.append(gridcopy[i][idxG]) 
            else:
                solution.append(gridcopy[i][idxG + 1])
            idxG += 1
        # add elements of solution to next row    
        solution = [solution[j] + gridcopy[i - 1][j] for j in range(len(solution))]
        all_solutions.append(solution)
        gridcopy[i - 1] = all_solutions[idxA] # replace next row with solution
        idxA += 1
    # convert list to int
    for num in all_solutions[-1]:
        num = int(num)

    return num


def main ():
    # read triangular grid from file
    inf = open("triangle.txt", "r")

    line = inf.readline()
    line = line.strip()
    num_rows = int(line)
    
    grid = []
    for i in range(num_rows):
        line = inf.readline()
        line = line.strip()
        row = line.split()
        for j in range(len(row)):
            row[j] = int(row[j])
        grid.append(row)
    
 

    


    # output greatest path from exhaustive search
    #times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
    #times = times / 10
    # print time taken using exhaustive search

    # output greatest path from greedy approach
    times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
    times = times / 10
    # print time taken using greedy approach
    print("The greatest path sum through greedy search is ", greedy(grid))
    print("The time taken for the greedy approach is ", times, "seconds.")

    # output greatest path from divide-and-conquer approach
    times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print("The greatest path sum through recursive search is ", divide_conquer(grid))
    print("The time taken for the greedy approach is ", times, "seconds.")

    # output greatest path from dynamic programming 
    times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
    times = times / 10
    # print time taken using dynamic programming
    print("The greatest path sum through dynamic programming is ", dynamic_prog(grid))
    print("The time taken for the greedy approach is ", times, "seconds.")

if __name__ == "__main__":
  main()

   

