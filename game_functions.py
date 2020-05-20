import sys, pygame
from bullet import Bullet
from alian import Alian
from time import sleep


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


def check_events(ai_setting, screen, ship, bullets, stats, play_button, aliens):
    #Обработка нажатий клавиш и событий мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Проверка нажата ли клавиша
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_setting, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_buttons(ai_setting, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
               

def check_play_buttons(ai_setting, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # Запускаем игру при нажатии на Play
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True

        # Очищение списков прищельцев и пуль
        aliens.empty()
        bullets.empty()

        #Создание нового флота и размещеие корабля в центре
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_setting, screen, ship, alians, bullets, play_button, stats):
    #Обнавляет изображение на экране и отображает новый экран
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #alian.blitme()
    alians.draw(screen)
    # Кнопка Play отображается в том случае, если игра неактивна
    if not stats.game_active:
        play_button.draw_button()
    #Отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(ai_setting, screen, ship, alians, bullets):
    bullets.update()
    # Удаление пуль вышешедших за край
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, ship, alians, bullets) 

def check_bullet_alien_collisions(ai_setting, screen, ship, alians, bullets):
    # Обработка коллизий пул с пришельцами
    collisions = pygame.sprite.groupcollide(bullets, alians, True, True)
    if len(alians) == 0:
        # Уничтожение существующих пуль и создание нового флота
        bullets.empty()
        create_fleet(ai_setting, screen, ship, alians)

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

def update_alians(ai_setting, stats, screen, ship, alians, bullets):
    # Обнавляем позиции пришельцев
    check_fleet_edges(ai_setting, alians)
    alians.update()
    # Проверка коллизий пришелец и корабль
    if pygame.sprite.spritecollideany(ship, alians):
        ship_hit(ai_setting, stats, screen, ship, alians, bullets)

    # Проверка пришельцев, достигших нижнего края
    check_aliens_bottom(ai_setting, stats, screen, ship, alians, bullets)

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


def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
    #Обработка столкновения пришельца с кораблем
    # Уменьшаем количество кораблей
    if stats.ship_left >0:
        stats.ship_left -= 1

        #Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty() 

        #Создание нового флота
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

        # Пауза
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    # Проверка добрались ли прищельцы до нижнего края
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break