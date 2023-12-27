# 唔規範嘅地方：小部分用駝峰式，部分變量不符合命名法，branch名字應該改為master，部分地方可以函數化
# 應將func和初始值變量放到獨立的文件裡,init.py + func_lib.py + class.py等等
# func需要的變量在func文件夾，在debug的時候也方便了解變量是幹什麼的
# 未利用到sprite的碰撞等函數，在x y坐標都可以移動的遊戲裡這種算法不利

# 可增加處/改善處（Lord_Game V2時改善）
# 角色圖片/背景的優化
# 【待完成】 / # 需改
# 結算界面增加【所用時間】，本地自動儲存該時間，在主頁新增一個歷史記錄按鈕
# 觀察後，輸入框的內容保留(txt = self.text已完成，剩下調用watching_mode後self.txt = previous_txt)
# 每局隨機金錢（200-500）+敵人數目+友軍購買所需金錢
# 靜音按鈕（任何時候都有，在右上角）+提交兵種數目按鈕 + 重置輸入按鈕（重置按鈕可以在文本框旁邊/和提交按鈕放在一起，表示重置輸入）
# 重置時改為不是重置界面，而是重置指定的輸入，
# 可以從左到右執行框的輸入（其實不難，因為已經劃分inputbox1和2）
# 選兵界面input時就進行檢查，而不是在按f時檢查
# 避免任何情況的time.sleep()，（以免無法退出遊戲）而是無限進行pygame的循環，直到x秒 
# 試試文本輸入框避免try,except，而是用isdigit()
# 設置快捷方式只設置一次，而不是每次打開程序都設置（ipc）
# 第一個框輸入-100不顯示問題（和輸入a等無效字符的解決方法一樣）
# 如果watching_chance == 1 自動在左下角顯示"輸入W進入觀察模式"
# 因為enemy長度過長而導致"剩餘時間"字樣無法顯示的問題
# 減少默認速度，點擊兩下D開啟疾跑
# 在點擊f但沒有進入畫面的情況下，enter完兩個框的內容可以直接進入
# BUG(284行的檢測輸入是if(event.type == pygame.KEYDOWN)可能是問題，經測試，第一次輸入時有時候能通過這個if但是通過不了(event.key == pygame.K_RETURN)，有時候甚至通過不了前面的if):用中文輸入法剛進入選兵界面時點擊框輸入數字，不能成功輸入，輸入一次/對其他地方空enter一次後輸入才有效(按m等操作不會使其有效化)
# 解決方法1：以其他庫的函數來偵測K_RETURN，並且event.type == pygame.KEYDOWN改為pressing == True, 或是pynput.keyboard中研究怎麼偵測到RETURN的值 2.RETURN判定改為try
# 點擊其他按鍵的情況下，切換到輸入框輸入shift會輸入剛才的那些字符（設定一個對shift等操作的判定: content = ""）
# 輸入0應該是被允許的
# 向左移動時有對應的移動圖片，疾跑有對應的移動圖片
# 上載一些遊戲截圖到github，以及取得最高評分時最後衝刺的影片
# 上載至一些遊戲網站/遊戲平台如steam，以能在不同環境等情況展示遊戲？

# 把func和初始值變量放到獨立的文件裡,init.py + func_lib.py + class.py等等
# func需要的變量在func文件夾，在debug的時候也方便了解變量是幹什麼的

# 次要
# 改為合適的音樂,通關和失敗也有對應不同的音樂
# menu增加更多東西，創意化+美觀化
# 增加不同的模式
# 背景設定重新寫，但可以說借鑒曾經寫的小說，文學化：生靈塗炭..
# watching_mode可以創意化
# 觀察mode倒計時


import sys
import pygame
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import time
import random
from threading import Thread
from pynput.keyboard import KeyCode,Listener

# 初始化各個值以及加載圖片
pygame.init()
width = 800
height = 600
map_width = 3200
map_height = 600
screen = pygame.display.set_mode((width,height),flags=0)
surface = screen
icon = pygame.image.load("icons/seleixi.png").convert() # 唔convert都得，convert後理論畫質更好
start_menu = pygame.image.load("icons/start_menu.png").convert()
pygame.display.set_icon(icon)
pygame.display.set_caption('靈道源尊')
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
Killer = pygame.image.load("icons/Killer.png")
Killer = pygame.transform.scale(Killer,(80,70))
enemy_1 = pygame.image.load("icons/enemy_1.png")
enemy_1 = pygame.transform.scale(enemy_1,(100,100))
enemy_2 = pygame.image.load("icons/enemy_2.png")
enemy_2 = pygame.transform.scale(enemy_2,(50,50))
# 用作上方的圖標顯示
mini_Killer = pygame.transform.scale(Killer,(50,50))
mini_dover = pygame.transform.scale(dover,(50,50))
main_page_rect = main_page.get_rect()
HP = pygame.image.load("icons/HP.png")
HP = pygame.transform.scale(HP,(100,30))
num_list = []
txt = ''
# 自動分配character_dict（友軍的實例list）中object的名字（key）用
auto_dover_list = ['A0','A1','A2','A3','A4']
auto_Killer_list = ['B0','B1','B2','B3',]
character_dict = {}
dover_list = []
Killer_list = []
right_move_status = False
left_move_status = False
fullScreen = False
start_button = (pygame.Rect(280, 270, 234, 60))
entering_button = (pygame.Rect(105,500,600 , 60))
setting_finish = False
pressing = False
choosing = False
First_run = False
money = 300
game_end = False
win = False
game_over_page = pygame.image.load("icons/game_over.png")
winning_page = pygame.image.load("icons/winning_page.png")
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

watching_chance = 1
last_num = 0
last_y_index = 0
now = ""

# 加載音樂（最後一句是設置持續播放音樂時會觸發的函數）
pygame.mixer.init()
pygame.mixer.music.load("music/background_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT)


keyboard_input = ""
pressing_content = ""
# pressing = False
def on_press(key):
    global keyboard_input,pressing,pressing_content
    
    if not pygame.mouse.get_focused():
        return 
    if isinstance(key, KeyCode):
        pressing_content = key.char
        if key.char == 'w':
            keyboard_input = pygame.K_w
        elif key.char == 's':
            keyboard_input = pygame.K_s
        elif key.char == 'a':
            keyboard_input = pygame.K_a
        elif key.char == 'd':
            keyboard_input = pygame.K_d
        elif key.char == 'm':
            keyboard_input = pygame.K_m
        elif key.char == 'f':
            keyboard_input = pygame.K_f
        pressing = True
listener = Listener(on_press=on_press)
listener.start()


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

    
    def update(self,direction):
        # 根據移動的方向（通過鍵盤輸入a/d檢測）來移動地區的x坐標，從而實現移動
        global move_status
        if direction == 'r':
            # 向右走的話，main_page的x坐標是一直在減少的（因為初始值為0,0）-3200是到達城堡的邊界
            if not main_page_rect.x<-3200:
                # 如果沒有到達邊界，就一直讓主頁的x坐標減少，讓角色看起來在"移動"
                for i in range(20):
                    main_page_rect.x -= 1
                    screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                    # screen.blit(money_pic,(0,0))
                    # screen.blit(f.render(str(money),True,(255,0,0)),(50,0))
                    # all_sprites.draw(screen)  # Bug解決：這句導致角色死亡後仍然在刷新精靈（還有176行那句（下一個elif語句，向左走的情況））
                    for enemy_sample in enemy_sample_list:
                        enemy_sample.rect.x -= 1

                    main_page_bliting()
                    pygame.display.flip()
                
            else:
                # 到達城堡後觸發成功function
                win_ending()

        elif direction == "l":
            if not main_page_rect.x>150:
                # 邊界是第一顆數，x坐標是150
                for i in range(20):
                    main_page_rect.x += 1
                    screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                    # all_sprites.draw(screen) # Bug解決：這句導致角色死亡後仍然在刷新精靈
                    for enemy_sample in enemy_sample_list:
                        enemy_sample.rect.x += 1
                    main_page_bliting()
                    pygame.display.flip()
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

num_amount_legal = True
text_content = ""
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
    
    
    def dealEvent(self, event: pygame.event.Event):
        # 當點擊框的時候進行的處理
        global selection,text

        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(self.boxBody.collidepoint(event.pos)):  
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if(
                self.active) else self.color_inactive
        if(event.type == pygame.KEYDOWN):  # 鍵盤輸入響應
            if(self.active):
                global num_amount_legal,text_content
                if self.finish == False:
                    if(event.key == pygame.K_RETURN):
                        global num_list,txt,input_type_legal
                        try:
                            if int(self.text)>=0:
                                num_list.append(int(self.text))
                                txt = int(self.text)
                                self.finish = True
                                num_amount_legal = True
                                input_type_legal = True
                            else:
                                self.text = ""
                                text = f.render("請輸入合理範圍的數值",True,(0,100,255))
                                text_content = "請輸入合理範圍的數值"
                                screen.blit(text,(160,384))
                                num_amount_legal = False
                        except:
                            self.text = ""
                            text = f.render("請輸入正常數字",True,(0,100,255))
                            num_amount_legal = False
                            screen.blit(text,(160,384))
                            text_content = "請輸入正常數字"
                        # if 
                        
                        # self.text=''
                    elif(event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]
                    else:
                        # self.text += 用戶輸入的內容
                        # self.tesxt += event.unicode
                        self.text += pressing_content
        

    def draw(self, screen: pygame.surface.Surface):
        # 文本輸入框的blit()函數
        txtSurface = self.font.render(
            self.text, True, self.color)  # 文字轉換為圖片
        width = max(200, txtSurface.get_width()+10)  # 當文字過長時，延長文本框
        self.boxBody.w = width
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))
        pygame.draw.rect(screen, self.color, self.boxBody, 2)

def main_page_bliting():
    screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
    for key,value in character_dict.items():
        
    # 所有object都blit一次
        
        if now == "dover":
            screen.blit(dover,(350,490))   
        elif now == "Killer":
            screen.blit(Killer,(350,490))
        screen.blit(money_pic,(0,0))
        screen.blit(f.render(str(money),True,(255,0,0)),(50,0))
        y_index = int(character_dict[key]["y_index"])
        text = character_dict[key]["num"]
        HP = character_dict[key]["HP"]
        HP_percentage = character_dict[key]["HP_percentage"]
        
        HP = pygame.transform.scale(HP, (HP_percentage, HP.get_height()))
        if key.startswith("A"):
            # 前面幾行已經設置了變量
            screen.blit(text,(0,y_index))
            screen.blit(mini_dover,(50,y_index))
            screen.blit(HP,(100,y_index))
            # 顯示HP percentage數值
            # HP_percentage_icon = f.render(str(HP_percentage),True,(0,100,255))
            # screen.blit(HP_percentage_icon,(100+50,y_index,character_dict[key]["HP_percentage"],50))
        else:
            # Killer的處理
            screen.blit(text,(0,y_index))
            screen.blit(mini_Killer,(50,y_index))
            screen.blit(HP,(100,y_index))
            # screen.blit(HP_percentage,(100+50,y_index,character_dict[key]["HP_percentage"],50))
        for enemy_object in enemy_sample_list:
            # 所有enemy都blit一次
            if enemy_object.name == "enemy_1":
                screen.blit(enemy_1,(enemy_object.rect.x,enemy_object.rect.y))
            if enemy_object.name == "enemy_2":
                screen.blit(enemy_2,(enemy_object.rect.x,enemy_object.rect.y))
    pygame.display.flip()
def fight():
    # 判定角色遇到敵人時
    global now_num,now
    for key in character_dict:
        if character_dict[key]["int_num"] == now_num:
           break
    # 在不同兵種遇到不同敵人時，HP減的程度（待做：把數額改為減去的圖標百分比（前面設置這個百分比為100，然後固定減，if判定檢測到減到0了就pop這個角色））
    if enemy_list[0] == "enemy_1":
        if now == "Killer":
            character_dict[key]["HP_percentage"] -= 80
        elif now == "dover":
            character_dict[key]["HP_percentage"] -= 20
    elif enemy_list[0] == "enemy_2":
        if now == "Killer":
            character_dict[key]["HP_percentage"] -= 20
        elif now == "dover":
            character_dict[key]["HP_percentage"] -= 80
    if character_dict[key]["HP_percentage"] <= 0:
        del character_dict[key]
        now_num += 1
        for key in character_dict:
            if key.startswith("A"):
                now = "dover"
            elif key.startswith("B"):
                now = "Killer"
        # all_sprites.remove(player)
        # all_sprites.update("l")
        # all_sprites.draw(screen)
        pygame.display.flip()
        # player.remove()
        # player.update("r")

        # Test
        # all_sprites = pygame.sprite.Group()
        # # if dover_list == []:
        # player = Player(Killer)
        # now = "Killer"
        # if key.startswith("A"):
        #     player = Player(dover)
        #     now = dover
        #     dover_list.pop(0)
        # else:
        #     player = Player(Killer)
        #     now = Killer
        #     Killer_list.pop(0)
        # all_sprites.add(player)
        # all_sprites.update('r')
        # all_sprites.update('l')
        
        if character_dict == {}:
            fail_ending()
            
        # else:
            # if now == "dover":
            #     screen.blit(dover,(350,490))
            # else:
                # screen.blit(now,(350,490))   
        # print(dover_list)
        
    enemy_x_position.pop(0)
    enemy_list.pop(0)
    enemy_sample_list.pop(0)

def watching_mode():
    # 將enemy_list內容顯示
    global frequency,main_page_exists,all_sprites,num_list,choosing,choosing_start
    text = "敵人順序："
    enemy_frequency = 0
    for enemy in enemy_list:
        enemy_frequency +=1
        if enemy == "enemy_1":
            added_text = f"{enemy_frequency}.妖弭猴 "
        else:
            added_text = f"{enemy_frequency}.紅猩 "
        text += added_text
    enemy_final_list = text
    text = f.render(text+"觀察時間僅有五秒",True,(0,100,255))
    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 2))
    screen.blit(text,(0,height-30))
    if main_page_exists == True:  
        # 在主頁時的顯示    
        pygame.display.flip()
        time.sleep(5)
        # all_sprites.update('r')
        # all_sprites.update('l')
    else:
        # 在選擇界面的顯示
        pygame.display.flip()
        time.sleep(5)
        # text = f.render((enemy_final_list+"所剩時間:5秒"),True,(0,100,255))
        # screen.blit(text,(0,height-30))
        # pygame.display.flip()
        # time.sleep(1)
        # text = f.render((enemy_final_list+"所剩時間:4秒"),True,(0,100,255))
        # screen.blit(text,(0,height-30))
        # pygame.display.flip()
        # time.sleep(1)
        # text = f.render((enemy_final_list+"所剩時間:3秒"),True,(0,100,255))
        # screen.blit(text,(0,height-30))
        # pygame.display.flip()
        # time.sleep(1)
        # text = f.render((enemy_final_list+"所剩時間:2秒"),True,(0,100,255))
        # screen.blit(text,(0,height-30))
        # pygame.display.flip()
        # time.sleep(1)
        # text = f.render((enemy_final_list+"所剩時間:1秒"),True,(0,100,255))
        # screen.blit(text,(0,height-30))
        # time.sleep(1)
        # pygame.display.flip()
        choosing_mode_entering()
        # inputbox = InputBox(pygame.Rect(150, 450, 10, 32)) 
        # inputbox2 = InputBox(pygame.Rect(450, 450, 10, 32)) 
        # inputbox.draw(screen)
        # inputbox2.draw(screen)
        #待添加 #blit：進入遊戲：F(以英文輸入法) (可啟動 / 不可啟動)，火鴿子數目： Killer數目： 

def choosing_mode_entering():
    # 點擊s時會重置頁面的函數，把所有數額重置
    global num_list,choosing,choosing_start,inputbox,inputbox2,first_choosing,selecting_page,num_amount_legal,input_type_legal
    selecting_page = pygame.image.load("icons/selecting_page.png")
    screen.blit(selecting_page,(0,0))
    num_list = []
    inputbox = InputBox(pygame.Rect(150, 450, 10, 32)) 
    inputbox2 = InputBox(pygame.Rect(450, 450, 10, 32)) 
    inputbox.draw(screen)
    inputbox2.draw(screen)
    choosing = True
    choosing_start = True
    text = f.render("輸入兵種數目並輸入enter(注意需要從左到右執行),輸入S重置界面",True,(0,0,50))
    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // (1.5)))
    screen.blit(text,(0,0))
    text = f.render("輸入W進入觀察模式(檢查敵人構成),輸入M關閉音樂",True,(0,0,50))
    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
    screen.blit(text,(0,25))
    first_choosing == False

    #待添加 #blit：進入遊戲：F(以英文輸入法) (可啟動 / 不可啟動)，火鴿子數目： Killer數目：
    num_amount_legal = True
    input_type_legal = True

def fail_ending():
    # 失敗時觸發的function
    global main_page_exists,choosing,game_end,music_muted
    screen.blit(game_over_page,(0,0))
    pygame.display.flip()
    # 避開主程序運行時的條件
    main_page_exists = False
    choosing = False
    game_end = True
    music_muted = True
    pygame.mixer.music.stop()
    

def win_ending():
    # 勝利時觸發的function
    global main_page_exists,choosing,game_end,result,win,music_muted
    main_page_exists = False
    choosing = False
    game_end = True
    screen.blit(winning_page,(0,0))
    used_money = 300-money
    if used_money <= 160:
        result = pygame.image.load("icons/excellent.png")
    elif used_money <= 180:
        result = pygame.image.load("icons/good.png")
    elif used_money <= 200:
        result = pygame.image.load("icons/not_bad.png")
    else:
        result = pygame.image.load("icons/pass.png")
    screen.blit(result,(0,0))
    win = True
    music_muted = True
    pygame.mixer.music.stop()
    pygame.display.flip()

first_choosing = False
music_muted = False
selection = 0
entering = False
input_type_legal = True

while True: 
    frequency += 1
    clock.tick(60)
    current_y_position = 30
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 音樂結束時繼續播放音樂
        elif event.type == pygame.USEREVENT and music_muted == False:
            pygame.mixer.music.play()


        if choosing == True and game_end == False:
            # 把選擇界面的各個圖像都blit/draw上去

            # 嘗試修復BUG：第一次因為未定義inputbox導致deal event無法成立
            # if first_choosing == False:
            # choosing_mode_entering()
            if len(num_list)== 1:
                selecting_page = pygame.image.load("icons/nf_1.png")
                screen.blit(selecting_page,(0,0))
                selection = 3
            if len(num_list)== 2:
                selecting_page = pygame.image.load("icons/f_2.png")
                screen.blit(selecting_page,(0,0))
                selection = 3

            # 嘗試修復BUG2：第一次因為未定義inputbox導致deal event無法成立
            # if inputbox.
            # inputbox = InputBox(pygame.Rect(150, 450, 10, 32)) 
            # inputbox2 = InputBox(pygame.Rect(450, 450, 10, 32)) 


            
            
            # inputbox1_text = txt
            # print(inputbox1_text)
            screen.blit(selecting_page,(0,0)) # 是否導致【請輸入正常數字】出現的關鍵
            # 123
            if num_amount_legal == False:
                text = f.render(text_content,True,(0,100,255))
                screen.blit(text,(160,384))
            if input_type_legal == False:
                text = f.render("請完成所有輸入",True,(255,0,0),(0,0,0))
                screen.blit(text,(510,546))
            inputbox.draw(screen)
            inputbox2.draw(screen) 
            input2 = inputbox2.dealEvent(event)
            input1 = inputbox.dealEvent(event)
            text = f.render("輸入兵種數目並輸入enter(注意需要從左到右執行),輸入S重置界面",True,(255,0,0))
            text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // (1.5)))
            screen.blit(text,(0,0))
            text = f.render("輸入W進入觀察模式(檢查敵人構成),輸入M關閉音樂",True,(0,0,50))
            text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
            screen.blit(text,(0,25))
            if watching_chance == 0:
                text = f.render("觀察機會已耗盡",True,(0,0,50))
                text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                screen.blit(text,(0,height-30))
            # inputbox2_text = txt
            # print(inputbox2_text)
            while first_choosing == False:
                text = f.render("輸入兵種數目並輸入enter(注意需要從左到右執行),輸入S重置界面",True,(255,0,0))
                text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // (1.5)))
                screen.blit(text,(0,0))
                text = f.render("輸入W進入觀察模式(檢查敵人構成),輸入M關閉音樂",True,(0,0,50))
                text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                screen.blit(text,(0,25))
                first_choosing = True
            #待添加 # blit：進入遊戲(以英文輸入法輸入F)： (可啟動 / 不可啟動(請完成輸入))，火鴿子數目： Killer數目：
        if pressing == True and game_end == False:
            # listener = Listener(on_press=on_press)
            # 當遊戲進行時所有可調用的快捷鍵
            # pressing = False
            if keyboard_input == pygame.K_w:
                # 進入觀察模式
                if watching_chance == 1 and choosing_start == True:
                    watching_mode()
                    watching_chance -=1
                    event.key = pygame.K_s
                elif watching_chance == 0 and main_page_exists == False:
                    text = f.render("觀察機會已耗盡",True,(0,0,50))
                    text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                    screen.blit(text,(0,height-30))
            if keyboard_input == pygame.K_m:
                keyboard_input = ""
                if music_muted == False:
                    pygame.mixer.music.stop()
                    music_muted = True
                elif music_muted == True:
                    pygame.mixer.music.play()
                    music_muted = False
        # 通過鼠標進入選兵頁面【test】
        if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos) and choosing == False and main_page_exists == False:
            choosing_mode_entering()
        if event.type == pygame.MOUSEBUTTONDOWN and entering_button.collidepoint(event.pos) and len(num_list)== 2 and main_page_exists == False and game_end == False:
            entering = True
        elif pressing == True and main_page_exists == False and game_end == False:
            # event.type == pygame.KEYDOWN
            # pressing = False
            # 要確認main_page不存在（未進入主程序）才進行以下操作（因為以下操作是進行選兵操作的）
            if keyboard_input == pygame.K_s:
                # 重新加載選兵界面
                keyboard_input = ""
                choosing_mode_entering()
            if (keyboard_input == pygame.K_f) and game_end == False:# or (event.type == pygame.MOUSEBUTTONDOWN and entering_button.collidepoint(event.pos) and len(num_list)== 2 and main_page_exists == False and game_end == False):
                entering = True
                keyboard_input = ""
        if entering == True:
            # 進入遊戲時的初始化（角色，角色HP等等）
            text = f.render("Text",True,(255,0,0),(0,0,0))
            try:
                total_cost = num_list[0]*80 + num_list[1]*100
            except:
                text = f.render("請完成所有輸入",True,(255,0,0),(0,0,0))
                screen.blit(text,(510,546))
                entering = False
                input_type_legal = False
                break
            if total_cost <=300:
                entering = False
                money -= total_cost
                for i in range(num_list[0]):
                    # 設置各個角色的屬性進入character_dict
                    dover_list.append(auto_dover_list[i])
                    character_dict[auto_dover_list[i]] = {}
                    # 嵌套字典裝該角色的屬性
                    character_dict[auto_dover_list[i]]["HP"] = HP
                    character_dict[auto_dover_list[i]]["num"] = f.render(str(i+1),True,(255,0,0))
                    character_dict[auto_dover_list[i]]["int_num"] = i+1
                    character_dict[auto_dover_list[i]]["y_index"] = (i+1)*50
                    character_dict[auto_dover_list[i]]["HP_percentage"] = 100
                    last_y_index = (i+1)*50
                    last_num = i+1
                for i in range(num_list[1]):
                    # Killer的處理（不能函數化，因為差別細節太多，不能以幾個參數完成）
                    Killer_list.append(auto_Killer_list[i])
                    HP = pygame.image.load("icons/HP.png")
                    HP = pygame.transform.scale(HP,(100,30))
                    character_dict[auto_Killer_list[i]] = {}
                    character_dict[auto_Killer_list[i]]["HP"] = HP
                    character_dict[auto_Killer_list[i]]["num"] = f.render(str(i+last_num+1),True,(255,0,0))
                    character_dict[auto_Killer_list[i]]["int_num"] = i+last_num+1
                    character_dict[auto_Killer_list[i]]["y_index"] = i*50+last_y_index+50
                    character_dict[auto_Killer_list[i]]["HP_percentage"] = 100
                setting_finish = True
                main_page_exists = True
                choosing = False
                screen.blit(main_page,(0,0))
                screen.blit(money_pic,(0,0))
                if dover_list == []:
                    screen.blit(Killer,(350,490))
                else:
                    screen.blit(dover,(350,490))
                x = 0
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
                text = f.render("請輸入所需不超過300金幣的兵種構成，火鴿子:$80,Killer:$100（規則在ui菜單中）",True,(0,0,50))
                text = pygame.transform.scale(text, (text.get_width() // 2, text.get_height() // 1.5))
                screen.blit(text,(0,height-60))
                entering = False
                break
                        

        # 進入主程序
        if pressing == True and main_page_exists == True and game_end == False:
            # pressing = False
            # 進入主程序後只會執行一次
            if First_run == False:
                all_sprites = pygame.sprite.Group()
                now_num = 1
                if dover_list == []:
                    player = Player(Killer)
                    all_sprites.add(player)
                    now = "Killer"
                    # 此處需要Blit一個sprite
                else:
                    player = Player(dover)
                    all_sprites.add(player)
                    now = "dover"
                First_run = True
            if pressing == True:
                # 全屏化處理
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    if fullScreen == False:
                        screen = pygame.display.set_mode((width,height),(pygame.FULLSCREEN))
                        fullScreen = True
                        screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                        all_sprites.draw(screen)
                    else:
                        # 解鎖全屏
                        screen = pygame.display.set_mode((width,height),flags=0)
                        screen.blit(main_page,(main_page_rect.x,main_page_rect.y))
                        all_sprites.draw(screen)
                        fullScreen = False
            if pressing_content == "1" or pressing_content == "2" or pressing_content == "3" or pressing_content == "4":
                # 切換兵種
                for key,value in character_dict.items():
                    if pykey[character_dict[key]["int_num"]] == pykey[int(pressing_content)]:
                        all_sprites = pygame.sprite.Group()
                        now_num = character_dict[key]["int_num"]
                        if key.startswith("A"):
                            # 角色是dover時的處理
                            player = Player(dover)
                            all_sprites.add(player)
                            now = "dover"
                            main_page_bliting()
                            
                            
                            break
                        elif key.startswith("B"):
                            player = Player(Killer)
                            all_sprites.add(player)
                            now = "Killer"
                            main_page_bliting()
                            break
                
            # 向右走
            if keyboard_input == pygame.K_d:
                move_status = True
                right_move_status = True
                left_move_status = False
                all_sprites.update('r')
                keyboard_input = ""
            # 向左走
            if keyboard_input == pygame.K_a:
                move_status = True
                left_move_status = True
                right_move_status = False
                all_sprites.update('l')
                keyboard_input = ""

        # 按住走路不放的奔跑功能實現
        if right_move_status == True and move_status == True:
            # update這個function是讓地圖的index改變，從而實現角色移動
            all_sprites.update('r')
            move_status = False
        if left_move_status == True and move_status == True:
            all_sprites.update('l')  
            move_status = False
        if event.type ==  pygame.KEYUP:
            move_status = False
        # 每走一次，都會使得畫面刷新，因此所有的圖像需要根據他們的數值重新blit一次
        if game_end == False and main_page_exists == True:
            # 每個主程序處理都需要帶上game_end == False，以免遊戲結束後主程序干擾結束界面

            main_page_bliting()
            # 結束界面時，不斷循環blit結束畫面
        elif game_end == True:
            if win == True:
                screen.blit(result,(0,0))
            else:
                screen.blit(game_over_page,(0,0))
        for enemy_position in enemy_x_position:
            # 如果角色走過了enemy_position的位置，就觸發攻擊function，通過main_page的x坐標來判定（因為角色移動就是main_page的x坐標移動）
            if abs(main_page_rect.x-400) >= enemy_position:
                fight()
                # try: # 測試是否顯示錯誤（不是，是扣血者錯誤）
                #     print("A0的HP比例為：",character_dict["A0"]["HP_percentage"])
                #     print("B0的HP比例為：",character_dict["B0"]["HP_percentage"])
                # except:
                #     pass
                break
    # 每次循環後更新頁面
    pygame.display.flip() 