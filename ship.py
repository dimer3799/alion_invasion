import pygame

class Ship():
    def __init__(self, ai_setting, screen):
        #Инизилиазируем корабль и задаем начальную точку
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()#Получение прямоугольника
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_reight = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        # Обнавление позиции корабля с учетом флага
        if self.moving_reight and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):
        #Рисуем корабль в текущей позиции
        self.screen.blit(self.image, self.rect)