import sys
import pygame
from ship import Ship
import game_function as gf
from settings import settings
from pygame.sprite import Group


def run_game():
    ai_settings = settings()
    #初始化游戏并且创建一个屏幕对象
    pygame.init() 
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption(ai_settings.game_name)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    bullets = Group()
    #pygame.draw.rect(screen,(200,00,00),((200,200),(10,10)))
    #开始游戏主循环
    while True:
        #检查pygame事件
        gf.check_events(ai_settings,screen,ship,bullets)   
        ship.update() 
        bullets.update()    
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
