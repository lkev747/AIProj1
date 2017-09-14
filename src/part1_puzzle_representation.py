'''
Created on Sep 13, 2017

@author: Kevin, Ely
'''

# Import statements
import random

# Ask user for puzzle size
# n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')
n = 5
# n = int(n)

# Generates a 2D matrix
puz = [[random.randint(1,n-1) for x in range(n)] for y in range(n)]
puz[n][n] = 0

# Print the randomly generated puzzle
for x in range(0,n):
    for y in range(0,n):
        print(puz[x][y], end = '')
    print()
        