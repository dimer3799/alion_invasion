class GameStats():
    def __init__(self, ai_settings):
        # Игра запускается при активном состоянии
        self.game_active = True
        
        # Статистика
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        # Инициализируем статистику, изменяющуюся в ходе игры
        self.ship_left = self.ai_settings.ship_limit