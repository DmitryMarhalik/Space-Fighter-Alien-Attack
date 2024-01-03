import pygame


class Ufo(pygame.sprite.Sprite):
    """класс одного пришельца"""
    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()
        self.speed = 0.9
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение пришельцев"""
        self.y += self.speed
        self.rect.y = self.y
