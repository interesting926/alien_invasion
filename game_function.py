import sys
import pygame
from bullet import Bullet


def check_key_down(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_righ = True               
    elif event.key == pygame.K_LEFT:   
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        #print('增加子弹')

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
                


def update_screen(ai_settings,screen,ship,bullets):
    ''' 更新屏幕上的图像并且切换到新的屏幕 '''
    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #每次循环都要重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.biltme()
    pygame.display.flip()



