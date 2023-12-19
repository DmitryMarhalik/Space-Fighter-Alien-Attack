class Statistics():
    """отслеживание статистики"""
    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.play_game = True
        with open('highscore.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.lives = 3
        self.score = 0

