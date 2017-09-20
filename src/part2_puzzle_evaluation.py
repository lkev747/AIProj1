'''
Created on Sep 14, 2017

@author: Kevin, Ely
'''


## ----- Import Statements ----- ##
from part1_puzzle_representation import generate_puzzle
from part1_puzzle_representation import print_matrix
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


## ----- Print Successful Path ----- #
def print_path(nodes, n, visited):
    if len(nodes[n-1][n-1]) == 5: 
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
        print('Value Function: ', visited[n-1][n-1])
        print('Visited Matrix: ')
        
        visited[0][0] = 0
        for x in range(0, n):
            for y in range(0, n):
                if visited[x][y] == 0 and (x != 0 or y != 0):
                    visited[x][y] = 'X'
                print(visited[x][y], end = '')
            print()    
    
        return visited, visited[n-1][n-1]
    else:
        print("No successful path!")
        visited[0][0] = 0
        k = 0
        for x in range(0, n):
            for y in range(0, n):
                if visited[x][y] == 0 and (x != 0 or y != 0):
                    visited[x][y] = 'X'
                    k = k + 1
                print(visited[x][y], end = '')
            print()
        print('Value Function: ', -1 * k)
        print()
        return visited, -1*k
## ----- End Print Successful Path ----- ##


## ----- Breadth-First Search ----- ##
def BFS(nodes, n):
    q = [] # Queue
    visited = [[0 for x in range(n)] for y in range(n)] # Matrix of visited nodes
    
    q.append(nodes[0][0]) # Enqueue the start point
    visited[0][0] = 1 # Mark start point as visited
    
    while len(q) != 0:        
        w = q.pop(0) # Dequeue from q (returns node dictionary)        
        
        if (w['xcoord'] + w['value'] <= n-1) and (visited[w['xcoord'] + w['value']][w['ycoord']] == 0): 
            visited[w['xcoord'] + w['value']][w['ycoord']] = w['level'] + 1 # Mark new node as visited
            q.append(nodes[ w['xcoord'] + w['value']][w['ycoord']]) # Add child node to queue
            nodes[w['xcoord'] + w['value']][w['ycoord']]['parent'] = w
            nodes[w['xcoord'] + w['value']][w['ycoord']]['level'] = w['level'] + 1
            
        if (w['xcoord'] - w['value'] >= 0) and (visited[w['xcoord'] - w['value']][w['ycoord']] == 0): 
            visited[ w['xcoord'] - w['value'] ][ w['ycoord'] ] = w['level'] + 1 # Mark new node as visited
            q.append(nodes[w['xcoord'] - w['value']][w['ycoord']]) # Add child node to queue
            nodes[w['xcoord'] - w['value']][w['ycoord']]['parent'] = w
            nodes[w['xcoord'] - w['value']][w['ycoord']]['level'] = w['level'] + 1
            
        if (w['ycoord'] + w['value'] <= n-1) and (visited[w['xcoord']][w['ycoord'] + w['value']] == 0): 
            visited[w['xcoord']][w['ycoord'] + w['value']] = w['level'] + 1 # Mark new node as visited
            q.append(nodes[w['xcoord']][w['ycoord'] + w['value']]) # Add child node to queue
            nodes[w['xcoord']][w['ycoord'] + w['value']]['parent'] = w
            nodes[w['xcoord']][w['ycoord'] + w['value']]['level'] = w['level'] + 1
            
        if (w['ycoord'] - w['value'] >= 0) and (visited[w['xcoord']][w['ycoord'] - w['value']] == 0): 
            visited[ w['xcoord']][w['ycoord'] - w['value']] = w['level'] + 1 # Mark new node as visited
            q.append(nodes[w['xcoord']][ w['ycoord'] - w['value']]) # Add child node to queue
            nodes[w['xcoord']][w['ycoord'] - w['value']]['parent'] = w
            nodes[w['xcoord']][w['ycoord'] - w['value']]['level'] = w['level'] + 1

    k = print_path(nodes, n, visited)

    return visited, k
## ----- End Breadth-First Search ----- ##


## ----- Unit Test ----- ##
nodes, n = generate_puzzle()
print_matrix(nodes,n)
visited, k = BFS(nodes, n)
## ----- End Unit Test ----- ##

