'''
Created on Sep 16, 2017

@author: Kevin and Ely
'''
## ----- Import Statements ----- ##
import random
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import BFS
## ----- End Import Statements ----- ##


## ----- Hill-Climbing ----- ##
def hill_climb(nodes, n, iteration): # must return new_puzzle, new_visited, new_k
    for i in range(0, iteration):
        visited, k = BFS(nodes, n)
        oldk = visited[n-1][n-1]
        tempnode = 0
        
        ## ----- Choose Random Cell ----- ##
        a = True
        randx = 0
        randy = 0
        while a:
            randx = random.randint(0, n - 1)
            randy = random.randint(0, n - 1)
            if randx != n-1 and randy != n-1:
                tempnode = nodes[randx][randy]['value']
                a = False
        ## ----- End Choose Random Cell ----- ##
        
        print()
        print('Next Iteration: (', randx, end = '')
        print(',', randy, ')',  end = '')
        print('. Old node:', tempnode, end = '')
        
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
        
        print('. New node: ', temp)
        print('New Matrix: ')
        
        ## ----- Print New Matrix ----- ##
        for x in range(0, n):
            for y in range(0, n):
                print(nodes[x][y]['value'], end = '')
            print()
        ## ----- End Print New Matrix -----##
        
        newvisited, k = BFS(nodes, n)
        newk = newvisited[n-1][n-1]
        print('Old k value:', oldk, end = '')
        print('. New k value:', newk, end = '')
        if(newk < oldk):
            nodes[randx][randy]['value'] = tempnode
            print('. Change Not Accepted')
        else:
            print('. Change Accepted')


nodes, n = generate_puzzle()
print_matrix(nodes,n)
hill_climb(nodes, n, 50)
