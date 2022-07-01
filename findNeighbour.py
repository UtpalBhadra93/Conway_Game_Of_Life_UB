# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 11:59:40 2022

@author: utpal.bhadra
"""

import numpy

def findNeighbour(matrix, x, y, radius):
    window_length = 3 #standard kernel size
    #defining kernel window as (3+2^(radius-1)) if radius>1 else 3
    kernel = [x-radius for x in range ((window_length + (pow(2,radius-1))) if radius>1 else (window_length))]
    neighbours = numpy.zeros((numpy.shape(matrix)[0], numpy.shape(matrix)[1]), dtype="int")
    for row in kernel:
        for column in kernel:
            try:
                if x+row >= 0 and y+column >=0: neighbours[x+row][y+column] = matrix[x+row][y+column] 
            except:
                neighbours[row][column] = 0
    return neighbours

'''
matrix = [[1,5,6,8],
          [1,2,5,9],
          [7,5,6,2]]
x = 1
y = 1
radius = 1
neighbours = [[1,5,6],
              [1,2,5],
              [7,5,6]]
x = 0
y = 0
radius = 1
neighbours = [[1,5,0],
              [1,2,0],
              [0,0,0]]
'''

'''
if __name__ == "__main__":
    matrix = [[1,5,6,8],
              [1,2,5,9],
              [7,5,6,2]]
    x = 0
    y = 3
    radius = 1
    neighbours = numpy.array(findNeighbour(matrix, x, y, radius))
    #neighbours.reshape(numpy.array(matrix).shape)
    print (neighbours)
'''