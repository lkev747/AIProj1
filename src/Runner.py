'''
Created on Sep 25, 2017

@author: Kevin, Ely
'''

## ----- Import Statements ----- ##
import time
import csv
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import BFS
from part2_puzzle_evaluation import print_path
from part3_basic_hill_climbing_approach import hill_climb
from part4_Hill_Climbing_with_Random_Restarts import hill_climbing_random_restart
from part5_Hill_Climbing_with_Random_Walk import hill_climb_random_walk
from part6_Simulated_Annealing import hill_climb_simulated_annealing
## ----- End Import Statements ----- ##


## ----- Parameters ----- ##
number_of_runs = 50
iterations = 50
increment = 50
puzzle_size = 11
data = [[0.0 for x in range(0, 3)] for y in range(0, number_of_runs)] 
puzzles_store = [{} for x in range(0, number_of_runs)]
## ----- End Parameters ----- ##


max_k = 0
## ----- Generate Points ----- ##
for i in range(0, number_of_runs):
    puzzle = generate_puzzle(puzzle_size)
    
    start_time = time.time()
    new_puzzle, _, new_k = hill_climb_simulated_annealing(puzzle, puzzle_size, iterations, 100, 0.9)
    end_time = time.time()
    
    data[i][0] = iterations
    data[i][1] = end_time - start_time 
    data[i][2] = new_k
    if new_k > max_k:
        max_k = new_k
    
    puzzles_store[i] = new_puzzle
    iterations += increment   
## ----- End Generate Points ----- ##
    
print("Printing Best Puzzle Found: ")    
for i in range(0, number_of_runs):
    if max_k == data[i][2]:
        print_matrix(puzzles_store[i], puzzle_size)
        visited, k = BFS(puzzles_store[i], puzzle_size)
        print_path(puzzles_store[i], puzzle_size, visited)
        

with open('store_table.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in data]
    