import pygame.font

text_color = (136, 223, 142)
high_score_color = (255, 255, 0)


class Scores():
    """вывод игровой информации"""

    def __init__(self, screen, stats):
        """инициализация подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = text_color
        self.font = pygame.font.SysFont('kalapi', 40)
        self.image_score()
        self.image_high_score()

    def image_score(self):
        """преобразование текста счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), 1, self.text_color, None)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 0

    def image_high_score(self):
        """преобразование рекорда в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score),
                                                 1, high_score_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
