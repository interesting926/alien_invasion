class settings():
    '''存储《外星人入侵》的所有设置 '''
    def __init__(self):
        self.bg_color = (230,230,230)
        self.screen_width = 1200
        self.screen_hight = 800
        self.game_name = 'alien_invasion'
        self.ship_speed_factor = 1.5
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (255,00,00)
        self.bullet_allow = 3
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed =10
        # fleet_direction =1右移动 -1左移动
        self.fleet_direction =1
