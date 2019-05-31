import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图片并获取其外接矩形
        self.image = pygame.image.load("alien_invasion/image/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #移动标志
        self.moving_righ = False
        self.moving_left = False

        #将每艘新飞船放置在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom 

        #在飞船center属性中存储小数值
        self.center = float(self.rect.centerx)


    def update(self):
        if self.moving_righ == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor


        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)