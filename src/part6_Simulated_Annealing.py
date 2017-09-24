'''
Created on Sep 20, 2017

@author: Kevin and Ely
'''
## ----- Import Statements ----- ##
import random
import math
import time
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import print_path
from part2_puzzle_evaluation import BFS
## ----- End Import Statements ----- ##

## ----- Hill-Climbing w Simulated Annealing ----- ##
def hill_climb_simulated_annealing(nodes, n, iteration, temperature, decay_constant): 
    for i in range(0, iteration):
        _, oldk = BFS(nodes, n)
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
        _, newk = BFS(nodes, n)
        print('Old k value:', oldk, end = '')
        print('. New k value:', newk, end = '')
        if(newk < oldk):
            if (random.random() <= math.exp((newk - oldk) / temperature)):
                print('. Change Accepted with Simulated Annealing', '| ', temperature)
            else:
                nodes[randx][randy]['value'] = tempnode # Apply Reversion    
                print('. Change Not Accepted')
        else:
            print('. Change Accepted')
        ## ----- End Accept/Reject Change ----- ##
        temperature *= decay_constant
        
        
    newvisited, newk = BFS(nodes, n)        
    return nodes, newvisited, newk
## ----- End Hill-Climbing w Simulated Annealing ----- ##

## ----- Unit Test ----- ##
number_of_iterations = 20000
initial_temp = 100
initial_d = .7
## ----- Input Puzzle Size ----- ##
n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')  # need to validate
n = int(n)
## ----- End Input Puzzle Size ----- ##
nodes = generate_puzzle(n)
print_matrix(nodes, n)

start_time = time.time()
nodes, newvisited, newk = hill_climb_simulated_annealing(nodes, n, number_of_iterations, initial_temp, initial_d)
print("--- %s seconds ---" % (time.time()-start_time))
  
print_matrix(nodes, n)
print_path(nodes, n, newvisited)
print("End part 6")
## ----- End Unit Test ----- ##