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