'''
Created on Sep 24, 2017

@author: Kevin, Ely
'''

## ----- Import Statements ----- ##
from tkinter import *
import random
from part1_puzzle_representation import *
from part2_puzzle_evaluation import *
from part3_basic_hill_climbing_approach import hill_climb
from part4_Hill_Climbing_with_Random_Restarts import hill_climbing_random_restart
from part5_Hill_Climbing_with_Random_Walk import hill_climb_random_walk
from part6_Simulated_Annealing import hill_climb_simulated_annealing
import time
from _tracemalloc import start
## ----- End Import Statements ----- ##



## ----- Generated Random Puzzle given grid size ----- ##
def display_puzzle(event):
    n = int(puzzle_size.get())
    nodes = generate_puzzle(n)
    
    global p_grid 
    p_grid = nodes
    global p_size 
    p_size = n
    
    for x in range(0, n):
        for y in range(0, n):
            Label(frame2, text = nodes[x][y]['value']).grid(row = x,
                                                            column = y,
                                                            sticky = W,
                                                            padx = 8)
## ----- End Generated Random Puzzle given grid size ----- ##



## ----- Open File, Display Puzzle ------ ##
def open_file(event):
    
    f = file_name.get()
    fileObject = open(f, 'r')
    line_list = fileObject.readlines()
    fileObject.close()
    
    puzzle_size = int(line_list[0])
    puzzle = [[{} for x in range(0, puzzle_size)] for y in range(0, puzzle_size)]
    
    for i in range(0, puzzle_size):
        row = line_list[i+1]
        elements = row.split()
        for j in range(0, puzzle_size):
            puzzle[i][j]['xcoord'] = i
            puzzle[i][j]['ycoord'] = j
            puzzle[i][j]['level'] = 0
            puzzle[i][j]['value'] = int(elements[j])

    global p_grid 
    p_grid = puzzle
    global p_size 
    p_size = puzzle_size

    for x in range(0, puzzle_size):
        for y in range(0, puzzle_size):
            Label(frame2, text = puzzle[x][y]['value']).grid(row = x, column = y, sticky = W, padx = 8)
## ----- End Open File, Display Puzzle ----- ##



## ----- Clear Spaces ----- ##
def clear_space(event):
    event.widget.delete(0, "end")
    return None
## ----- End Clear Spaces ----- ##


## ----- Task 2 Call: Evaluate Puzzle ----- ##
def solve(event):
    start_time = time.time()
    visited, k = BFS(p_grid, p_size)
    end_time = time.time()
    
    for x in range(0, p_size):
        for y in range(0, p_size):
            Label(frame5, text = visited[x][y]).grid(row = x, column = y, sticky = W, padx = 8)
    Label(frame5, text = 0).grid(row = 0, column = 0, sticky = W, padx = 8)
    Label(frame6, text = k).grid(row = 1, column = 1, sticky = W, padx = 8)
    Label(frame6, text = str(end_time - start_time) + " seconds").grid(row = 2, column = 1, sticky = W, padx = 8)
    
    solution = print_path(p_grid, p_size, visited)
    
    Label(frame6, text = solution).grid(row = 0, column = 1, sticky = W, padx = 8)
## ----- End Task 2 Call: Evaluate Puzzle ----- ##



## ----- Task 3 Call: Hill Climbing ----- ##
def hill(event):
    iteration = int(num_iter1.get())
    start_time = time.time()
    puzzle, visited, k = hill_climb(p_grid, p_size, iteration)
    end_time = time.time()
    
    root2 = Tk()
    frameA = Frame(root2) # contains Puzzle Label
    frameB = Frame(root2) # contains New Puzzle
    frameC = Frame(root2) # contains Visit Matrix Label
    frameD = Frame(root2) # contains Visit Matrix
    frameE = Frame(root2) # contains Steps and K Value

    Label(frameA, text = "New Puzzle").grid(row = 0, column = 0)
    Label(frameC, text = "Visited Matrix").grid(row = 0, column = 0)
    
    for x in range(0, p_size):
        for y in range(0, p_size):
            Label(frameB, text = puzzle[x][y]['value']).grid(row = x,
                                                             column = y,
                                                             sticky = W,
                                                             padx = 5)
            Label(frameD, text = visited[x][y]).grid(row = x,
                                                     column = y,
                                                     sticky = W,
                                                     padx = 5)
    
    Label(frameD, text = 0).grid(row = 0, column = 0, sticky = W, padx = 5)
    solution = print_path(puzzle, p_size, visited)
    
    Label(frameE, text = "Path: ").grid(row = 0, column = 0, sticky = W)
    Label(frameE, text = solution).grid(row = 0, column = 1, sticky = W)
    Label(frameE, text = "K Value: ").grid(row = 1, column = 0, sticky = W)
    Label(frameE, text = k).grid(row = 1, column = 1, sticky = W)
    Label(frameE, text = "Time: ").grid(row = 2, column = 0, sticky = W)
    Label(frameE, text = str(end_time - start_time) + " seconds").grid(row = 2, column = 1, sticky = W)
    
    frameA.grid(row = 0, column = 0)
    frameB.grid(row = 1, column = 0)
    frameC.grid(row = 0, column = 1)
    frameD.grid(row = 1, column = 1)
    frameE.grid(row = 2, column = 1)        
    root2.mainloop()
## ----- End Task 3 Call: Hill Climbing ----- ##



## ----- Task 4 Call: Hill Climbing w/ RR ----- ##
def hill_rr(event):
    iteration = int(num_iter2.get())
    restarts = int(num_rest.get())
    
    start_time = time.time()
    puzzle, visited, k = hill_climbing_random_restart(p_grid, p_size, iteration, restarts)
    end_time = time.time()
    
    root2 = Tk()
    frameA = Frame(root2) # contains Puzzle Label
    frameB = Frame(root2) # contains New Puzzle
    frameC = Frame(root2) # contains Visit Matrix Label
    frameD = Frame(root2) # contains Visit Matrix
    frameE = Frame(root2) # contains Steps and K Value

    Label(frameA, text = "New Puzzle").grid(row = 0, column = 0)
    Label(frameC, text = "Visited Matrix").grid(row = 0, column = 0)
    
    for x in range(0, p_size):
        for y in range(0, p_size):
            Label(frameB, text = puzzle[x][y]['value']).grid(row = x,
                                                             column = y,
                                                             sticky = W,
                                                             padx = 5)
            Label(frameD, text = visited[x][y]).grid(row = x,
                                                     column = y,
                                                     sticky = W,
                                                     padx = 5)
    Label(frameD, text = 0).grid(row = 0, column = 0, sticky = W, padx = 5)
    solution = print_path(puzzle, p_size, visited)
    
    Label(frameE, text = "Path: ").grid(row = 0, column = 0, sticky = W)
    Label(frameE, text = solution).grid(row = 0, column = 1, sticky = W)
    Label(frameE, text = "K Value: ").grid(row = 1, column = 0, sticky = W)
    Label(frameE, text = k).grid(row = 1, column = 1, sticky = W)
    Label(frameE, text = "Time: ").grid(row = 2, column = 0, sticky = W)
    Label(frameE, text = str(end_time - start_time) + " seconds").grid(row = 2, column = 1, sticky = W)
    
    frameA.grid(row = 0, column = 0)
    frameB.grid(row = 1, column = 0)
    frameC.grid(row = 0, column = 1)
    frameD.grid(row = 1, column = 1)
    frameE.grid(row = 2, column = 1)        
    root2.mainloop()

## ----- End Task 4 Call: Hill Climbing w/ RR ----- ##


## ----- Task 5 Call: Hill Climbing w/ RW ----- ##
def hill_rw(event):
    iteration = int(num_iter3.get())
    probability = int(walk_prob.get())
    
    start_time = time.time()
    puzzle, visited, k = hill_climb_random_walk(p_grid, p_size, iteration, probability)
    end_time = time.time()
            
    root2 = Tk()
    frameA = Frame(root2) # contains Puzzle Label
    frameB = Frame(root2) # contains New Puzzle
    frameC = Frame(root2) # contains Visit Matrix Label
    frameD = Frame(root2) # contains Visit Matrix
    frameE = Frame(root2) # contains Steps and K Value

    Label(frameA, text = "New Puzzle").grid(row = 0, column = 0)
    Label(frameC, text = "Visited Matrix").grid(row = 0, column = 0)
    
    for x in range(0, p_size):
        for y in range(0, p_size):
            Label(frameB, text = puzzle[x][y]['value']).grid(row = x,
                                                             column = y,
                                                             sticky = W,
                                                             padx = 5)
            Label(frameD, text = visited[x][y]).grid(row = x,
                                                     column = y,
                                                     sticky = W,
                                                     padx = 5)
    Label(frameD, text = 0).grid(row = 0, column = 0, sticky = W, padx = 5)
    solution = print_path(puzzle, p_size, visited)
    
    Label(frameE, text = "Path: ").grid(row = 0, column = 0, sticky = W)
    Label(frameE, text = solution).grid(row = 0, column = 1, sticky = W)
    Label(frameE, text = "K Value: ").grid(row = 1, column = 0, sticky = W)
    Label(frameE, text = k).grid(row = 1, column = 1, sticky = W)
    Label(frameE, text = "Time: ").grid(row = 2, column = 0, sticky = W)
    Label(frameE, text = str(end_time - start_time) + " seconds").grid(row = 2, column = 1, sticky = W)
    
    frameA.grid(row = 0, column = 0)
    frameB.grid(row = 1, column = 0)
    frameC.grid(row = 0, column = 1)
    frameD.grid(row = 1, column = 1)
    frameE.grid(row = 2, column = 1)        
    root2.mainloop()
## ----- End Task 5 Call: Hill Climbing w/ RW ----- ##


## ----- Task 6 Call: Simulated Annealing ----- ##
def sim_ann(event):
    iteration = int(num_iter4.get())
    temperature = int(temper.get())
    decay_rate = float(decay_const.get())
    
    start_time = time.time()
    puzzle, visited, k = hill_climb_simulated_annealing(p_grid, p_size, iteration, temperature, decay_rate)
    end_time = time.time()
            
    root2 = Tk()
    frameA = Frame(root2) # contains Puzzle Label
    frameB = Frame(root2) # contains New Puzzle
    frameC = Frame(root2) # contains Visit Matrix Label
    frameD = Frame(root2) # contains Visit Matrix
    frameE = Frame(root2) # contains Steps and K Value

    Label(frameA, text = "New Puzzle").grid(row = 0, column = 0)
    Label(frameC, text = "Visited Matrix").grid(row = 0, column = 0)
    
    for x in range(0, p_size):
        for y in range(0, p_size):
            Label(frameB, text = puzzle[x][y]['value']).grid(row = x,
                                                             column = y,
                                                             sticky = W,
                                                             padx = 5)
            Label(frameD, text = visited[x][y]).grid(row = x,
                                                     column = y,
                                                     sticky = W,
                                                     padx = 5)
    Label(frameD, text = 0).grid(row = 0, column = 0, sticky = W, padx = 5)
    solution = print_path(puzzle, p_size, visited)
    
    Label(frameE, text = "Path: ").grid(row = 0, column = 0, sticky = W)
    Label(frameE, text = solution).grid(row = 0, column = 1, sticky = W)
    Label(frameE, text = "K Value: ").grid(row = 1, column = 0, sticky = W)
    Label(frameE, text = k).grid(row = 1, column = 1, sticky = W)
    Label(frameE, text = "Time: ").grid(row = 2, column = 0, sticky = W)
    Label(frameE, text = str(end_time - start_time) + " seconds").grid(row = 2, column = 1, sticky = W)
    
    frameA.grid(row = 0, column = 0)
    frameB.grid(row = 1, column = 0)
    frameC.grid(row = 0, column = 1)
    frameD.grid(row = 1, column = 1)
    frameE.grid(row = 2, column = 1)        
    root2.mainloop()


## ----- End Task 6 Call: Simulated Annealing ----- ##


## ----- Simple Gui ----- ##
root = Tk() # Creates first window

frame1 = Frame(root) # Label over Puzzle
frame2 = Frame(root) # Display the Puzzle
frame3 = Frame(root) # Enter info and buttons
frame4 = Frame(root) # Label over Visited Matrix
frame5 = Frame(root) # Visited Matrix
frame6 = Frame(root) # Print Steps and K Value
frame7 = Frame(root) # More Buttons
## ----- End Simple Gui ----- ##



## ----- Frame 1: Label over Puzzle ----- ##
Label(frame1, text = "Sample Puzzle").grid(row = 0, column = 0)
## ----- End Frame 1: Label over Puzzle ----- ##



## ----- Frame 2: Display the Puzzle ----- ##
for x in range(0, 11):
    for y in range(0, 11):
        Label(frame2, text = '').grid(row = x,
                                      column = y,
                                      sticky = W,
                                      padx = 5)
## ----- End Frame 2: Dislay the Puzzle ----- ##



## ----- Frame 3: Buttons and Inputs ----- ##
Label(frame3, text = "Enter size of puzzle grid:").grid(row = 0, column = 0, sticky = W)
puzzle_size = Entry(frame3, width = 10)
puzzle_size.grid(row = 0, column = 1)

enter_size = Button(frame3, text = "Enter Size")
enter_size.bind("<Button-1>", display_puzzle)
enter_size.grid(row = 0, column = 3, padx = 15, sticky = W)

Label(frame3, text = "Enter the name of the file: ").grid(row = 1, column = 0, sticky = W)

file_name = Entry(frame3, width = 10)
file_name.grid(row = 1, column = 1)

get_file = Button(frame3, text = "Find File")
get_file.bind("<Button-1>", open_file)
get_file.grid(row = 1, column = 3, padx = 15, sticky = W)


solve_puzzle = Button(frame3, text = "Solve Puzzle")
solve_puzzle.bind("<Button-1>", solve)
solve_puzzle.grid(row = 2, column = 3, sticky = W, padx = 15)
## ----- End Frame 3: Buttons and Inputs ----- ##



## ----- Frame 4: Label over Visited Matrix ----- ##
Label(frame4, text = "Visited Matrix").grid(row = 0, column = 0, padx = 125)
## ----- End Frame 4: Label over Visited Matrix ----- ##



## ----- Frame 5: Visited Matrix ----- ##
for x in range(0, 11):
    for y in range(0, 11):
        Label(frame5, text = '').grid(row = x,
                                      column = y,
                                      sticky = W,
                                      padx = 5)
## ----- End Frame 5: Visited Matrix ----- ##



## ----- Frame 6: Show Steps and k value ----- ##
Label(frame6, text = 'Steps: ').grid(row = 0, column = 0, sticky = W)
Label(frame6, text = 'K-Value: ').grid(row = 1, column = 0, sticky = W)
Label(frame6, text = 'Time: ').grid(row = 2, column = 0, sticky = W)
## ----- End Frame 6: Show Steps and k value ----- ##



## ----- Frame 7: More Buttons ----- ##

Label(frame7, text = 'New Puzzle').grid(row = 0, column = 0, pady = 10)

b_hill = Button(frame7, text = "Hill Climb Only    ")
b_hill.bind("<Button-1>", hill)
b_hill.grid(row = 1, column = 0, sticky = W, padx = 10)

num_iter1 = Entry(frame7, width = 15)
num_iter1.grid(row = 1, column = 1)
num_iter1.insert(0, "# Steps?")
num_iter1.bind("<Button-1>", clear_space)

b_hill_rr = Button(frame7, text = "Hill Climb w/ RR  ")
b_hill_rr.bind("<Button-1>", hill_rr)
b_hill_rr.grid(row = 2, column = 0, sticky = W, padx = 10)

num_iter2 = Entry(frame7, width = 15)
num_iter2.grid(row = 2, column = 1)
num_iter2.insert(0, "# Steps?")
num_iter2.bind("<Button-1>", clear_space)

num_rest = Entry(frame7, width = 15)
num_rest.grid(row = 2, column = 2)
num_rest.insert(0, "# Restarts?")
num_rest.bind("<Button-1>", clear_space)

b_hill_rw = Button(frame7, text = "Hill Climb w/ RW ")
b_hill_rw.bind("<Button-1>", hill_rw)
b_hill_rw.grid(row = 3, column = 0, sticky = W, padx = 10)

num_iter3 = Entry(frame7, width = 15)
num_iter3.grid(row = 3, column = 1)
num_iter3.insert(0, "# Steps?")
num_iter3.bind("<Button-1>", clear_space)

walk_prob = Entry(frame7, width = 15)
walk_prob.grid(row = 3, column = 2)
walk_prob.insert(0, "Prob: 0-100?")
walk_prob.bind("<Button-1>", clear_space)

b_sim_an = Button(frame7, text = "Simulate Anneal   ")
b_sim_an.bind("<Button-1>", sim_ann)
b_sim_an.grid(row = 4, column = 0, sticky = W, padx = 10)

num_iter4 = Entry(frame7, width = 15)
num_iter4.grid(row = 4, column = 1)
num_iter4.insert(0, "# Steps?")
num_iter4.bind("<Button-1>", clear_space)

temper = Entry(frame7, width = 15)
temper.grid(row = 4, column = 2)
temper.insert(0, "Temperature?")
temper.bind("<Button-1>", clear_space)

decay_const = Entry(frame7, width = 15)
decay_const.grid(row = 4, column = 3)
decay_const.insert(0, "Decay: 0.0-1.0?")
decay_const.bind("<Button-1>", clear_space)

b_gen_al = Button(frame7, text = "Genetic Algorithm")
b_gen_al.bind("<Button-1>")
b_gen_al.grid(row = 5, column = 0, sticky = W, padx = 10)

num_iter5 = Entry(frame7, width = 15)
num_iter5.grid(row = 5, column = 1)
num_iter5.insert(0, "# Steps?")
num_iter5.bind("<Button-1>", clear_space)

ini_pop = Entry(frame7, width = 15)
ini_pop.grid(row = 5, column = 2)
ini_pop.insert(0, "# Puzzles?")
ini_pop.bind("<Button-1>", clear_space)
## ----- End Frame 7: More Buttons ----- ## 

frame1.grid(row = 0, column = 0)
frame2.grid(row = 1, column = 0)
frame3.grid(row = 2, column = 0)
frame4.grid(row = 0, column = 1)
frame5.grid(row = 1, column = 1)
frame6.grid(row = 2, column = 1)
frame7.grid(row = 3, column = 0)

# Keeps our program running and our main window visible until we close it #
root.mainloop()
