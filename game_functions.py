import sys, pygame


def check_keydown_events(event, ship):
    # Проверка нажатия клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_reight = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    # Обработка отпускани клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_reight = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    #Обработка нажатий клавиш и событий мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Проверка нажата ли клавиша
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
                

def update_screen(ai_setting, screen, ship):
    #Обнавляет изображение на экране и отображает новый экран
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    #Отображение последнего прорисованного экрана
    pygame.display.flip()