#  File: Spiral.py

#  Description: hw 1

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 1/30/19

#  Date Last Modified: 2/1/19


# this function creates the spiral matrix and calls functions to find adjacent elements and sum them
def spiral(dim, value):

    matrix = [[0]* dim for i in range(dim)]
    row_change = 0 # initally row does not change
    col_change = -1 # initally column decreases by 1
    row = 0 # initial row position
    col = dim - 1 # inital column position
    num = dim ** 2 # start value
    
    for i in range(num):
            
        matrix[row][col] = num
        newrow = row + row_change
        newcol = col + col_change

        if num == value:
            adjacents = getAdjacent(row, col, dim) # this contains the list of adjacent coordinates for our value
            
        num -= 1
        
        if 0 <= newrow < dim and 0 <= newcol < dim and matrix[newrow][newcol] == 0:
            # the new row and new column must have ranges [0,dim)
            # if matrix[newrow][newcol] == 0, then the position has not yet been filled
            row = newrow
            col = newcol

        else:
            row_change, col_change = -col_change, row_change # swap values to change directions of row and column
            row += row_change
            col += col_change

    value_sum = sumAdjacent(matrix, adjacents) # call function to sum adjacent numbers
    
    return value_sum

# this function finds the adjacent elements of each desired value in the spiral matrix and saves the coordinates as a list
def getAdjacent(row, col, dim):
    
    adjacent = []
    if row > 0:
        adjacent.append((row - 1, col))
        if col + 1 < dim:
            adjacent.append((row - 1, col + 1))
        if col > 0:
            adjacent.append((row - 1, col - 1))
    if row + 1 < dim:
        adjacent.append((row + 1, col))
        if col > 0:
            adjacent.append((row + 1, col - 1))
        if col + 1 < dim:
            adjacent.append((row + 1, col + 1))
    if col > 0:
        adjacent.append((row, col - 1))
    if col + 1 < dim:
        adjacent.append((row, col + 1))
        
    return adjacent

# this function sums the adjacent elements    
def sumAdjacent(matrix, listOfAdjacents):

    total = 0

    for position in listOfAdjacents:
        row = position[0]
        col = position[1]
        value = matrix[row][col]
        total += value

    return total
    

    
# main program reads in file and calls functions to produce desired output  
def main():

    inf = open("spiral.txt", "r")
    data = [int(num) for num in inf]
    dimension = int(data[0])

    for num in data[1:]:
        value = num
        matrix = spiral(dimension, num)
        print(matrix)

    inf.close()
    
    
main()


            
                    
        
        
        
        
        
