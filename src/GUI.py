'''
Created on Sep 24, 2017

@author: Kevin, Ely
'''

## ----- Import Statements ----- ##
from tkinter import *
import random
from part1_puzzle_representation import *
from part2_puzzle_evaluation import *
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
            puzzle[i][j] = elements[j]

    global p_grid 
    p_grid = puzzle
    global p_size 
    p_size = puzzle_size

    for x in range(0, puzzle_size):
        for y in range(0, puzzle_size):
            Label(frame2, text = puzzle[x][y]).grid(row = x, column = y, sticky = W, padx = 8)
## ----- End Open File, Display Puzzle ----- ##


## ----- Task 2 Call: Evaluate Puzzle ----- ##

def solve(event):
    visited, k = BFS(p_grid, p_size)
    
    for x in range(0, p_size):
        for y in range(0, p_size):
            Label(frame5, text = visited[x][y]).grid(row = x, column = y, sticky = W, padx = 8)

## ----- End Task 2 Call: Evaluate Puzzle ----- ##


## ----- Simple Gui ----- ##
root = Tk() # Creates first window

frame1 = Frame(root) # Label over Puzzle
frame2 = Frame(root) # Display the Puzzle
frame3 = Frame(root) # Enter info and buttons

frame4 = Frame(root) # Label over Visited Matrix
frame5 = Frame(root) # Visited Matrix
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
Label(frame3, text = "Enter size of puzzle grid:").grid(row = 0,
                                                        column = 0)
puzzle_size = Entry(frame3, width = 10)
puzzle_size.grid(row = 0, column = 1)

enter_size = Button(frame3, text = "Enter Size")
enter_size.bind("<Button-1>", display_puzzle)
enter_size.grid(row = 0, column = 3, padx = 15)

Label(frame3, text = "Enter the name of the file: ").grid(row = 1, column = 0)

file_name = Entry(frame3, width = 10)
file_name.grid(row = 1, column = 1)

get_file = Button(frame3, text = "Find File")
get_file.bind("<Button-1>", open_file)
get_file.grid(row = 1, column = 3, padx = 15)


solve_puzzle = Button(frame3, text = "Solve Puzzle")
solve_puzzle.bind("<Button-1>", solve)
solve_puzzle.grid(row = 2, column = 0)

## ----- End Frame 3: Buttons and Inputs ----- ##


## ----- Frame 4: Label over Visited Matrix ----- ##
Label(frame4, text = "Visited Matrix").grid(row = 0, column = 0)
## ----- End Frame 4: Label over Visited Matrix ----- ##


## ----- Frame 5: Visited Matrix ----- ##
for x in range(0, 11):
    for y in range(0, 11):
        Label(frame5, text = '').grid(row = x,
                                      column = y,
                                      sticky = W,
                                      padx = 5)
## ----- End Frame 5: Visited Matrix ----- ##



## ----- Frame 6: Show Steps ----- ##

## ----- End Frame 6: Show Steps ----- ##



frame1.grid(row = 0, column = 0)
frame2.grid(row = 1, column = 0)
frame3.grid(row = 2, column = 0)
frame4.grid(row = 0, column = 1)
frame5.grid(row = 1, column = 1)

# Keeps our program running and our main window visible until we close it #
root.mainloop()
