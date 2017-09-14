'''
Created on Sep 13, 2017

@author: Kevin, Ely
'''

# Import statements
import random

# Ask user for puzzle size
n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')
#n = 5
n = int(n)

## ----- Generates a 2D Valid matrix ----- ##
puz = [[0 for x in range(n)] for y in range(n)]
for x in range(0, n):
    for y in range(0, n):
        for k in range(0, int((n - 1)/2) + 1):
            if(x == k or x == n - (k + 1) or y == k or y == n - (k +1)):
                puz[x][y] = random.randint(1, n - (k + 1))
puz[n-1][n-1] = 0
## ----- End Valid Matrix ----- ##

# Print the randomly generated puzzle
for x in range(0,n):
    for y in range(0,n):
        print(puz[x][y], end = '')
    print()
     
