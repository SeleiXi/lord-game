# first version

import sys
import pygame
pygame.init()
width = 800
height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((width,height),flags=0)
surface = screen
icon = pygame.image.load("icons/chigua.png").convert()
start_menu = pygame.image.load("icons/start_menu.png").convert()
pygame.display.set_icon(icon)
pygame.display.set_caption('灵道源尊')
# f = pygame.font.SysFont("",30)
f = pygame.font.Font('Fonts/MiSans-Heavy.ttf',30)
f_small = pygame.font.Font('Fonts/MiSans-Heavy.ttf',20)
screen.blit(start_menu,(0,0))
import time
clock = pygame.time.Clock()
main_page_exists = False
main_page = pygame.image.load("icons/main_page.png").convert()
money_pic = pygame.image.load("icons/money.png").convert()
dover_original = pygame.image.load("icons/dover.png")
selecting_page = pygame.image.load("icons/selecting_page.png")
dover = pygame.transform.scale(dover_original,(80,70))
XUANer = pygame.image.load("icons/XUANer.png")
XUANer = pygame.transform.scale(XUANer,(80,70))
mini_XUANer = pygame.transform.scale(XUANer,(50,50))
mini_dover = pygame.transform.scale(dover,(50,50))
main_page_rect = main_page.get_rect()


from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
class Stats:
    # 治疗面板
    def __init__(self):
        self.ui = QUiLoader().load('cure.ui')
        self.ui.pushButton.clicked.connect(self.cure)
            
        
    def cure(self):
        global money,character_dict
        number  = self.ui.spinBox.value()
        if number<=money:
            pass

def cure_interface():
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()
from threading import Thread
thread = Thread(target=cure_interface)
thread.start()




# 友军/操作角色对象
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 490

    def update(self,direction):
        global move_status
        if direction == 'r':
            main_page_rect.x -=3
            screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
            all_sprites.draw(screen)
        elif direction == "l":
            main_page_rect.x +=3
            screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
            all_sprites.draw(screen)

# 文本输入框            
class InputBox:
    def __init__(self, rect: pygame.Rect = pygame.Rect(100, 100, 140, 32)) -> None:
        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')  # 未被选中的颜色
        self.color_active = pygame.Color('dodgerblue2')  # 被选中的颜色
        self.color = self.color_inactive  # 当前颜色，初始为未激活颜色
        self.active = False
        self.text = ''
        self.done = False
        self.font = pygame.font.Font(None, 32)
        self.finish = False

    def dealEvent(self, event: pygame.event.Event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(self.boxBody.collidepoint(event.pos)):  # 若按下鼠标且位置在文本框
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if(
                self.active) else self.color_inactive
        if(event.type == pygame.KEYDOWN):  # 键盘输入响应
            if(self.active):
                if self.finish == False:
                    if(event.key == pygame.K_RETURN):
                        global num_list
                        try:
                            num_list.append(int(self.text))
                        except:
                            pass
                        print(num_list)
                        self.finish = True
                        # self.text=''
                    elif(event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

    def draw(self, screen: pygame.surface.Surface):
        txtSurface = self.font.render(
            self.text, True, self.color)  # 文字转换为图片
        width = max(200, txtSurface.get_width()+10)  # 当文字过长时，延长文本框
        self.boxBody.w = width
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))
        pygame.draw.rect(screen, self.color, self.boxBody, 2)



def watching_mode():
    # 需改 ， 之後改為遠程放大一下整個地圖
    global frequency,main_page_exists,all_sprites,num_list,choosing,choosing_start
    # text = f_small.render(str(enemy_list),True,(0,0,255))
    text = f.render(str(enemy_list),True,(0,0,255))
    # 需改
    screen.blit(text,(0,0))
    if main_page_exists == True:
        pygame.display.flip()
        time.sleep(5)
        all_sprites.update('r')
        all_sprites.update('l')
    else:
        pygame.display.flip()
        time.sleep(5)
        num_list = []
        inputbox = InputBox(pygame.Rect(150, 450, 10, 32)) 
        inputbox2 = InputBox(pygame.Rect(450, 450, 10, 32)) 
        screen.blit(selecting_page,(0,0))
        inputbox.draw(screen)
        inputbox2.draw(screen)
        choosing = True
        choosing_start = True

num_list = []
auto_dover_list = ['A0','A1','A2','A3','A4']
auto_XUANer_list = ['B0','B1','B2','B3',]
character_dict = {}
dover_list = []
XUANer_list = []
right_move_status = False
left_move_status = False
fullScreen = False
setting_finish = False
choosing = False
First_run = False
money = 400
enemy_list = []
pykey = {
    1:49,
    2:50,
    3:51,
    4:52,
    5:53,
}
frequency = 0
choosing_start = False
import random
for random_enemy_frequency in range(7):
    x = random.randint(1,2)
    if x == 1:
        enemy_list.append("妖弭猴")
    else:
        enemy_list.append("閃電猩")
Watching_chance = 1
last_num = 0
last_y_index = 0

while True: 
    frequency += 1
    clock.tick(60)
    current_y_position = 30
        # tiaozhuan
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if choosing == True:
            inputbox.dealEvent(event)
            inputbox.draw(screen)
            inputbox2.dealEvent(event)
            inputbox2.draw(screen)
            # 进入选兵页面
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if Watching_chance == 1 and choosing_start == True:
                    watching_mode()
        if event.type == pygame.KEYDOWN and main_page_exists == False:
            
            if event.key == pygame.K_s:
                num_list = []
                inputbox = InputBox(pygame.Rect(150, 450, 10, 32)) 
                inputbox2 = InputBox(pygame.Rect(450, 450, 10, 32)) 
                screen.blit(selecting_page,(0,0))
                inputbox.draw(screen)
                inputbox2.draw(screen)
                choosing = True
                choosing_start = True
                
                print("在输入界面记得先enter左侧输入框,以及要开英文输入法")
            elif event.key == pygame.K_f:
                try:
                    text = f.render("Text",True,(255,0,0),(0,0,0))
                    total_cost = num_list[0]*80 + num_list[1]*100
                    if total_cost <=400:
                        money -= total_cost
                        for i in range(1,num_list[0]+1):
                            dover_list.append(auto_dover_list[i])
                            HP = pygame.image.load("icons/HP.png")
                            HP = pygame.transform.scale(HP,(100,30))
                            character_dict[auto_dover_list[i]] = {}
                            # 嵌套字典装该角色的属性
                            character_dict[auto_dover_list[i]]["HP"] = HP
                            character_dict[auto_dover_list[i]]["num"] = f.render(str(i),True,(255,0,0),(0,0,0))
                            character_dict[auto_dover_list[i]]["int_num"] = i
                            character_dict[auto_dover_list[i]]["y_index"] = i*50
                            last_y_index = i*50
                            last_num = i
                        for i in range(1,num_list[1]+1):
                            XUANer_list.append(auto_XUANer_list[i])
                            HP = pygame.image.load("icons/HP.png")
                            HP = pygame.transform.scale(HP,(100,30))
                            character_dict[auto_XUANer_list[i]] = {}
                            character_dict[auto_XUANer_list[i]]["HP"] = HP
                            character_dict[auto_XUANer_list[i]]["num"] = f.render(str(i+last_num),True,(255,0,0))
                            character_dict[auto_XUANer_list[i]]["int_num"] = i+last_num
                            character_dict[auto_XUANer_list[i]]["y_index"] = i*50+last_y_index
                        setting_finish = True
                        main_page_exists = True
                        choosing = False
                        screen.blit(main_page,(0,0))
                        screen.blit(money_pic,(0,0))
                        if dover_list == []:
                            screen.blit(XUANer,(350,490))
                        else:
                            screen.blit(dover,(350,490))
                        # tiaozhuan
                    else:
                        event.key = pygame.K_s
                except:
                    print(Exception)
        # 进入主程序
        if event.type == pygame.KEYDOWN and main_page_exists == True:
            if First_run == False:
                all_sprites = pygame.sprite.Group()
                if dover_list == []:
                    player = Player(XUANer)
                    all_sprites.add(player)
                    # 此处需要Blit一个sprite
                else:
                    player = Player(dover)
                    all_sprites.add(player)
                First_run = True
            if event.key == pygame.K_F11:
                if fullScreen == False:
                    screen = pygame.display.set_mode((width,height),(pygame.FULLSCREEN))
                    fullScreen = True
                    screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                    all_sprites.draw(screen)
                else:
                    screen = pygame.display.set_mode((width,height),flags=0)
                    screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                    all_sprites.draw(screen)
                    fullScreen = False
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5:
                print(event.key)
                for key,value in character_dict.items():
                    if pykey[character_dict[key]["int_num"]] == event.key:
                        all_sprites = pygame.sprite.Group()
                        if key.startswith("A"):
                            player = Player(dover)
                            all_sprites.add(player)
                            all_sprites.update('r')
                            all_sprites.update('l')
                            # tiaozhuan
                            break
                        else:
                            player = Player(XUANer)
                            all_sprites.add(player)
                            all_sprites.update('r')
                            all_sprites.update('l')
                            
                            break
                

            if event.key == pygame.K_d:
                move_status = True
                right_move_status = True
                left_move_status = False
                all_sprites.update('r')
            if event.key == pygame.K_a:
                move_status = True
                left_move_status = True
                right_move_status = False
                all_sprites.update('l')

        # 按住走路不放的奔跑功能实现
        if right_move_status == True and move_status == True:
            all_sprites.update('r')
        if left_move_status == True and move_status == True:
            all_sprites.update('l')    
        if event.type ==  pygame.KEYUP:
            move_status = False
        for key,value in character_dict.items():
            screen.blit(money_pic,(0,0))
            screen.blit(f.render(str(money),True,(255,0,0)),(50,0))
            y_index = int(character_dict[key]["y_index"])
            text = character_dict[key]["num"]
            HP = character_dict[key]["HP"]
            if key.startswith("A"):
                screen.blit(text,(0,y_index))
                screen.blit(mini_dover,(50,y_index))
                screen.blit(HP,(100,y_index,100,50))
            else:
                screen.blit(text,(0,y_index))
                screen.blit(mini_XUANer,(50,y_index))
                screen.blit(HP,(100,y_index,50,100))
                
    pygame.display.flip() 



