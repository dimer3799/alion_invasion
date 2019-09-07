import pygame

class Ship():
    def __init__(self, screen):
        #Инизилиазируем корабль и задаем начальную точку
        self.screen = screen
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()#Получение прямоугольника
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #Рисуем корабль в текущей позиции
        self.screen.blit(self.image, self.rect)