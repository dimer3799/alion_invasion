class Setting():
    #Класс для хранения настроек игры
    def __init__(self):

        #Параметры экрна
        self.screen_width = 1200
        self.screen_heigth = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowd = 10
        
        # Настройка скорости прищельца
        self.alian_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 вправо, -1 влево 