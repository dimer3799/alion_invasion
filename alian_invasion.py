import sys
import pygame
from setting import Setting

def run_game():
    # Инизилизируем игру и моздаем объект экран
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_heigth))
    pygame.display.set_caption('Game by Dimer v1.0')
    bg_color = (230,230,230)
    while True:
        screen.fill(ai_setting.bg_color)
        #Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()    
