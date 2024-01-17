import pygame

from random import randint
from meteorite import Meteorit

garbage_imgs = ({'path': 'virus.png'},
                {'path': 'asteroid.png'},
                {'path': 'meteorite-mineral.png'},
                {'path': 'bolt.png'},
                {'path': 'amfoot.png'},
                {'path': 'gold.png'},
                {'path': 'mineral.png'},
                {'path': 'blue-ast.png'},
                {'path': 'red-ast.png'},
                {'path': 'green-ast.png'},
                {'path': 'orange-ast.png'},
                {'path': 'molot.png'},
                {'path': 'bag.png'},
                {'path': 'crystal-quartz.png'},
                {'path': 'puck.png'},
                {'path': 'disk.png'},
                {'path': 'small-meteor.png'})

garbage_surface = [pygame.image.load('images/' + file['path']) for file in garbage_imgs]


def create_meteorite(meteorites, garbage_surface, WIDTH):
    indx = randint(0, len(garbage_surface) - 1)
    x_position = randint(40, WIDTH - 40)
    speed_garbage = randint(1, 5)
    return Meteorit(x_position, speed_garbage, garbage_surface[indx], meteorites)
