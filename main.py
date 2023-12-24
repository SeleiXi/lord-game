# 【待完成】 / # 需改
# 不規範處：部分用駝峰命名法，部分變量如XUANer不符合命名法，branch名字應該改為master，部分地方可以函數化


# bug：173行fight函數，有時候會默認到最後一個num，導致判定是最後一個角色減血
# +切換時扣血的仍然是最後一個

# bug：player被刪除後，應該自動切換到下一個角色（重新draw一個？）


# 重要
# 增加函數和意思模糊的變量的注釋

# 可增加處/改善處
# 修改背景介紹減少中二化
# 選兵不需要從左到右
# 添加音樂
# 第一個圖標後面有黑色背景
# menu增加更多東西
# 選兵界面字體太粗，看不清
# 本地自動儲存通關記錄txt
# 有可能5轮也有可能六轮
# 做BGM以及配音
# 增加不同的模式

import sys
import pygame
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import time
import random
# from threading import Thread

# 初始化各個值以及加載圖片
pygame.init()
width = 800
height = 600
map_width = 3200
map_height = 600
screen = pygame.display.set_mode((width,height),flags=0)
surface = screen
icon = pygame.image.load("icons/chigua.png").convert() # 唔convert都得，convert後理論畫質更好
start_menu = pygame.image.load("icons/start_menu.png").convert()
pygame.display.set_icon(icon)
pygame.display.set_caption('靈道源尊')
# f = pygame.font.SysFont("",30)
f = pygame.font.Font('fonts/MiSans-Heavy.ttf',40)
f_small = pygame.font.Font('fonts/MiSans-Heavy.ttf',20)
screen.blit(start_menu,(0,0))
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
# 用作上方的圖標顯示
mini_XUANer = pygame.transform.scale(XUANer,(50,50))
mini_dover = pygame.transform.scale(dover,(50,50))
main_page_rect = main_page.get_rect()
HP = pygame.image.load("icons/HP.png")
HP = pygame.transform.scale(HP,(100,30))


# class Stats:
#     # 治療面板（已取消，呢個版本唔設置cure function）
#     def __init__(self):
#         self.ui = QUiLoader().load('cure.ui')
#         self.ui.pushButton.clicked.connect(self.cure)
            
        
#     def cure(self):
#         global money,character_dict
#         number  = self.ui.spinBox.value()
#         if number<=money:
#             pass

# def cure_interface():
#     app = QApplication([])
#     stats = Stats()
#     stats.ui.show()
#     app.exec_()

# thread = Thread(target=cure_interface)
# thread.start()




# 友軍/操作角色對象
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        # 友軍角色的xy坐標都需要始終處於地圖中央
        self.rect.x = 350
        self.rect.y = 490

    # 根據移動的方向（通過鍵盤輸入a/d檢測）來移動地區的x坐標，從而實現移動
    def update(self,direction):
        global move_status
        if direction == 'r':
            if not main_page_rect.x<-3200:
                main_page_rect.x -=3
                screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                all_sprites.draw(screen)
                for enemy_sample in enemy_sample_list:
                    enemy_sample.rect.x -=3
            else:
                win_ending()

        elif direction == "l":
            if not main_page_rect.x>150:
                main_page_rect.x +=3
                screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                all_sprites.draw(screen)
                for enemy_sample in enemy_sample_list:
                    enemy_sample.rect.x +=3
            # 設置最左邊邊界（main_page_rect.x>150），不需要設置右邊，因為到右邊的某個點自動會結算遊戲
            else:
                main_page_rect.x = 150
                x = 0
                for enemy_sample in enemy_sample_list:
                    enemy_sample.rect.x = enemy_x_position[x]+150
                    x += 1
        
class enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 490
        # 不添加x坐標,因為每個enemy的x坐標都不一樣

class InputBox:
    # 文本輸入框(選兵界面的)
    def __init__(self, rect: pygame.Rect = pygame.Rect(100, 100, 140, 32)) -> None:
        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')  
        self.color_active = pygame.Color('dodgerblue2') 
        self.color = self.color_inactive  
        self.active = False
        self.text = ''
        self.done = False
        self.font = pygame.font.Font(None, 32)
        self.finish = False
    # 當點擊框的時候進行的處理
    def dealEvent(self, event: pygame.event.Event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(self.boxBody.collidepoint(event.pos)):  
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


def fight():
    # 判定角色遇到敵人時
    global now_num,now
    for key in character_dict:
        if character_dict[key]["int_num"] == now_num:
           break
    # 在不同兵種遇到不同敵人時，HP減的程度（待做：把數額改為減去的圖標百分比（前面設置這個百分比為100，然後固定減，if判定檢測到減到0了就pop這個角色））
    print(key)
    if enemy_list[0] == "enemy_1":
        if now == "XUANer":
            character_dict[key]["HP_percentage"] -= 80
        elif now == "dover":
            character_dict[key]["HP_percentage"] -= 20
    elif enemy_list[0] == "enemy_2":
        if now == "XUANer":
            character_dict[key]["HP_percentage"] -= 20
        elif now == "dover":
            character_dict[key]["HP_percentage"] -= 80
    if character_dict[key]["HP_percentage"] <= 0:
        del character_dict[key]
        now_num += 1
        if character_dict == {}:
            fail_ending()
            
        else:
            next_key = next(iter(character_dict.keys()))
        if next_key.startswith("A"):
            screen.blit(dover,(350,490))
            now = "dover"
        if next_key.startswith("B"):
            screen.blit(XUANer,(350,490))
            now = "XUANer"
        # debug用，看看是否改變了
        pygame.display.flip()
        
    enemy_x_position.pop(0)
    enemy_list.pop(0)
    enemy_sample_list.pop(0)

def watching_mode():
    # 需改 更有創意的方式
    global frequency,main_page_exists,all_sprites,num_list,choosing,choosing_start
    # text = f_small.render(str(enemy_list),True,(0,0,255))
    text = f.render(str(enemy_list),True,(0,100,255))
    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 2))
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

def fail_ending():
    print("fail")  
    sys.exit()
def win_ending():
    import main    
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
money = 300
# 儲存7個enemy分別是enemy1還是enemy2的順序
enemy_list = []
# 儲存各個enemy的實例（裡面有各個enemy的屬性如x坐標）
enemy_sample_list = []
# 因為event.key裡面的pygame.K_1到K5分別對應這5個數字，所以需要對應角色序號和當用戶點擊1-5時所得到的event.key來知道對應點擊的是什麼角色
pykey = {
    1:49,
    2:50,
    3:51,
    4:52,
    5:53,
}
frequency = 0
choosing_start = False
enemy_x_position = []
# 記錄7個enemy的x坐標（平均分佈在地圖七個位置）
for i in range(1,7+1):
    enemy_x_position.append((map_width//7)*i)
# 隨機一個enemy_list
for random_enemy_frequency in range(7):
    x = random.randint(1,2)
    if x == 1:
        enemy_list.append("enemy_1")
    else:
        enemy_list.append("enemy_2")

Watching_chance = 1
last_num = 0
last_y_index = 0

while True: 
    frequency += 1
    clock.tick(60)
    current_y_position = 30
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if choosing == True:
            # 把選擇界面的各個圖像都blit/draw上去
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
        
        if event.type == pygame.KEYDOWN:
            # 進入選兵頁面
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
            # 要確認main_page不存在（未進入主程序）才進行以下操作（因為以下操作是進行選兵操作的）
            if event.key == pygame.K_s:
                # 重新加載選兵界面
                choosing_mode_entering()

            elif event.key == pygame.K_f:
                # 進入遊戲時的初始化（角色，角色HP等等）
                    text = f.render("Text",True,(255,0,0),(0,0,0))
                    total_cost = num_list[0]*80 + num_list[1]*100
                    if total_cost <=300:
                        money -= total_cost
                        for i in range(num_list[0]):
                            # 設置各個角色的屬性進入character_dict
                            dover_list.append(auto_dover_list[i])
                            character_dict[auto_dover_list[i]] = {}
                            # 嵌套字典裝該角色的屬性
                            character_dict[auto_dover_list[i]]["HP"] = HP
                            character_dict[auto_dover_list[i]]["num"] = f.render(str(i+1),True,(255,0,0),(0,0,0))
                            character_dict[auto_dover_list[i]]["int_num"] = i+1
                            character_dict[auto_dover_list[i]]["y_index"] = (i+1)*50
                            character_dict[auto_dover_list[i]]["HP_percentage"] = 100
                            last_y_index = (i+1)*50
                            last_num = i+1
                        for i in range(num_list[1]):
                            XUANer_list.append(auto_XUANer_list[i])
                            HP = pygame.image.load("icons/HP.png")
                            HP = pygame.transform.scale(HP,(100,30))
                            character_dict[auto_XUANer_list[i]] = {}
                            character_dict[auto_XUANer_list[i]]["HP"] = HP
                            character_dict[auto_XUANer_list[i]]["num"] = f.render(str(i+last_num+1),True,(255,0,0))
                            character_dict[auto_XUANer_list[i]]["int_num"] = i+last_num+1
                            character_dict[auto_XUANer_list[i]]["y_index"] = i*50+last_y_index+50
                            character_dict[auto_XUANer_list[i]]["HP_percentage"] = 100
                        setting_finish = True
                        main_page_exists = True
                        choosing = False
                        screen.blit(main_page,(0,0))
                        screen.blit(money_pic,(0,0))
                        if dover_list == []:
                            screen.blit(XUANer,(350,490))
                        else:
                            screen.blit(dover,(350,490))
                        x = 0
                        print(enemy_list)
                        for enemy_name in enemy_list:
                            # 設置各個enemy為一個object並增加對應的屬性如x坐標，將其添加到enemy_sample_list中
                            x_position = enemy_x_position[x]
                            x += 1
                            if enemy_name == "enemy_1":
                                enemy_sample = enemy(enemy_1)
                            else:
                                enemy_sample = enemy(enemy_2)
                            enemy_sample.rect.x = x_position
                            enemy_sample.name = enemy_name
                            enemy_sample_list.append(enemy_sample)

                                                 
                                
                    else:
                        # 輸入的數值不符合條件，如兵種所需的金錢大於300
                        event.key = pygame.K_s
                        text = f.render("請輸入所需不超過300金幣的兵種構成，火鴿子:$80,玄者:$100（規則在ui菜單中）",True,(0,0,50))
                        text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                        screen.blit(text,(0,height-60))
                # except:
                #     print(Exception)
        # 通過點擊圖標進入【待完成】
        # if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos) and choosing == False and main_page_exists == False:
        #     choosing_mode_entering()
            

        # 進入主程序
        if event.type == pygame.KEYDOWN and main_page_exists == True:
            if First_run == False:
                all_sprites = pygame.sprite.Group()
                now_num = 1
                if dover_list == []:
                    player = Player(XUANer)
                    all_sprites.add(player)
                    now = "XUANer"
                    # 此處需要Blit一個sprite
                else:
                    player = Player(dover)
                    all_sprites.add(player)
                    now = "dover"
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
                        now_num = pykey[character_dict[key]["int_num"]]
                        if key.startswith("A"):
                            player = Player(dover)
                            all_sprites.add(player)
                            all_sprites.update('r')
                            all_sprites.update('l')
                            now = "dover"
                            

                            break
                        elif key.startswith("B"):
                            player = Player(XUANer)
                            all_sprites.add(player)
                            all_sprites.update('r')
                            all_sprites.update('l')
                            now = "XUANer"
                            break
                
            # 向右走
            if event.key == pygame.K_d:
                move_status = True
                right_move_status = True
                left_move_status = False
                all_sprites.update('r')
            # 向左走
            if event.key == pygame.K_a:
                move_status = True
                left_move_status = True
                right_move_status = False
                all_sprites.update('l')

        # 按住走路不放的奔跑功能實現
        if right_move_status == True and move_status == True:
            # update這個function是讓地圖的index改變，從而實現角色移動
            all_sprites.update('r')
        if left_move_status == True and move_status == True:
            all_sprites.update('l')    
        if event.type ==  pygame.KEYUP:
            move_status = False
        # 每走一次，都會使得畫面刷新，因此所有的圖像需要根據他們的數值重新blit一次
        for key,value in character_dict.items():
            screen.blit(money_pic,(0,0))
            screen.blit(f.render(str(money),True,(255,0,0)),(50,0))
            y_index = int(character_dict[key]["y_index"])
            text = character_dict[key]["num"]
            HP = character_dict[key]["HP"]
            HP_percentage = character_dict[key]["HP_percentage"]
            HP = pygame.transform.scale(HP, (HP_percentage, HP.get_height()))
            if key.startswith("A"):
                screen.blit(text,(0,y_index))
                screen.blit(mini_dover,(50,y_index))
                screen.blit(HP,(100,y_index,character_dict[key]["HP_percentage"],50))
                # 顯示HP percentage數值
                # HP_percentage_icon = f.render(str(HP_percentage),True,(0,100,255))
                # screen.blit(HP_percentage_icon,(100+50,y_index,character_dict[key]["HP_percentage"],50))
            else:
                screen.blit(text,(0,y_index))
                screen.blit(mini_XUANer,(50,y_index))
                screen.blit(HP,(100,y_index,character_dict[key]["HP_percentage"],100))
                # screen.blit(HP_percentage,(100+50,y_index,character_dict[key]["HP_percentage"],50))
            for enemy_object in enemy_sample_list:
                if enemy_object.name == "enemy_1":
                    screen.blit(enemy_1,(enemy_object.rect.x,enemy_object.rect.y))
                if enemy_object.name == "enemy_2":
                    screen.blit(enemy_2,(enemy_object.rect.x,enemy_object.rect.y))
        for enemy_position in enemy_x_position:
            # 如果角色走過了enemy_position的位置，就觸發攻擊function，通過main_page的x坐標來判定（因為角色移動就是main_page的x坐標移動）
            if abs(main_page_rect.x-400) >= enemy_position:
                fight()
                break
    pygame.display.flip() 



