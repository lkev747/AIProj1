'''
Created on Sep 16, 2017

@author: Kevin and Ely
'''
## ----- Import Statements ----- ##
import random
import time
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import print_path
from part2_puzzle_evaluation import BFS
## ----- End Import Statements ----- ##


## ----- Hill-Climbing ----- ##
def hill_climb(nodes, n, iteration): 
    for i in range(0, iteration):
        visited, oldk = BFS(nodes, n)
        tempnode = 0
        
        ## ----- Choose Random Cell ----- ##
        a = True
        randx = 0
        randy = 0
        while a:
            randx = random.randint(0, n - 1)
            randy = random.randint(0, n - 1)
            if not (randx == n - 1 and randy == n - 1):
                tempnode = nodes[randx][randy]['value']
                a = False
        ## ----- End Choose Random Cell ----- ##
        
        
        ## ----- Choose Random Value ----- ##
        temp = 0
        b = True
        while b:
            for k in range(0, int((n - 1)/2) + 1):
                if(randx == k or randx == n - (k + 1) or randy == k or randy == n - (k + 1)): 
                    temp = random.randint(1, n - (k + 1))
                    if temp != nodes[randx][randy]['value']:
                        nodes[randx][randy]['value'] = temp
                        b = False
                        break
        ## ----- End Choose Random Value ----- ##
        
        
        ## ----- Print Details ----- ##
        print()
        print('Next Iteration: (', randx, ',', randy, ')',  end = '')
        print(' | Old Value:', tempnode, '| New Value: ', temp)
        ## ----- End Print Details ----- ##
        
        
        ## ----- Print New Matrix ----- ##
        print('New Matrix: ')
        for x in range(0, n):
            for y in range(0, n):
                print(nodes[x][y]['value'], end = '')
            print()
        ## ----- End Print New Matrix ----- ##
        
        ## ----- Accept/Reject Change ----- ##
        newvisited, newk = BFS(nodes, n)
        print('Old k value:', oldk, end = '')
        print('. New k value:', newk, end = '')
        if(newk < oldk):
            nodes[randx][randy]['value'] = tempnode # Apply Reversion
            print('. Change Not Accepted')
        else:
            print('. Change Accepted')
        ## ----- End Accept/Reject Change ----- ##
        
        
    newvisited, newk = BFS(nodes, n)        
    return nodes, newvisited, newk
## ----- End Hill-Climbing ----- ##


## ----- Unit Test ----- ##
'''
## ----- Input Puzzle Size ----- ##
n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')  # need to validate
n = int(n)

## ----- End Input Puzzle Size ----- ##
nodes = generate_puzzle(n)
#print_matrix(nodes,n)
visited, k = BFS(nodes, n)
#print_path(nodes, n, visited)
start_time = time.time()
new_nodes, new_visited, new_k = hill_climb(nodes, n, 2500)
#print("--- %s seconds ---" % (time.time()-start_time)) 
#print_matrix(nodes, n)
#print_path(new_nodes, n, new_visited)
print(new_visited[n-1][n-1])
print("End part 3")
'''
## ----- End Unit Test ----- ##
