'''
Created on Sep 19, 2017

@author: Kevin Ely
'''
## ----- Import Statements ----- ##
from part1_puzzle_representation import generate_puzzle
# import hillclimb
## ----- End Import Statements ----- ##

## ----- Hill Climb w Random Restart ----- ##
number_of_iterations = 50
number_of_restarts = 10
best_k_value_yet = -(n*n)
best_puzzle_yet = None
best_visited_puzzle_yet = None

for m in range(0, number_of_restarts):
    nodes, n = generate_puzzle()
    new_nodes, new_visited, k = hill_climb(nodes, n, iteration)
    if(k > best_k_value_yet):
        best_k_value_yet = k
        best_puzzle_yet = new_nodes
        best_visited_puzzle_yet = new_visited
## ----- End Hill Climb w Random Restart ----- ##        

N = 500