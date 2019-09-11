import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # Создаем объект bullet в текущей позиции корабля
    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0.0) и назначение правильной позиции
        self.rect = pygame.Rect(0,0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        # Перемещение пули вверх по экрану

        self.y -= self.speed_factor
        # Обнавление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        # Вывод пули на экран
        pygame.draw.rect(self.screen, self.color, self.rect)