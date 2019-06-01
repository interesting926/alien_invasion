import sys
import pygame
from bullet import Bullet
from alien import Alien


def first_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allow:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        #print('增加子弹')

def check_key_down(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_righ = True               
    elif event.key == pygame.K_LEFT:   
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        first_bullet(ai_settings,screen,ship,bullets)
    #测试时使用Q结束测试
    elif  event.key == pygame.K_q:   
        sys.exit()

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_righ = False 
    elif event.key == pygame.K_LEFT:   
        ship.moving_left = False   

def check_events(ai_settings,screen,ship,bullets):
    ''' 相应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

        elif event.type == pygame.KEYDOWN:
            check_key_down(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_key_up(event,ship)   
                


def update_bullets(aliens,bullets):
    bullets.update() 
    for bullte in bullets.copy():
        if bullte.rect.bottom <= 0:
            bullets.remove(bullte) 
    colisions = pygame.sprite.groupcollide(aliens,bullets,True,True)



def update_screen(ai_settings,screen,ship,aliens,bullets):
    ''' 更新屏幕上的图像并且切换到新的屏幕 '''
    #每次循环都要重新绘制屏幕
    screen.fill(ai_settings.bg_color)

    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def get_number_rows(ai_settings,ship_height,alein_height):
    """ 计算屏幕可容纳多少行外星人"""
    availabe_space_y = (ai_settings.screen_hight - (3 * alein_height) - ship_height)
    number_row = int(availabe_space_y / (2 * alein_height))
    return number_row


def get_number_alien_x(ai_settings,alien_width):
    """计算每行可容纳多少外星人"""
    availabe_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(availabe_space_x / (2 * alien_width))
    return number_alien_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放入当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def creat_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人并且计算可容纳多少外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    number_alien_width = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)

    #打印测试信息
    print("行数 %d 列数 %d",(number_alien_width,number_rows))
    for row_number in range(number_rows):
        for alien_number in range(number_alien_width):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    #外星人到达边缘并采取相应措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):  
    """将整群外星人下移， 并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,ship,aliens):
    #更新外星人群中所有外星人位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测飞船是否和外星人碰撞了
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
