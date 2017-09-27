'''
Created on Sep 19, 2017

@author: Kevin Ely
'''
## ----- Import Statements ----- ##
import time
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import print_path
from part3_basic_hill_climbing_approach import hill_climb
## ----- End Import Statements ----- ##


def hill_climbing_random_restart(nodes, n, number_of_iterations, number_of_restarts):
    start_time = time.time()
    best_k_value_yet = -(n*n)
    best_puzzle_yet = None
    best_visited_puzzle_yet = None
    
    for _ in range(0, number_of_restarts):
        new_nodes, new_visited, k = hill_climb(nodes, n, number_of_iterations)
        if(k > best_k_value_yet):
            print('New High Score: ')
            best_k_value_yet = k
            best_puzzle_yet = new_nodes
            best_visited_puzzle_yet = new_visited
            print_matrix(best_puzzle_yet, n)
            
        print('Creating new puzzle: ')
        nodes = generate_puzzle(n)
        print_matrix(nodes, n)
    print("--- %s seconds ---" % (time.time()-start_time))  
    
    return best_puzzle_yet, best_visited_puzzle_yet, best_k_value_yet 
## ----- End Hill Climb w Random Restart ----- ##        

'''
## ----- Hill Climb w Random Restart ----- ##
number_of_iterations = 2500 # Change to user input, N = 500
number_of_restarts = 10 # Change to user input, N = 500
## ----- Input Puzzle Size ----- ##
n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')  # need to validate
n = int(n)

## ----- End Input Puzzle Size ----- ##
nodes = generate_puzzle(n)
best_puzzle_yet, best_visited_puzzle_yet, bext_k_value_yet = hill_climbing_random_restart(nodes, n, number_of_iterations, number_of_restarts)
print()
print('Highest Value: ')
print_matrix(best_puzzle_yet, n)
print_path(best_puzzle_yet, n, best_visited_puzzle_yet)
print("End part 4")
'''