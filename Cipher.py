#  File: Cipher.py

#  Description: hw 3

#  Student Name: Melanie Sifen

#  Student UT EID: MS69768

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/5/19

#  Date Last Modified: 2/9/19

import math
# this function encrypts the message
def encrypt(message):

    L = len(message)
    M = math.ceil(math.sqrt(L)) ** 2
    K = int(M ** 0.5) # side length of matrix
    numOfAsterisks = M - L

    grid = [["0"] * K for i in range(K)]
    row = 0 # inital row
    col = K - 1 # initial column
    row_change = 1  # initally row increases by 1
    col_change = 0 # initally column does not change

    for i, letter in enumerate(message):
        grid[row][col] = letter
        new_row = row + row_change
        new_col = col + col_change
        
        if new_row <= K - 1 and new_col <= K - 1:
            row = new_row
            col = new_col
        else:
            col -= 1
            row = 0

    encrypted = "".join(letter for i in grid for letter in i if letter != "0")

    return encrypted

# this function decrypts the message
def decrypt(message):

    L = len(message)
    M = math.ceil(math.sqrt(L)) ** 2
    K = int(M ** 0.5) # side length of matrix
    numOfAsterisks = M - L

    grid = [["*"] * K for i in range(K)] # create initial matrix
    row = col = 0 
    row_change = 0  
    col_change = 1
    asteriskPosition = []    
    
    for i, letter in enumerate(message): # put message into matrix
        grid[row][col] = letter
        new_row = row + row_change
        new_col = col + col_change
            
        if new_row <= K - 1 and new_col <= K - 1:
            row = new_row
            col = new_col
        else:
            col = 0
            row += 1
            
    for row in range(K): # determine the position of the asterisks
        for col in range(K):
            if grid[row][col] == "*":
                asteriskPosition.append((row, col))
                
    rotated_matrix = [["0"] * K for i in range(K)] # put asterisks into new matrix
    if asteriskPosition != []:
        for tup in asteriskPosition:
            rotated_matrix[tup[0]][tup[1]] = "*"
        

    row = K - 1
    col = 0
    row_change = -1
    col_change = 0
    for i, letter in enumerate(message): # place * in rotated matrix, then add the letters of the message
        while rotated_matrix[row][col] == "*":
            row -= 1
        rotated_matrix[row][col] = letter
        new_row = row + row_change
        new_col = col + col_change
        if 0 <= new_row and 0 <= new_col:
            row = new_row
            col = new_col
        else:
            row = K - 1
            col += 1

    
    decrypted = "".join(letter for i in rotated_matrix for letter in i if letter != "*")
    return decrypted
# main function reads the file and returns encryption and decryption 
def main():

    inf = open("encrypt.txt", "r")
    inf2 = open("decrypt.txt", "r")
    data = [line.strip() for line in inf]
    data2 = [line2.strip() for line2 in inf2]
    
    print("Encryption:")
    for i, line in enumerate(data[1::]):
        print(encrypt(line))

    print()
    print("Decryption")
    for i, line2 in enumerate(data2[1::]):
        print(decrypt(line2))

   
main()
