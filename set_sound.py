import pygame


def config_sound(file: str, volume: float) -> pygame.mixer.Sound:
    """ Настраивает звуковой файл с определенной громкостью.
    Args:
        file (str): Путь к звуковому файлу.
        Volume (float): Уровень громкости звука.
    Return:
        pygame.mixer.Sound: настроенный звуковой объект.
    """
    sound = pygame.mixer.Sound(file)
    sound.set_volume(volume)
    return sound
