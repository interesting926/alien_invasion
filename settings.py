class settings():
    '''存储《外星人入侵》的所有设置 '''
    def __init__(self):
        self.bg_color = (230,230,230)
        self.screen_width = 800
        self.screen_hight = 600
        self.game_name = 'alien_invasion'
        self.ship_speed_factor = 1.5
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width =3
        self.bullet_hight = 15
        self.bullet_color =255,00,00
