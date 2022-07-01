# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:59:06 2022

@author: utpal.bhadra
"""
def lifeRules(neighbours, x,y, state): #state = 1/0
    neighbours = neighbours.tolist()
    count  = sum(x.count(1) for x in neighbours) - 1
    if state == 0 and count == 0:
        return 0 #ignore update
    if count<2 and state == 1:
        return 1 #underpopulation
    elif count >= 2 and count <=3 and state == 1:
        return 2 #lives on to the next generation
    elif count>3 and state == 1:
        return 3 #overpopulation
    elif count == 2 and state == 0:
        return 4 #reproduction
    else:
        return 5 #unknown

''' 
from findNeighbour import findNeighbour
if __name__ == "__main__":
    matrix = [[0,1,0],
              [1,0,1],
              [0,1,0]]
    x = 1
    y = 1
    radius = 1
    neighbourss = findNeighbour(matrix, x, y, radius)
    #print(neighbourss,matrix[1][1])
    print(lifeRules(neighbourss,x,y,matrix[x][y]))
'''