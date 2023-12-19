import time
import pygame, sys
from random import choice, randint
from rocket import Rocket
from ufo import Ufo


def events(screen, spaceship, rockets):
    """обработка нажатий клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spaceship.move_right = True
            elif event.key == pygame.K_LEFT:
                spaceship.move_left = True
            elif event.key == pygame.K_SPACE:
                new_rocket = Rocket(screen, spaceship)
                rockets.add(new_rocket)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                spaceship.move_right = False
            elif event.key == pygame.K_LEFT:
                spaceship.move_left = False


def update(background_image, screen, stats, scs, spaceship, ufos, rockets, lives):
    """обновление экрана"""
    screen.blit(background_image, (0, 0))
    scs.show_score()
    for rocket in rockets.sprites():
        rocket.output()
    live_width = lives.rect.width
    for live_number in range(stats.lives):
        lives.x = 10 + (live_width * live_number * 1.3)
        lives.y = 10
        lives.rect.x = lives.x
        lives.rect.y = lives.y
        lives.output()
    ufos.draw(screen)
    spaceship.output()
    pygame.display.flip()


def update_rockets(stats, scs, ufos, rockets):
    """обновление позиции ракет"""
    rockets.update()
    for rocket in rockets:  # ...in rockets.copy()
        if rocket.rect.bottom <= 0:
            rockets.remove(rocket)
    collisions = pygame.sprite.groupcollide(rockets, ufos, True, True)
    if collisions:
        for ufos in collisions.values():
            stats.score += 1 * len(ufos)
        scs.image_score()
        check_high_score(stats, scs)


count_clear_level = 0


def update_ufos(stats, screen, spaceship, ufos, rockets, level_failed, you_died):
    """обновляет позицию пришельцев"""
    ufos.update()
    global count_clear_level
    if len(ufos) == 0:
        count_clear_level += 0.05  # повышение скорости нового уровня при успешном прохождении предыдущего
        speed = count_clear_level
        rockets.empty()
        create_ufos_army(screen, ufos, speed=speed)

    speed = count_clear_level
    ufos_bottom_line(stats, screen, spaceship, ufos, rockets, speed, level_failed, you_died)


def create_ufos_army(screen, ufos, speed=0):
    """создание армии космических кораблей пришельцев"""
    ufo = Ufo(screen)
    ufo_width = ufo.rect.width
    counts_ufo_x = int((1280 / ufo_width))
    ufo_height = ufo.rect.height
    counts_ufo_y = int((720 - 100 - 2 * ufo_height) / ufo_height)
    for row_number in range(counts_ufo_y - 1):
        counts_empty_places = (randint(0, counts_ufo_x - 1))  #
        empty_position = [choice(range(counts_ufo_x)) for _ in range(counts_ufo_x - counts_empty_places)]
        # случайный выбор количества пришельцев в одном ряду (для красоты)
        for ufo_number in range(counts_ufo_x):
            ufo = Ufo(screen)
            ufo.speed += speed
            if ufo_number in empty_position:
                continue
            ufo.x = 0.5 * ufo_width + (ufo_width * ufo_number)
            ufo.y = ufo_height + (ufo_height * row_number)
            ufo.speed += speed
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.y
            ufos.add(ufo)


def spaceship_kill(stats, screen, spaceship, ufos, rockets, speed, level_failed, you_died):
    """изменения при столкновение космического корабля и пришельца"""
    stats.lives -= 1
    if stats.lives > 0:
        screen.blit(level_failed, (0, 0))
        pygame.display.flip()
        time.sleep(5)
        ufos.empty()
        rockets.empty()
        create_ufos_army(screen, ufos, speed=speed)
        spaceship.create_spaceship()
    else:
        screen.blit(you_died, (160, 0))
        pygame.display.flip()
        time.sleep(5)
        stats.play_game = False
        sys.exit()


def ufos_bottom_line(stats, screen, spaceship, ufos, rockets, speed, level_failed, you_died):
    """проверка, дошли ли пришельцы до линии космического корабля"""
    for ufo in ufos.sprites():
        if ufo.rect.bottom == spaceship.rect.top:
            spaceship_kill(stats, screen, spaceship, ufos, rockets, speed, level_failed, you_died)
            break


def check_high_score(stats, scs):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scs.image_high_score()
        with open('highscore.txt', 'w') as file:
            file.write(str(stats.high_score))
