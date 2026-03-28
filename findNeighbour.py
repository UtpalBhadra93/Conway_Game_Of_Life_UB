# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 11:59:40 2022

@author: utpal.bhadra
"""

import numpy as np

def findNeighbour(matrix, x, y, radius=1):
    """
    Returns a (2*radius+1)x(2*radius+1) window of neighbours around (x, y)
    including the cell itself. Handles edges by zero-padding.
    """
    rows, cols = matrix.shape
    size = 2 * radius + 1
    
    # Initialize the window with zeros
    neighbours = np.zeros((size, size), dtype=int)
    
    # Calculate bounds for the slice
    row_start = max(0, x - radius)
    row_end = min(rows, x + radius + 1)
    col_start = max(0, y - radius)
    col_end = min(cols, y + radius + 1)
    
    # Calculate where to place the slice in the neighbours window
    insert_row_start = radius - (x - row_start)
    insert_row_end = insert_row_start + (row_end - row_start)
    insert_col_start = radius - (y - col_start)
    insert_col_end = insert_col_start + (col_end - col_start)
    
    # Copy the slice into the neighbours window
    neighbours[insert_row_start:insert_row_end, insert_col_start:insert_col_end] = matrix[row_start:row_end, col_start:col_end]
    
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