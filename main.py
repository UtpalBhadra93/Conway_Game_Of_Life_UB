# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:47:37 2022

@author: utpal.bhadra
"""

from findNeighbour import findNeighbour
from lifeRules import lifeRules
from updateMatrix import state
from imagePlot import imagePlot

import numpy as np
import pygame

# Global variable definitions
default_dead_color = 0
default_live_color = 1 

'''matrix = np.random.choice([default_dead_color, default_live_color], size=(50, 50))  # choose random matrix'''
np.random.seed(10242)  # you can pick any integer as the seed
matrix = np.random.choice([default_dead_color, default_live_color], size=(50, 50)) #generate matrix with seed
count = 0  # define frame/simulation run count
radius = 1  # define the radius of the filter/window
dead_cell_color = 0  # dead cell color for representation
live_cell_color = 125  # live cell color for representation
bgcolor = (255, 0, 0)  # playground background color

def main(matrix, radius, count, default_dead_color, default_live_color, live_cell_color, dead_cell_color, bgcolor):
    # Create Pygame window once
    window_size_x = matrix.shape[0] * 10  # scale up for visibility
    window_size_y = matrix.shape[1] * 10
    pygame.init()
    window = pygame.display.set_mode((window_size_x, window_size_y))
    clock = pygame.time.Clock()  # control the simulation speed

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the matrix
        new_matrix = matrix.copy()  # optional, avoid modifying matrix while iterating
        for x, y in np.ndindex(matrix.shape):
            neighbours = findNeighbour(matrix, x, y, radius)
            status = lifeRules(neighbours, x, y, matrix[x][y])
            if status != 0 and status != 5:
                state(status, new_matrix, x, y)
        matrix = new_matrix  # update matrix

        # Draw the matrix in the same window
        imagePlot(matrix, count, default_dead_color, default_live_color,
                  live_cell_color, dead_cell_color, bgcolor, window)

        count += 1
        clock.tick(5)  # 5 frames per second

    pygame.quit()

if __name__ == "__main__":
    main(matrix, radius, count, default_dead_color, default_live_color,
         live_cell_color, dead_cell_color, bgcolor)