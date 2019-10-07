import sys, pygame
from bullet import Bullet
from alian import Alian

def check_keydown_events(event, ai_setting, screen, ship, bullets):
    # Проверка нажатия клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_reight = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()        

def check_keyup_events(event, ship):
    # Обработка отпускани клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_reight = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events( ai_setting, screen, ship, bullets):
    #Обработка нажатий клавиш и событий мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Проверка нажата ли клавиша
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_setting, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
                

def update_screen(ai_setting, screen, ship, alians, bullets):
    #Обнавляет изображение на экране и отображает новый экран
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #alian.blitme()
    alians.draw(screen)
    #Отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # Удаление пуль вышешедших за край
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_setting, screen, ship, bullets):
    # Создание новой пули и включение ее в групу bullets
    if len(bullets) < ai_setting.bullets_allowd:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def get_number_alians_x(ai_setting, alian_width):
    available_space_x = ai_setting.screen_width - 2* alian_width
    number_alians_x = int(available_space_x/(2*alian_width))
    return number_alians_x

def create_alian(ai_setting, screen, alians, alian_number, row_number):
    # Создание флота пришельцев
    alian = Alian(ai_setting, screen)
    alian_width = alian.rect.width
    alian.x = alian_width+2*alian_width*alian_number
    alian.rect.x = alian.x
    alian.rect.y = alian.rect.height + 2 * alian.rect.height * row_number

    alians.add(alian)

def create_fleet(ai_setting, screen, ship, alians):   
    # Создание первого ряда пришельцев
    alian = Alian(ai_setting, screen)
    number_alians_x = get_number_alians_x(ai_setting, alian.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alian.rect.height)
    for row_number in range(number_rows):
        for alian_number in range(number_alians_x):
            # Создание пришельца и размещение его в ряду
            create_alian(ai_setting, screen, alians, alian_number, row_number)
        
def get_number_rows(ai_setting, ship_height, alien_height):
    # Определяем количество рядов помещяющихся на экране
    available_space_y = (ai_setting.screen_heigth - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_alians(ai_setting, alians):
    # Обнавляем позиции пришельцев
    check_fleet_edges(ai_setting, alians)
    alians.update()

def check_fleet_edges(ai_setting, alians):
    # Опускаем флот и меняем напраление
    for alian in alians.sprites():
        if alian.check_edges():
            chenge_fleet_direction(ai_setting, alians)
            break

def chenge_fleet_direction(ai_setting, alians):
    for alian in alians.sprites():
        alian.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1
