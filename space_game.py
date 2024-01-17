import pygame, controls

from spaceship import SpaceShip
from pygame.sprite import Group
from statistics import Statistics
from text_images import Scores, NextLevel
from live import Lives
from set_sound import config_sound

WIDTH = 1280
HEIGHT = 720
FPS = 60  # количество кадров в секунду


def run():
    """
    Запуск игрового цикла.
    """
    # Инициализация pygame и mixer
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, 3000)
    pygame.time.set_timer(pygame.USEREVENT + 1, 13000)

    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load('sounds/bg_music.mp3')
    pygame.mixer.music.play(-1, 27.0, 4000)
    pygame.mixer.music.set_volume(0.2)

    # Загрузка и настройка звуковых эффектов
    miss_astronaut = config_sound('sounds/miss_astronaut.mp3')
    safe = config_sound('sounds/yes.mp3')
    shoot = config_sound('sounds/shoot.mp3', volume=0.2)
    hit = config_sound('sounds/hit.mp3')
    crush = config_sound('sounds/crush_spaceship.mp3')
    next_level = config_sound('sounds/next_level.mp3')
    game_over = config_sound('sounds/game_over.mp3')

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Загрузка изображений
    icon = pygame.image.load('images/icon.png').convert_alpha()
    bg_image = pygame.image.load('images/space.png').convert_alpha()
    level_failed = pygame.image.load('images/level_failed.png').convert_alpha()
    you_died = pygame.image.load('images/you_died.jpg').convert_alpha()

    # Установка свойств окна игры
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Space Fighter: Aliens Attack')
    clock = pygame.time.Clock()

    # Создание игровых объектов
    spaceship = SpaceShip(screen)
    rockets = Group()
    ufos = Group()
    astronauts = Group()
    meteorites = Group()
    lives = Lives(screen)
    stats = Statistics()
    scs = Scores(screen, stats)
    msg_next_level = NextLevel(screen)
    controls.create_ufos_army(screen, ufos)

    while True:
        # Обработка событий
        controls.events(screen, spaceship, rockets, shoot, meteorites, astronauts, WIDTH)
        if stats.play_game:
            # Обновление положение космического корабля
            spaceship.update_position()
            # Обновление пришельцев
            controls.update_ufos(stats, screen, spaceship, ufos, rockets, level_failed, you_died, crush, next_level,
                                 msg_next_level, game_over, bg_image, astronauts, meteorites)
            # Обновление позиции объектов
            controls.update_objects_positions(stats, spaceship, scs, ufos, rockets, hit, astronauts, meteorites, safe,
                                              miss_astronaut)
            # Обновление экрана
            controls.update(bg_image, screen, stats, scs, spaceship, ufos, rockets, lives, astronauts, meteorites,
                            HEIGHT)
            clock.tick(FPS)


run()
