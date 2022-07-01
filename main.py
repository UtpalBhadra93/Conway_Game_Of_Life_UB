# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:47:37 2022

@author: utpal.bhadra
"""

from findNeighbour import findNeighbour
from lifeRules import lifeRules
from updateMatrix import state
from imagePlot import imagePlot

import numpy
import pygame
#Global variable definations

# default cell color ** Note: not to be changed
default_dead_color = 0
default_live_color = 1 

matrix = numpy.random.choice([default_dead_color,default_live_color], size=(50, 50)) #choose random matrix
count = 0 # define frame/ simulation run count
radius = 1 #define the radius of the filter/ window, default = 1
dead_cell_color = 0 #dead cell color for representation
live_cell_color = 125 #live cell color for representation
bgcolor =  (255,0,0) #define the playground back ground color


def main(matrix, radius, count, default_dead_color, default_live_color, live_cell_color, dead_cell_color, bgcolor):
    while 1:
        imagePlot(matrix, count, default_dead_color, default_live_color, live_cell_color, dead_cell_color, bgcolor)
        for x, y in numpy.ndindex(matrix.shape):
            #find the neighbours of the cell (x,y)
            neighbourss = findNeighbour(matrix, x, y, radius)
            #get state of each cell in the matrix as per previous value.
            status = lifeRules(neighbourss,x,y,matrix[x][y])
            #change the state of each cell in the matrix.
            if status != 0 or state != 5: state(status,matrix,x,y)
        count += 1
    return 0


if __name__ == "__main__":
    pygame.init() #initialize
    main(matrix, radius, count, default_dead_color, default_live_color, live_cell_color, dead_cell_color, bgcolor) #call main
    pygame.quit() #quit
    