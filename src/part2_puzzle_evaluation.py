'''
Created on Sep 14, 2017

@author: Kevin, Ely
'''

## ----- Import Statements ----- ##
from part1_puzzle_representation import puz
from part1_puzzle_representation import n
## ----- End Import Statements ----- ##


## ----- Unit Tests ----- ##
'''
# 19 Moves - Initial Example
puz = [[3, 2, 1, 4, 1],
       [3, 2, 1, 3, 3],
       [3, 3, 2, 1, 4],
       [3, 1, 2, 3, 3],
       [1, 4, 4, 3, 0]]

n = 5
'''
'''
# Pass - Value Function 5 Example
puz = [[2, 2, 2, 4, 3],
       [2, 2, 3, 3, 3],
       [3, 3, 2, 3, 3],
       [4, 3, 2, 2, 2],
       [1, 2, 1, 4, 0],]

n = 5
'''
'''
# Fail - Value Function -3 Example
puz = [[3, 3, 2, 4, 3],
       [2, 2, 2, 1, 1],
       [4, 3, 1, 3, 4],
       [2, 3, 1, 1, 3],
       [1, 1, 3, 2, 0]]

n = 5
'''
## ----- End Unit Tests ----- ##


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
#        print(', ', q[i]['value'], '; ', end = '')
    
    w = q.pop(0) # Dequeue from q (returns node dictionary)
    has_children = False # Check for and enqueue valid children
    
    
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


## ----- Print Successful Path ----- #
if len(nodes[n-1][n-1]) == 4:
    print('Successful Path: ')

    goalpath = []
    goalpath.append(nodes[n-1][n-1])
    par = nodes[n-1][n-1]['parent']
    
    while par['xcoord'] != 0 or par['ycoord'] != 0:
        goalpath.append(par)
        xc = par['xcoord']
        yc = par['ycoord']
        par = nodes[xc][yc]['parent']
    
    goalpath.append(nodes[0][0])
    goalpath.reverse()
    for i in range(0, len(goalpath)):
        print('(', goalpath[i]['xcoord'], ', ', goalpath[i]['ycoord'], ')', end = '')
    print()
    print('Value Function: ', len(goalpath) - 1)
else:
    print("No successful path!")
    k = 0
    for x in range(0, n):
        for y in range(0, n):
            print(visited[x][y], end = '')
            if visited[x][y] == 0:
                k = k + 1
        print()   
    print('Value Function: -', k)
## ----- End Print Successful Path ----- ##


print()
print('code terminated')
