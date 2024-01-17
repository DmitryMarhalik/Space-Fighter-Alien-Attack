import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, screen):
        """инициализация космического корабля"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rectangle = screen.get_rect()
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.center = self.screen_rectangle.centerx  # положение внизу по оси X
        self.rect.bottom = self.screen_rectangle.bottom  # положение внизу по оси Y
        self.move_right = False
        self.move_left = False

    def output(self):
        """рисование космического корабля"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """обновление позиции космического корабля"""
        if self.move_right and self.rect.right < self.screen_rectangle.right:
            self.center += 10.5
        elif self.move_left and self.rect.left > 0:  # self.screen_rectangle.left:
            self.center -= 10.5
        self.rect.centerx = self.center

    def create_spaceship(self):
        """размещение космического корабля по центру внизу экрана"""
        self.center = self.screen_rectangle.centerx
