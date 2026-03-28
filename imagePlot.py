# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:26:06 2022

@author: utpal.bhadra
"""

import pygame
import numpy as np

def imagePlot(matrix, count, default_dead_color, default_live_color, live_cell_color, dead_cell_color, bgcolor, window):
    # Replace live/dead cell colors in the matrix for display
    np.place(matrix, matrix == default_live_color, live_cell_color)
    np.place(matrix, matrix == default_dead_color, dead_cell_color)

    # Create a surface from the matrix
    surface = pygame.surfarray.make_surface(matrix)
    surface = pygame.transform.scale(surface, (window.get_width() - 20, window.get_height() - 20))

    # Fill background and blit the surface
    window.fill(bgcolor)
    window.blit(surface, (10, 10))
    pygame.display.set_caption(f'Cellular Automaton --- Step number: {count}')
    pygame.display.flip()

    # Restore original matrix values
    np.place(matrix, matrix == live_cell_color, default_live_color)
    np.place(matrix, matrix == dead_cell_color, default_dead_color)
    
'''
import numpy
if __name__ == "__main__":
    #matrix = [[1, 0, 1, 1],
    #          [1, 0, 1, 1],
    #          [1, 1, 1, 0],
    #          [1, 1, 1, 0]]
    pygame.init()
    clock = pygame.time.Clock()
    for i in range (10):
        matrix = numpy.random.choice([0,255], size=(20, 20))
        #image = Image.fromarray(matrix,"L").save('img.jpg')
        imagePlot(matrix)
    clock.tick(1)
    pygame.quit()
'''