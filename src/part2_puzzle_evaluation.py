'''
Created on Sep 14, 2017

@author: Kevin, Ely
'''
## ----- Import Statements ----- ##
from part1_puzzle_representation import puz
from part1_puzzle_representation import n
import queue
## ----- End Import Statements ----- ##

## ----- Breadth-First Search ----- ##

q = queue.Queue() # Queue
s = [] # Stack
visited = [[0 for x in range(n)] for y in range(n)] # Matrix of visited nodes

q.put(puz[0][0])
visited[0][0] = 1

while q.full():
    w = q.get()
    
    


## ----- Print Matrix ----- ##
for x in range(0,n):
    for y in range(0,n):
        print(puz[x][y], end = '')
    print()
## ----- End Print Matrix ----- ##