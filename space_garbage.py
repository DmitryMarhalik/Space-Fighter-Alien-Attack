import pygame

from random import randint
from meteorite import Meteorit

garbage_imgs = ({'path': 'virus.png'},
                {'path': 'asteroid.png'},
                {'path': 'meteorite-mineral.png'},
                {'path': 'bolt.png'},
                {'path': 'astronaut.png'},
                {'path': 'garbage.png'},
                {'path': 'amfoot.png'},
                {'path': 'piano.png'},
                {'path': 'molot.png'},
                {'path': 'potato.png'},
                {'path': 'gas.png'},
                {'path': 'ski.png'},
                {'path': 'bag.png'},
                {'path': 'bosch.png'},
                {'path': 'meteorite.png'},
                {'path': 'crystal-quartz.png'},
                {'path': 'small-meteor.png'})

garbage_surface = [pygame.image.load('images/' + file['path']) for file in garbage_imgs]


def create_meteorite(meteorites, garbage_surface, WIDTH):
    indx = randint(0, len(garbage_surface) - 1)
    x_position = randint(40, WIDTH - 40)
    speed_garbage = randint(1, 4)
    return Meteorit(x_position, speed_garbage, garbage_surface[indx], meteorites)

# def collideBalls():
#     global game_score
#     for ball in balls:
#         if t_rect.collidepoint(ball.rect.center):
#             s_catch.play()
#             game_score += ball.score
# ball.kill()
