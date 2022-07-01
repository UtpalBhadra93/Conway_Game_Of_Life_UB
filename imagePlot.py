# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:26:06 2022

@author: utpal.bhadra
"""

import pygame
import numpy
def imagePlot(matrix, count, default_dead_color, default_live_color, live_cell_color, dead_cell_color, bgcolor):

    #enlarge display window by 700 pixels
    x = numpy.shape(matrix)[0] + 700
    y = numpy.shape(matrix)[1] + 700
    
    #replacing/ setting "Live cell" color for display
    # 0-Black, 2-blue, 125-Yellow, 255-white
    numpy.place(matrix, matrix == default_live_color, live_cell_color)
    numpy.place(matrix, matrix == default_dead_color, dead_cell_color)
    
    #Setting display window
    pygame.display.set_caption('Image --- Step number:  ' + 
                               str(count)) #initializing the display window title.
    window = pygame.display.set_mode((x, y))           #setting the display window.
    surface = pygame.surfarray.make_surface(matrix)    #image to be displayed.
    surface = pygame.transform.scale(surface, (x-20, y-20))  # fit the image to the frame ratio.
    
    for event in pygame.event.get(): #display untill quite is clicked
        if event.type == pygame.QUIT:   #if close button is click
            pygame.quit() #quite pygame display window
    
    #display result
    window.fill(bgcolor) #fill the background color
    window.blit(surface, (10, 10)) #replacing the simulation image - surface as a object
    pygame.display.flip() #display the simulation
    
    #changing to default value
    numpy.place(matrix, matrix == live_cell_color, default_live_color) 
    numpy.place(matrix, matrix == dead_cell_color, default_dead_color)
    return 0
    
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