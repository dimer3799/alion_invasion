import pygame
from pygame.sprite import Sprite


class Alian(Sprite):
    # Класс, представляющий одного пришельца
    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        # Загрузка пришельца
        self.image = pygame.image.load('alion.png')
        self.rect = self.image.get_rect()
        # Каждый новый появляется в верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции
        self.x = float(self.rect.x)

    def blitme(self):
        # Выводим пришельца в текущем положении
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # Возвращакт True если пришелец достиг края
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Перемещение влево или вправо
        self.x += (self.ai_setting.alian_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x