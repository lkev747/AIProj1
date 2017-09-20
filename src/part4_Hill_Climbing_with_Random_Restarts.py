'''
Created on Sep 19, 2017

@author: Kevin Ely
'''
from part1_puzzle_representation import generate_puzzle
from part2_puzzle_evaluation import print_path


## ----- Hill Climb w Random Restart ----- ##
number_of_iterations = 50
number_of_restarts = 10
best_k_value_yet = -(n*n)
best_puzzle_yet = None

for m in range(0, number_of_restarts):
    nodes, n = generate_puzzle()
    visited, k = Hill_Climb(nodes, n, iteration)
    if(k > best_puzzle_yet):
        best_k_value_yet = k
        best_puzzle_yet = nodes
## ----- End Hill Climb w Random Restart ----- ##        

N = 500