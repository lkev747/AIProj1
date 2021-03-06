'''
Created on Sep 20, 2017

@author: Kevin and Ely
'''

## ----- Import Statements ----- ##
import random
import math
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
from part2_puzzle_evaluation import print_path
from part2_puzzle_evaluation import BFS
from lib2to3.fixer_util import Number
## ----- End Import Statements ----- ##

def genetic_algorithm(puzzles, number_of_puzzles, size_of_puzzles): # puzzles is a list of square matrix puzzles
  
    ## ----- Flatten Puzzle ----- ##
    population = [] # array of puzzles flattened to arrays
    for i in range(0, number_of_puzzles):
        flattened_puzzle = [] # single puzzle flattened to arrays
        for x in range(0, size_of_puzzles):
            for y in range(0, size_of_puzzles):
                flattened_puzzle.append(puzzles[i][x][y])        
        population.append(flattened_puzzle)
    ## ----- End Flatten Puzzle ----- ##
  

         
    ## ----- Evaluate Fitness ----- ##
    k_values = [] # k values of the puzzles
    survivability = [] # percent chance of the survivability of the puzzle
    selection = [] # number line representing each index
    k_sum = 0
    
    for i in range(0, len(population)):
        _, k = BFS(puzzles[i], size_of_puzzles)
        if k < 0:
            k = 1 # puzzle is unsolveable, but we permit the slim possibility of survival
        k_values.append(k)
        k_sum += k

    for i in range(0, len(k_values)):
        survivability.append(k_values[i]/k_sum) 
        selection.append(sum(survivability))
    ## ----- End Evaluate Fitness ----- ##
    
    '''
    ## Restrict 2 consecutive
    ## ----- Selection Step ----- ##
    selected_pop = [] # Selected Population of flattened puzzles

    for j in range(0, number_of_puzzles):
        flag = True     # flag is true means we are picking a differeing string

        while(flag):
            print("flag")
            index = 0
            temp = random.random()
            for i in selection:
                if temp < i:
                    if j > 0:
                        if (selected_pop[-1] == population[index]):
                            flag = True
                            break
                        else:
                            selected_pop.append(population[index])
                            flag = False
                            break
                    else:
                        selected_pop.append(population[index])
                        flag = False                    
                    break
                index += 1
    ## ----- End Selection Step ----- ##
    '''
    ## Dont Restrict 2 consecutive
    ## ----- Selection Step ----- ##
    selected_pop = [] # Selected Population of flattened puzzles

    for j in range(0, number_of_puzzles):
        flag = True     # flag is true means we are picking a differeing string

        while(flag):
            print("flag")
            index = 0
            temp = random.random()
            for i in selection:
                if temp < i:
                    selected_pop.append(population[index])
                    flag = False
                    break
                index += 1
    ## ----- End Selection Step ----- ##
    
    ## ----- Crossover Step ----- ##
    if len(selected_pop) % 2 > 0: # in case of odd number of puzzles
        selected_pop.append(population[0])
        print()
    crossover_pop = [] # List of child arrays post-mating
    while selected_pop:
        print("selected_pop")
        par1 = selected_pop.pop(0)
        par2 = selected_pop.pop(0)
        split_location = random.randint(1, len(population[0]) - 1)
        crossover_pop.append(par1[0:split_location] + par2[split_location:])
        split_location = random.randint(1, len(population[0]) - 1)
        crossover_pop.append(par2[0:split_location] + par1[split_location:])
    ## ----- End Crossover Step ----- ##


        
    ## ----- Reshape Puzzles ----- ##
    next_gen = [] # array of square matrix puzzles
    for i in range(0, number_of_puzzles):
        temp_matrix = [[{} for x in range(size_of_puzzles)] for y in range(size_of_puzzles)]
        for j in range(0, (size_of_puzzles*size_of_puzzles)):
            temp_matrix[math.floor(j / size_of_puzzles)][j % size_of_puzzles] = crossover_pop[i][j]
        next_gen.append(temp_matrix)
    ## ----- End Reshape Puzzles ----- ##

    print("before mutation")
    for i in range(0, number_of_puzzles):
        print_matrix(next_gen[i], size_of_puzzles)
    
    ## ----- Mutation Step ----- ##
    for i in range(0, number_of_puzzles): 
        
        ## ----- Choose Random Cell ----- ##
        a = True
        randx = 0
        randy = 0
        while a:
            print("a")
            randx = random.randint(0, size_of_puzzles - 1)
            randy = random.randint(0, size_of_puzzles - 1)
            if not (randx == size_of_puzzles - 1 and randy == size_of_puzzles - 1):
                a = False
        ## ----- End Choose Random Cell ----- ##
        
        ## ----- Choose Random Value ----- ##
        temp = 0
        b = True
        while b:
            print("b")
            for k in range(0, int((size_of_puzzles - 1)/2) + 1):
                if(randx == k or randx == size_of_puzzles - (k + 1) or randy == k or randy == size_of_puzzles - (k + 1)): 
                    temp = random.randint(1, size_of_puzzles - (k + 1))
                    if temp != next_gen[i][randx][randy]['value']:
                        next_gen[i][randx][randy]['value'] = temp
                        b = False
                        break
        ## ----- End Choose Random Value ----- ##

    print("after mutation")
    for i in range(0, number_of_puzzles):
        print_matrix(next_gen[i], size_of_puzzles)
    

    return next_gen
    


## ----- Input Puzzle Size ----- ##
number_of_puzzles = int(input('Enter the number of puzzles: '))
iterations = int(input('Enter the number of iterations: '))
n = input('Enter the size of the puzzle grid (5, 7, 9, 11): ')  # need to validate
size_of_puzzles = int(n)
## ----- End Input Puzzle Size ----- ##

## ----- Generate Set of Puzzles ----- ##
puzzles = []
for i in range(0, number_of_puzzles):
    temp = generate_puzzle(size_of_puzzles)
    puzzles.append(temp)
## ----- End Generate Set of Puzzles ------ ##


## ----- Print Population ----- ##
for i in range(0, len(puzzles)):
    print('Puzzle #', i)
    print_matrix(puzzles[i], size_of_puzzles)
    print()
## ----- End Print Population ----- ##


## ----- Unit Test ----- ##
for i in range(0, iterations):
    puzzles = genetic_algorithm(puzzles, number_of_puzzles, size_of_puzzles)

print('Completed!!')
for i in range(0, len(puzzles)):
    print_matrix(puzzles[i], size_of_puzzles)
    visited, k = BFS(puzzles[i], size_of_puzzles)
    print_path(puzzles[i], size_of_puzzles, visited)

## ----- End Unit Test ----- ##
print("End part 7")
