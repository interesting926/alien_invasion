import sys
import pygame
from ship import Ship
import game_function as gf
from settings import settings



def run_game():
    ai_settings = settings()
    #初始化游戏并且创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption(ai_settings.game_name)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #开始游戏主循环
    while True:
        #检查pygame事件
        gf.check_events(ship)   
        ship.update()     
        gf.update_screen(ai_settings,screen,ship)

run_game()
