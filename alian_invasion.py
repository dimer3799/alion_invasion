import sys
import pygame
from setting import Setting
from ship import Ship
from alian import Alian
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # Инизилизируем игру и моздаем объект экран
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_heigth))
    pygame.display.set_caption('Game by Dimer v1.0')
    stats = GameStats(ai_setting)
    ship = Ship(ai_setting,screen)
    alian = Alian(ai_setting, screen)
    #Создание группы пуль для хранения
    bullets = Group()
    alians = Group()
    gf.create_fleet(ai_setting, screen, ship, alians)
    while True:      
        gf.check_events(ai_setting, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, alians, bullets)
            gf.update_alians(ai_setting, stats, screen, ship, alians, bullets)
        # print(len(bullets)) # Вывод в терминале склько пуль на экране
        gf.update_screen(ai_setting, screen, ship, alians, bullets)



run_game()    

#276 Обработка столкновений с кораблем