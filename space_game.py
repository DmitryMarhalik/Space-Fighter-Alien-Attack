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

    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load('sounds/bg_music.mp3')
    pygame.mixer.music.play(-1, 27.0, 4000)
    pygame.mixer.music.set_volume(0.2)

    # Загрузка и настройка звуковых эффектов
    shoot = config_sound('sounds/shoot.mp3')
    hit = config_sound('sounds/bang.ogg')
    crush = config_sound('sounds/crush_spaceship.ogg')
    next_level = config_sound('sounds/level.ogg')
    game_over = config_sound('sounds/game_over.mp3')

    # Загрузка изображений
    icon = pygame.image.load('images/icon.png')
    bg_image = pygame.image.load('images/space.png')
    level_failed = pygame.image.load('images/level_failed.png')
    you_died = pygame.image.load('images/you_died.jpg')

    # Установка свойств окна игры
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Space Fighter: Aliens Attack')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Создание игровых объектов
    spaceship = SpaceShip(screen)
    rockets = Group()
    ufos = Group()
    lives = Lives(screen)
    stats = Statistics()
    scs = Scores(screen, stats)
    msg_next_level = NextLevel(screen)
    controls.create_ufos_army(screen, ufos)

    while True:
        # Обработка событий
        controls.events(screen, spaceship, rockets, shoot)
        if stats.play_game:
            # Обновление положение космического корабля
            spaceship.update_position()
            # Обновление пришельцев
            controls.update_ufos(stats, screen, spaceship, ufos, rockets, level_failed, you_died, crush, next_level,
                                 msg_next_level, game_over, bg_image)
            # Обновление ракет и очков
            controls.update_rockets(stats, scs, ufos, rockets, hit)
            # Обновление экрана
            controls.update(bg_image, screen, stats, scs, spaceship, ufos, rockets, lives)
            clock.tick(FPS)


run()
