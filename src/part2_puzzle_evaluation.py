'''
Created on Sep 14, 2017

@author: Kevin, Ely
'''

## ----- Import Statements ----- ##
from part1_puzzle_representation import puz
from part1_puzzle_representation import n
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
q = [] # Queue
visited = [[0 for x in range(n)] for y in range(n)] # Matrix of visited nodes

q.append(nodes[0][0]) # Enqueue the start point
visited[0][0] = 1 # Mark start point as visited

while len(q) != 0:
    
#    for i in range(0, len(q)):
#        print('(', q[i]['xcoord'], ', ', q[i]['ycoord'], ')', end = '')
    
    w = q.pop(0) # Dequeue from q (returns node dictionary)
    has_children = False # Check for and enqueue valid children
    
    if w['value'] == 0: # Win condition, we found the goal
        break
    
    if (w['xcoord'] + w['value'] <= n-1) and (visited[w['xcoord'] + w['value']][w['ycoord']] == 0): 
        visited[w['xcoord'] + w['value']][w['ycoord']] = 1 # Mark new node as visited
        q.append(nodes[ w['xcoord'] + w['value']][w['ycoord']]) # Add child node to queue
        nodes[w['xcoord'] + w['value']][w['ycoord']]['parent'] = w
        has_children = True
        
    if (w['xcoord'] - w['value'] >= 0) and (visited[w['xcoord'] - w['value']][w['ycoord']] == 0): 
        visited[ w['xcoord'] - w['value'] ][ w['ycoord'] ] = 1 # Mark new node as visited
        q.append(nodes[w['xcoord'] - w['value']][w['ycoord']]) # Add child node to queue
        nodes[w['xcoord'] - w['value']][w['ycoord']]['parent'] = w
        has_children = True
        
    if (w['ycoord'] + w['value'] <= n-1) and (visited[w['xcoord']][w['ycoord'] + w['value']] == 0): 
        visited[w['xcoord']][w['ycoord'] + w['value']] = 1 # Mark new node as visited
        q.append(nodes[w['xcoord']][w['ycoord'] + w['value']]) # Add child node to queue
        nodes[w['xcoord']][w['ycoord'] + w['value']]['parent'] = w
        has_children = True
        
    if (w['ycoord'] - w['value'] >= 0) and (visited[w['xcoord']][w['ycoord'] - w['value']] == 0): 
        visited[ w['xcoord']][w['ycoord'] - w['value']] = 1 # Mark new node as visited
        q.append(nodes[w['xcoord']][ w['ycoord'] - w['value']]) # Add child node to queue
        nodes[w['xcoord']][w['ycoord'] - w['value']]['parent'] = w
        has_children = True

#    print()

## ----- End Breadth-First Search ----- ##


## ----- Print Successful Path ----- ##
goalpath = []
goalpath.append(nodes[n-1][n-1])
par = nodes[n-1][n-1]['parent']

while par['xcoord'] != 0 and par['ycoord'] != 0:
    goalpath.append(par)
    xc = par['xcoord']
    yc = par['ycoord']
    par = nodes[xc][yc]['parent']

goalpath.append(nodes[0][0])
goalpath.reverse()
for i in range(0, len(goalpath)):
    print('(', goalpath[i]['xcoord'], ', ', goalpath[i]['ycoord'], ')')

## ----- End Print Successful Path ----- ##

print('code terminated')
