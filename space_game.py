import pygame, controls
from spaceship import SpaceShip
from pygame.sprite import Group
from statistics import Statistics
from scores import Scores
from live import Lives


def run():
    pygame.init()
    FPS = 60

    icon = pygame.image.load('images/icon.png')
    background_image = pygame.image.load('images/space.png')
    level_failed = pygame.image.load('images/level_failed.png')
    you_died = pygame.image.load('images/you_died.jpg')

    pygame.display.set_icon(icon)
    pygame.display.set_caption('Space Fighter: Alien Attack')
    screen = pygame.display.set_mode((1280, 720))

    clock = pygame.time.Clock()

    spaceship = SpaceShip(screen)
    rockets = Group()
    ufos = Group()
    lives = Lives(screen)
    controls.create_ufos_army(screen, ufos)
    stats = Statistics()
    scs = Scores(screen, stats)

    while True:
        controls.events(screen, spaceship, rockets)
        if stats.play_game:
            spaceship.update_position()
            controls.update_rockets(stats, scs, ufos, rockets)
            controls.update_ufos(stats, screen, spaceship, ufos, rockets, level_failed, you_died)
            controls.update(background_image, screen, stats, scs, spaceship, ufos, rockets, lives)
            clock.tick(FPS)


run()
