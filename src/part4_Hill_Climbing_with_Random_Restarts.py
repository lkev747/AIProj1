'''
Created on Sep 19, 2017

@author: Kevin Ely
'''
## ----- Import Statements ----- ##
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import print_path
from part3_basic_hill_climbing_approach import hill_climb
## ----- End Import Statements ----- ##



## ----- Hill Climb w Random Restart ----- ##
number_of_iterations = 50 # Change to user input, N = 500
number_of_restarts = 10 # Change to user input, N = 500
n = 5 # Change to user input

best_k_value_yet = -(n*n)
best_puzzle_yet = None
best_visited_puzzle_yet = None

for m in range(0, number_of_restarts):
    print('Creating new puzzle: ')
    nodes, n = generate_puzzle()
    print_matrix(nodes, n)
    
    new_nodes, new_visited, k = hill_climb(nodes, n, number_of_iterations)
    if(k > best_k_value_yet):
        print('New High Score: ')
        best_k_value_yet = k
        best_puzzle_yet = new_nodes
        best_visited_puzzle_yet = new_visited
        print_matrix(best_puzzle_yet, n)

## ----- End Hill Climb w Random Restart ----- ##        

print()
print('Highest Value: ')
print_matrix(best_puzzle_yet, n)
print_path(best_puzzle_yet, n, best_visited_puzzle_yet)
