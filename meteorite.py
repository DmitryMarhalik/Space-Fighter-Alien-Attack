import pygame


class Meteorit(pygame.sprite.Sprite):
    def __init__(self, x_position, speed_garbage, surface, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect(center=(x_position, 0))
        self.speed = speed_garbage
        self.add(group)

    def update(self, screen_height):
        if self.rect.y < screen_height:
            self.rect.y += self.speed
        else:
            self.kill()
