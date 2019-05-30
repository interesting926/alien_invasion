import sys
import pygame


def check_key_down(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_righ = True               
    elif event.key == pygame.K_LEFT:   
        ship.moving_left = True

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_righ = False 
    elif event.key == pygame.K_LEFT:   
        ship.moving_left = False   

def check_events(ship):
    ''' 相应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

        elif event.type == pygame.KEYDOWN:
            check_key_down(event,ship)

        elif event.type == pygame.KEYUP:
            check_key_up(event,ship)   
                


def update_screen(ai_settings,screen,ship):
    ''' 更新屏幕上的图像并且切换到新的屏幕 '''
    #每次循环都要重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.biltme()
    pygame.display.flip()
