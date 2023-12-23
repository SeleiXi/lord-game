# 【待完成】 / # 需改

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
pygame.display.set_caption('靈道源尊')
# f = pygame.font.SysFont("",30)
f = pygame.font.Font('Fonts/MiSans-Heavy.ttf',40)
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
enemy_1 = pygame.image.load("icons/enemy_1.jpg")
enemy_1 = pygame.transform.scale(enemy_1,(50,50))
enemy_2 = pygame.image.load("icons/enemy_2.jpg")
enemy_2 = pygame.transform.scale(enemy_2,(50,50))
mini_XUANer = pygame.transform.scale(XUANer,(50,50))
mini_dover = pygame.transform.scale(dover,(50,50))
main_page_rect = main_page.get_rect()


from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
class Stats:
    # 治療面板
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
# from threading import Thread
# thread = Thread(target=cure_interface)
# thread.start()




# 友軍/操作角色對象
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
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

class enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 490
# 新增
# 文本輸入框            
class InputBox:
    def __init__(self, rect: pygame.Rect = pygame.Rect(100, 100, 140, 32)) -> None:
        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')  # 未被選中的顏色
        self.color_active = pygame.Color('dodgerblue2')  # 被選中的顏色
        self.color = self.color_inactive  # 當前顏色，初始為未激活顏色
        self.active = False
        self.text = ''
        self.done = False
        self.font = pygame.font.Font(None, 32)
        self.finish = False

    def dealEvent(self, event: pygame.event.Event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(self.boxBody.collidepoint(event.pos)):  # 若按下鼠標且位置在文本框
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if(
                self.active) else self.color_inactive
        if(event.type == pygame.KEYDOWN):  # 鍵盤輸入響應
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
            self.text, True, self.color)  # 文字轉換為圖片
        width = max(200, txtSurface.get_width()+10)  # 當文字過長時，延長文本框
        self.boxBody.w = width
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))
        pygame.draw.rect(screen, self.color, self.boxBody, 2)



def watching_mode():
    # 需改 ， 之後改為遠程放大一下整個地圖
    global frequency,main_page_exists,all_sprites,num_list,choosing,choosing_start
    # text = f_small.render(str(enemy_list),True,(0,0,255))
    text = f.render(str(enemy_list),True,(0,100,255))
    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 2))
    # 需改
    screen.blit(text,(0,height-30))
    if main_page_exists == True:                                 
        pygame.display.flip()
        time.sleep(5)
        all_sprites.update('r')
        all_sprites.update('l')
    else:
        pygame.display.flip()
        time.sleep(5)
        inputbox = InputBox(pygame.Rect(150, 450, 10, 32)) 
        inputbox2 = InputBox(pygame.Rect(450, 450, 10, 32)) 
        screen.blit(selecting_page,(0,0))
        inputbox.draw(screen)
        inputbox2.draw(screen)
        choosing = True
        choosing_start = True
def choosing_mode_entering():
    global num_list,choosing,choosing_start,inputbox,inputbox2
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
start_button = (pygame.Rect(280, 270, 234, 60))
setting_finish = False
choosing = False
First_run = False
money = 1000
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
enemy_x_position = []
for i in range(1,7+1):
    enemy_x_position.append((width//7)*i)
print(enemy_x_position)
for random_enemy_frequency in range(7):
    x = random.randint(1,2)
    if x == 1:
        enemy_list.append("enemy_1")
    else:
        enemy_list.append("enemy_1")

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
            text = f.render("輸入兵種數目並輸入enter(注意需要從左到右執行),輸入S重置界面",True,(0,0,50))
            text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // (1.5)))
            screen.blit(text,(0,0))
            text = f.render("輸入W進入觀察模式(檢查敵人構成),輸入F即可進入遊戲(以英文輸入法)",True,(0,0,50))
            text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
            screen.blit(text,(0,25))
            # 進入選兵頁面
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                if Watching_chance == 1 and choosing_start == True:
                    watching_mode()
                    Watching_chance -=1
                    event.key = pygame.K_s
                elif Watching_chance == 0 and main_page_exists == False:
                    text = f.render("觀察機會已耗盡",True,(0,0,50))
                    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                    screen.blit(text,(0,height-80))

        if event.type == pygame.KEYDOWN and main_page_exists == False:
            
            if event.key == pygame.K_s:
                choosing_mode_entering()

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
                            # 嵌套字典裝該角色的屬性
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
                        for enemy_name in enemy_list:
                            enemy_sample = enemy()
                            for x_position in enemy_x_position:
                                enemy_sample.rect.x = enemy_x_position
                            enemy_sample.name = enemy_name
                                                 
                                
                    else:
                        event.key = pygame.K_s
                        text = f.render("請輸入所需不超過1000金幣的兵種構成，火鴿子:$80,玄者:$100（規則在ui菜單中）",True,(0,0,50))
                        text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                        screen.blit(text,(0,height-60))
                except:
                    print(Exception)
        # 通過點擊圖標進入【待完成】
        # if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos) and choosing == False and main_page_exists == False:
        #     choosing_mode_entering()
            

        # 進入主程序
        if event.type == pygame.KEYDOWN and main_page_exists == True:
            if First_run == False:
                all_sprites = pygame.sprite.Group()
                if dover_list == []:
                    player = Player(XUANer)
                    all_sprites.add(player)
                    # 此處需要Blit一個sprite
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

                            break
                        elif key.startswith("B"):
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

        # 按住走路不放的奔跑功能實現
        if right_move_status == True and move_status == True:
            # 模型轉變為向右（圖片改變）
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
            for enemy in enemy_list:
                pass
    pygame.display.flip() 



