from random import randint

import pygame


class Astronaut(pygame.sprite.Sprite):
    def __init__(self, x_position, speed_astronaut, surface, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect(center=(x_position, 0))
        self.speed = speed_astronaut
        self.add(group)

    def update(self, spaceship):
        if self.rect.y < spaceship.rect.bottom:
            self.rect.y += self.speed
        else:
            self.kill()


astronaut_imgs = (
    {'path': 'astronaut.png'},
)

astronaut_surface = [pygame.image.load('images/' + file['path']) for file in astronaut_imgs]


def create_astronaut(astronauts, astronaut_surface, WIDTH):
    indx = randint(0, len(astronaut_surface) - 1)
    x_position = randint(20, WIDTH - 20)
    speed_astronaut = randint(1, 2)
    return Astronaut(x_position, speed_astronaut, astronaut_surface[indx], astronauts)