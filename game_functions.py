import sys, pygame

def check_events():
    #Обработка нажатий клавиш и событий мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(ai_setting, screen, ship):
    #Обнавляет изображение на экране и отображает новый экран
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    #Отображение последнего прорисованного экрана
    pygame.display.flip()