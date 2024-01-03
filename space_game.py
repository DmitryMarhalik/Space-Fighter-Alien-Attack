import pygame, controls
from spaceship import SpaceShip
from pygame.sprite import Group
from statistics import Statistics
from scores import Scores
from live import Lives


def run():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    FPS = 60  # количество кадров в секунду
    WIDTH = 1280
    HEIGHT = 720
    pygame.mixer.music.load('sounds/music.mp3')
    pygame.mixer.music.play(-1, 27.0, 4000)
    pygame.mixer.music.set_volume(0.3)

    hit = pygame.mixer.Sound('sounds/bang.ogg')
    hit.set_volume(0.4)
    crush = pygame.mixer.Sound('sounds/crush_spaceship.ogg')
    crush.set_volume(0.5)
    level=pygame.mixer.Sound('sounds/level.ogg')
    level.set_volume(0.5)

    icon = pygame.image.load('images/icon.png')
    background_image = pygame.image.load('images/space.png')
    level_failed = pygame.image.load('images/level_failed.png')
    you_died = pygame.image.load('images/you_died.jpg')

    pygame.display.set_icon(icon)
    pygame.display.set_caption('Space Fighter: Alien Attack')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
            controls.update(background_image, screen, stats, scs, spaceship, ufos, rockets, lives)
            controls.update_ufos(stats, screen, spaceship, ufos, rockets, level_failed, you_died, crush, level)
            controls.update_rockets(stats, scs, ufos, rockets, hit)
            clock.tick(FPS)


run()
