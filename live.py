import pygame
from pygame.sprite import Sprite


class Lives(Sprite):
    def __init__(self, screen):
        """инициализация картинки для одной жизни"""
        super(Lives, self).__init__()
        self.screen = screen
        self.screen_rectangle = screen.get_rect()
        self.image = pygame.image.load('images/spaceship_lives.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def output(self):
        """отрисовка одной жизни"""
        self.screen.blit(self.image, self.rect)
