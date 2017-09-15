'''
Created on Sep 14, 2017

@author: Kevin, Ely
'''

## ----- Import Statements ----- ##
from part1_puzzle_representation import puz
from part1_puzzle_representation import n
import queue
## ----- End Import Statements ----- ##


## ----- Create Nodes ----- ##
nodes = [[{} for x in range(n)] for y in range(n)] # Store each node as a dictionary
for x in range(0,n):
    for y in range(0,n):
        nodes[x][y]['value'] = puz[x][y]
        nodes[x][y]['xcoord'] = x
        nodes[x][y]['ycoord'] = y
## ----- End Create Nodes ----- ##


## ----- Breadth-First Search ----- ##
q = queue.Queue() # Queue
s = [] # Stack
visited = [[0 for x in range(n)] for y in range(n)] # Matrix of visited nodes

q.put(nodes[0][0]) # Enqueue the start point
visited[0][0] = 1 # Mark start point as visited


while not q.empty():
    w = q.get() # Dequeue from q (returns node dictionary)
    s.append(w) # Append to stack
    
    has_children = False # Check for and enqueue valid children
    if (w['xcoord'] + w['value'] < n-1) and (visited[w['xcoord'] + w['value']][w['ycoord']] == 0): 
        visited[ w['xcoord'] + w['value'] ][ w['ycoord'] ] = 1 # Mark new node as visited
        q.put(nodes[ w['xcoord'] + w['value'] ][ w['ycoord'] ]) # Add child node to queue
        has_children = True
    if (w['xcoord'] - w['value'] > 0) and (visited[w['xcoord'] - w['value']][w['ycoord']] == 0): 
        visited[ w['xcoord'] - w['value'] ][ w['ycoord'] ] = 1 # Mark new node as visited
        q.put(nodes[ w['xcoord'] - w['value'] ][ w['ycoord'] ]) # Add child node to queue
        has_children = True
    if (w['ycoord'] + w['value'] < n-1) and (visited[w['xcoord']][w['ycoord'] + w['value']] == 0): 
        visited[ w['xcoord'] ][ w['ycoord'] + w['value'] ] = 1 # Mark new node as visited
        q.put(nodes[ w['xcoord'] ][ w['ycoord'] + w['value'] ]) # Add child node to queue
        has_children = True
    if (w['ycoord'] - w['value'] > 0) and (visited[w['xcoord']][w['ycoord'] - w['value']] == 0): 
        visited[ w['xcoord'] ][ w['ycoord'] - w['value'] ] = 1 # Mark new node as visited
        q.put(nodes[ w['xcoord'] ][ w['ycoord'] - w['value'] ]) # Add child node to queue
        has_children = True
    if has_children == False: # Needs more conditions, this is wrong. Tree can still go in the wrong direction
        s.pop()        
    if w['value'] == 0:
        break

## ----- End Breadth-First Search ----- ##


## ----- Print Successful Path ----- ##
for i in range(0, len(s)):
    print(s[i])
## ----- End Print Successful Path ----- ##

print('code terminated')
