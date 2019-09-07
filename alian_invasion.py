import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
    # Инизилизируем игру и моздаем объект экран
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_heigth))
    pygame.display.set_caption('Game by Dimer v1.0')
    ship = Ship(ai_setting,screen)
    while True:      
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting,screen,ship)


run_game()    
