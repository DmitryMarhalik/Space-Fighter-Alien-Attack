import pygame


def config_sound(file, volume):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(volume)
    return sound
