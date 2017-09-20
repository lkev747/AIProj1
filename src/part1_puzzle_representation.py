'''
Created on Sep 13, 2017

@author: Kevin, Ely
'''

# Import statements
import random


## ----- Generate Random Puzzle ----- ##
def generate_puzzle():
    ## ----- Input Puzzle Size ----- ##
    n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')  # need to validate
    n = int(n)
    ## ----- End Input Puzzle Size ----- ##
    
    ## ----- Valid Matrix ----- ##
    puz = [[0 for x in range(n)] for y in range(n)]
    for x in range(0, n):
        for y in range(0, n):
            for k in range(0, int((n - 1)/2) + 1):
                if(x == k or x == n - (k + 1) or y == k or y == n - (k +1)):
                    puz[x][y] = random.randint(1, n - (k + 1))
    puz[n-1][n-1] = 0
    ## ----- End Valid Matrix ----- ##
    
    ## ----- Unit Tests ----- ##
    '''
    # 19 Moves - Initial Example
    puz = [[3, 2, 1, 4, 1],
           [3, 2, 1, 3, 3],
           [3, 3, 2, 1, 4],
           [3, 1, 2, 3, 3],
           [1, 4, 4, 3, 0]]
    
    n = 5
    '''
    '''
    # Pass - Value Function 5 Example
    puz = [[2, 2, 2, 4, 3],
           [2, 2, 3, 3, 3],
           [3, 3, 2, 3, 3],
           [4, 3, 2, 2, 2],
           [1, 2, 1, 4, 0],]
    
    n = 5
    '''
    '''
    # Fail - Value Function -3 Example
    puz = [[3, 3, 2, 4, 3],
           [2, 2, 2, 1, 1],
           [4, 3, 1, 3, 4],
           [2, 3, 1, 1, 3],
           [1, 1, 3, 2, 0]]
    
    n = 5
    '''
    ## ----- End Unit Tests ----- ##
    

    ## ----- Create Nodes ----- ##
    nodes = [[{} for x in range(n)] for y in range(n)] # Store each node as a dictionary
    for x in range(0,n):
        for y in range(0,n):
            nodes[x][y]['value'] = puz[x][y]
            nodes[x][y]['xcoord'] = x
            nodes[x][y]['ycoord'] = y
            nodes[x][y]['level'] = 0
    ## ----- End Create Nodes ----- ##

    return nodes, n
## ----- End Generate Random Puzzle ----- ##


## ----- Print Matrix ----- ##
def print_matrix(nodes, n):
    print('Randomly Generated Puzzle: ')
    for x in range(0,n):
        for y in range(0,n):
            print(nodes[x][y]['value'], end = '')
        print()
## ----- End Print Matrix ----- ##