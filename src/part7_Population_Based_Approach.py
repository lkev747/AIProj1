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
  
  
    ##### Print The Flattenened Matrices
    print('Flattened Matrices: ')
    for i in range(0, number_of_puzzles):
        for j in range(0, len(population[0])):
            print(population[i][j]['value'], ', ', end = '')
        print()
    ##### End Print
        
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
    
    
    ##### Print the Fitnesses
    print('K Values: ', end = '')
    for i in range(0, len(selection)):
        print(k_values[i], ', ' , end = '')
    print()
    for i in range(0, len(selection)):
        print(survivability[i], ', ' , end = '')
    print()
    for i in range(0, len(selection)):
        print(selection[i], ', ' , end = '')
    print()
    ##### End Print
    
    
    ## ----- Selection Step ----- ##
    selected_pop = [] # Selected Population of flattened puzzles
    for j in range(0, number_of_puzzles):
        #index = 0
        #temp = random.random()
        #for i in selection:
        #    if temp < i:
        #        break
        #    index += 1
        
        flag = True     # flag is true means we are picking a differeing string
        while(flag):
            index = 0
            temp = random.random()
            for i in selection:
                if temp < i:
                    break
                index += 1
            if(j > 0):
                if (selected_pop[-1] == population[index]):
                    flag = True
                else:
                   selected_pop.append(population[index])
                   flag = False 
            else:
                selected_pop.append(population[index])
                flag = False
            
        
    ## ----- End Selection Step ----- ##
    
    
    ##### Print The Flattenened Matrices
    print('Selected Matrices: ')
    for i in range(0, number_of_puzzles):
        for j in range(0, len(selected_pop[0])):
            print(selected_pop[i][j]['value'], ', ', end = '')
        print()
    print()
    ##### End Print
    
    
    ## ----- Crossover Step ----- ##
    if len(selected_pop) % 2 > 0: # in case of odd number of puzzles
        selected_pop.append(population[0])
        print()
    crossover_pop = [] # List of child arrays post-mating
    while selected_pop:
        par1 = selected_pop.pop(0)
        par2 = selected_pop.pop(0)
        split_location = random.randint(1, len(population[0]) - 1)
        print('Crossed Matrices at: ', split_location)
        crossover_pop.append(par1[0:split_location] + par2[split_location:])
        split_location = random.randint(1, len(population[0]) - 1)
        print('Crossed Matrices at: ', split_location)
        crossover_pop.append(par2[0:split_location] + par1[split_location:])
    ## ----- End Crossover Step ----- ##
    
    ## ----- Print The Flattenened Matrices ----- ##
    for i in range(0, number_of_puzzles):
        for j in range(0, len(crossover_pop[0])):
            print(crossover_pop[i][j]['value'], ', ', end = '')
        print()
    print()
    ## ----- End Print the Flattened Matrices----- ##
    
    ## ----- Reshape Puzzles ----- ##
    next_gen = [] # array of square matrix puzzles
    for i in range(0, number_of_puzzles):
        temp_matrix = [[{} for x in range(size_of_puzzles)] for y in range(size_of_puzzles)]
        for j in range(0, (size_of_puzzles*size_of_puzzles)):
            temp_matrix[math.floor(j / size_of_puzzles)][j % size_of_puzzles] = crossover_pop[i][j]
        next_gen.append(temp_matrix)
    ## ----- End Reshape Puzzles ----- ##
    
    ## Mutation for all Puzzles
    for i in range(0, number_of_puzzles):
    ## Mutation Step for each Puzzle ##
            ## Pick a cell
        mutate_x = [0]*size_of_puzzles
        mutate_y = [0]*size_of_puzzles 
        
        for m in range(0, size_of_puzzles):
            pick_again = True
            while pick_again:
                randx = random.randint(0, size_of_puzzles - 1)
                randy = random.randint(0, size_of_puzzles - 1)
                if not (randx == size_of_puzzles - 1 and randy == size_of_puzzles -1):  # meaning the goal cell was not picked
                    ## we also want to check that this cell wasnt picked already
                    mutate_x[m] = randx
                    mutate_y[m] = randy
                    pick_again = False
                    break
        print(mutate_x, mutate_y)       
            ## Pick a random number
        mutate_value = [0]*size_of_puzzles
        for p in range(0, size_of_puzzles):
            temp_value = 0
            for k in range(0, int((size_of_puzzles - 1)/2) + 1):
                if(mutate_x[p] == k or mutate_x[p] == size_of_puzzles - (k + 1) or mutate_y[p] == k or mutate_y[p] == size_of_puzzles - (k + 1)): 
                    pick_again = True
                    while pick_again:
                        temp_value = random.randint(1, size_of_puzzles - (k + 1))
                        if not (temp_value == next_gen[i][mutate_x[p]][mutate_y[p]]['value']): # meaning the random value is different from the previous value already in the cell
                            #next_gen[mutate_x[p]][mutate_y[p]]['value'] = temp_value
                            mutate_value[p] = temp_value
                            pick_again = False
                            break
            break
        print(mutate_value)
            ## Assign the random number to the cell
        for q in range(0, size_of_puzzles):
            next_gen[i][mutate_x[q]][mutate_y[q]]['value'] = mutate_value[q]
        
        ## print out next gen
        for w in range(0, number_of_puzzles):
            for x in range(0, size_of_puzzles):
                for y in range(0, size_of_puzzles):
                    print(next_gen[w][x][y]['value'], ', ', end='')
                print()
            print()
        
        
    return next_gen 
    ## End Mutation Step for each Puzzle ##
    
    ## End Mutation Step for all Puzzles ##
       
    ## ----- Mutation Step ----- ##
    '''
    for i in range(0, number_of_puzzles):
        mutation_x = [0]*size_of_puzzles
        mutation_y = [0]*size_of_puzzles
        mutation_value = [0]*size_of_puzzles
        
        for j in range(0, size_of_puzzles):
            ## ----- Choose Random Cell ----- ##
            a = True
            randx = 0
            randy = 0
            while a:
                randx = random.randint(0, size_of_puzzles - 1)
                randy = random.randint(0, size_of_puzzles - 1)
                if (randx == size_of_puzzles - 1 and randy == size_of_puzzles - 1):
                    a = True
                else:
                    if(j > 0):
                        for m in range(0, j):
                            if(mutation_x[m] == randx and mutation_y[m] == randy):
                                a = True
                            else:
                                a = False
                                mutation_x[j] = randx
                                mutation_y[j] = randy
                                break
                    else:
                        a = False
                        mutation_x[j] = randx
                        mutation_y[j] = randy
            ## ----- End Choose Random Cell ----- ##
           
            ## ----- Choose Random Value ----- ##
        for p in range(0, size_of_puzzles):
            temp = 0
            b = True
            #print("Entering while b")
            while b:
                for k in range(0, int((size_of_puzzles - 1)/2) + 1):
                    if(mutation_x[p] == k or mutation_x[p] == size_of_puzzles - (k + 1) or mutation_y[p] == k or mutation_y[p] == size_of_puzzles - (k + 1)): 
                        temp = random.randint(1, size_of_puzzles - (k + 1))
                        if(temp == 0):
                            print("temp = 0")
                        if temp != next_gen[i][randx][randy]['value']:
                            mutation_value[p] = temp
                            b = False
                            #print("value, ", temp, "at P, ", p)
                            break
                break
            #print("Exiting while b")
            ## ----- End Choose Random Value ----- ##
        for r in range(0, size_of_puzzles):
            next_gen[i][mutation_x[r]][mutation_y[r]]['value'] = mutation_value[r]
    ## ----- End Mutation Step ----- ##
        print(mutation_x, mutation_y, mutation_value)
        '''
    


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
