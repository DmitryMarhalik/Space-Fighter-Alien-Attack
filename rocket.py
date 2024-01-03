import pygame


class Rocket(pygame.sprite.Sprite):
    def __init__(self, screen, spaceship):
        """создание ракеты"""
        pygame.sprite.Sprite.__init__(self)  # super(Rocket, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.speed = 4.5
        self.rect.centerx = spaceship.rect.centerx
        self.rect.centery = spaceship.rect.top
        self.y = float(self.rect.y)
        self.press = False

    def update(self):
        """перемещение ракеты вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def output(self):
        """отрисовка ракеты на экране"""
        self.screen.blit(self.image, self.rect)
