from pickle import GLOBAL
import time
import sys
import random
class guard:

    def __init__(self,name,HP,fighting_ability):
        self.name = name
        self.HP = HP
        self.fighting_ability = fighting_ability

    def fight(self):
        if self.fighting_ability == 20:
            self.HP -=20
            print(self.name,"的血量尚存",self.HP)
        else:
            self.HP -=80
            print(self.name,"的血量尚存",self.HP)
    def change_FA(self,fighting_ability):
        self.fighting_ability = fighting_ability

    def cure(self,Cho_guard):
        if Cho_guard[:4] =='cure':
            cure_cost = Cho_guard[4:-1]+Cho_guard[-1]
            if self.fighting_ability ==0:
                if int(cure_cost)<0:
                    print("不可輸入負數")
                elif int(cure_cost) + self.HP <= 100:
                    self.HP += int(cure_cost)
                    return int(cure_cost)
                else:
                    print("血量不可超出100")
            elif self.fighting_ability ==1:
                if int(cure_cost)<0:
                    print("不可輸入負數")
                elif int(cure_cost) + self.HP <= 120:
                    self.HP += int(cure_cost)
                    return int(cure_cost)
                else:
                    print("血量不可超出100")

    def ifdeath(self):
        if self.HP <=0:
            guard_dict.pop(self.name)

    def showdetails(self):
        if self.fighting_ability == 0:
            guard_type = "弓箭手"
        else:
            guard_type = "斧頭兵"
        print(f'''
士兵姓名：{self.name}
士兵生命值：{self.HP}
士兵類型：{guard_type}
''')
    def showname(self):
        return(self.name)

def display_guard():
    if len(guard_dict) == 0:
            print("士兵已耗盡，遊戲失敗！")
            time.sleep(3)
            sys.exit()
    for GN,Guard in guard_dict.items():
        if Guard.fighting_ability == 0:
            guard_type = "弓箭手"
        else:
            guard_type = "斧頭兵"
        print(f"你擁有的士兵有:{GN}({guard_type}) 血量尚存: {Guard.HP};")
        
# 初始金額1000
cost = 1000
enemy_list = []


eagle = 0
wolf = 0
def round_fight(FA,round_enemy): #FA=0 or 1 (弓箭手/斧頭兵)
    if FA == 0:
        eagle = 20
        wolf = 80
    elif FA ==1:
        eagle =80
        wolf=20
    if round_enemy == "鷹妖":
            fighting_army.change_FA(eagle)
            print(f"{fighting_army.showname()}打贏了戰鬥！")
            fighting_army.fight()
            fighting_army.ifdeath()
            fighting_army.change_FA(FA)
            display_guard()

        # 弓箭手遇到鷹妖-80血
    elif round_enemy == "狼妖":
        fighting_army.change_FA(wolf)
        print(f"{fighting_army.showname()}打贏了戰鬥！")
        fighting_army.fight()
        fighting_army.ifdeath()
        fighting_army.change_FA(FA)
        display_guard()
AN = 0
army_cost = 0
# 自動列表名，士兵種類（0 or 1）,士兵數目
def auto_name(auto_name_list,guard_type,army_num):
    global cost,guard_bow,guard_ax,guard_name,guard_list,guard_dict
    if guard_type == 0:
        army_cost = 100
        army_name = "弓箭手"
        guard_bow += army_num
    elif guard_type ==1:
        army_cost =120
        army_name = "斧頭人"
        guard_ax += army_num
    for armys_name in auto_name_list[:army_num]:
        guard_list.append(f'{armys_name}({army_name})')
        guard_dict[armys_name]  =  guard(armys_name,army_cost,int(guard_type))
        cost -=army_cost
        
# rules
print("""

""")
try:
    input("\n\n\n準備完畢後請輸入任意字符：")
except:
    pass
# 隨機選擇1-7關的敵人是什麽類型的
for random_enemy_frequency in range(7):
    x = random.randint(1,2)
    if x == 1:
        enemy_list.append("鷹妖")
    else:
        enemy_list.append("狼妖")
frequency = 0


# 測試用！！！
# enemy_list = ["狼妖","狼妖","狼妖","狼妖","狼妖","狼妖","鷹妖"]
# enemy_list = ["鷹妖","鷹妖","鷹妖","鷹妖","鷹妖","鷹妖","狼妖"]
# 3w 1b 2w 1b
# 打印1-7關的敵人
for enemy in enemy_list:
    frequency +=1
    print(f'第{frequency}關敵人：{enemy}')
print("請注意...敵人列表將在5秒後消失")
time.sleep(5)
for i in range(40):
    print("\n")
i = 0
guard_bow = 0
guard_ax = 0
guard_list =[]
guard_dict = {}
auto_bow_name_list = ['A0','A1','A2','A3','A4','A5','A6','A7','A8','A9']
auto_ax_name_list = ['B0','B1','B2','B3','B4','B5','B6','B7',]

# 自動起名模式
choose_name_model = input("請選擇是否進入自動起名模式(輸入1選擇進入起名模式,手動模式輸入任何字符)：")
if choose_name_model =="1":
    while True:
        try:
            bow_num = int(input("請輸入弓箭手數目："))
            ax_num = int(input("請輸入斧頭人數目："))
            if bow_num*100 + ax_num*120 >1000:
                print("弓箭手*100+斧頭人*120不可大於金額1000","\n","請重新輸入：")
                continue
            if bow_num<0 or ax_num<0:
                print("不可輸入負數") # 跳轉
                continue
            break
        except:     
            print("輸入的並非數字，請重新再試")
            continue
    # 自動列表名，士兵種類（0 or 1）,士兵數目
    auto_name(auto_bow_name_list,0,bow_num)
    auto_name(auto_ax_name_list,1,ax_num)
    display_guard()
cho_guard_count = 0
if not choose_name_model =="1":
    cho_guard_count = int(input("請選擇要雇傭士兵的數量（包括弓箭手和斧頭兵）："))

while guard_bow+guard_ax < cho_guard_count:
    if choose_name_model =="1":
        break
    print(f'你尚有${cost}')
    if cost<100:
        break
    guard_choose = input("請選擇你想征用的士兵( 弓箭兵(1) | 斧頭兵(2) )：")
    if guard_choose == '1' :
        guard_name = input("請輸入弓箭手名字:")
# 如果名字已經在列表中出現
        if guard_name+'(斧頭兵)' in guard_list or guard_name+'(弓箭手)' in guard_list:
            print("不能重覆起名")
            continue
        guard_list.append(f'{guard_name}(弓箭手)')
        guard_dict[guard_name]  =  guard(guard_name,100,0)
        cost -=100
        guard_bow += 1
        continue
            
    elif guard_choose == '2' :  
        if cost <120:
            continue
        guard_name = input("請輸入斧頭兵名字:")
        if guard_name+'(斧頭兵)' in guard_list or guard_name+'(弓箭手)' in guard_list:
            print("不能重覆起名")
            continue
        guard_list.append(f'{guard_name}(斧頭兵)')
        guard_dict[guard_name]  =  guard(guard_name,120,1)
        guard_name = guard(guard_name,120,1)
        cost -=120
        guard_ax += 1
        continue
    else:
        print("請輸入士兵的序號以選擇士兵")
        continue
round = 0
for round_enemy in enemy_list:
    print(f'\n你目前擁有${cost}')
    round +=1
    Cho_guard = None
    # 改成while true不是不可以,總不會真有人這麽閒吧
    while x<50:
        try:
            Cho_guard = input(f"\n請選擇第{round}輪出戰士兵 / 是否治愈士兵(輸入cure以及對應的治療值)：")
            if Cho_guard[:4] == 'cure':
                Cho_guard_name = input("請輸入要治愈的士兵:")
                # cost減去return回來的cure花費，而cure函數在計算花費時已經將受傷士兵治愈
                cost -= guard_dict[Cho_guard_name].cure(Cho_guard)
            fighting_army =  guard_dict[Cho_guard]
            break
        except :
            if Cho_guard[:4] == 'cure':
                display_guard()
                print(f"你目前擁有${cost}")
                continue
            print("士兵並不存在/已死亡(cure用法如：cure10)")
            display_guard()
            x = x+1
            continue
    fighting_army.showdetails()
    print(Cho_guard ,"vs",round_enemy)
    # FA為0，代表self是弓箭手
    round_fight(fighting_army.fighting_ability,round_enemy)
print("恭喜通關！")
print(f"你尚存的金幣：${cost}")
x=0

# 1斧頭兵打7狼，打死5狼時需要+21滴血。1000-（120+21）=859
# 1弓箭手打7鷹，打死4鷹時需要+41滴血，1000-（100+41）=859
# 歐皇評價前置條件是需要一定的運氣，匹配到余錢上限高的敵軍組合
if cost >=859:
    print("你的評級為極其完美!")
    x='完美'
    print("額外評價：歐皇在世！")
# 再其次為7鷹1狼，2弓箭手交替使用,最後余錢800,
elif cost >=800:
    print("你的評級為極其完美!")
    x='完美'
    print("額外評價：二等歐皇！")
# 再其次為7狼1鷹，1個斧頭兵倒數第二輪cure81,最後余錢799 
elif cost >=799:
    print("你的評級為極其完美!")
    x='完美'
    print("額外評價：三等歐皇！")

# 除去歐皇情況，其他所有情況的完美上限都只能是779-780
elif cost>=779:
    x='完美'
    print("你的評級為完美!")

# 貌似上限是698，需多經測試（購買3個同類兵，輪換著用，前期到了血量斬殺線就加到81，到了後期介於溢出機制可以隨便送）
elif cost>=679:
    x='優秀'
    print("你的評級為優秀")

# 一個兵一直cure到斬殺線以上（要先看狼多還是鷹多，選克的多的兵種）
elif cost >=619:
    x='不錯'
    print("你的評級為不錯")
else:
    x='一般'
    print("你的評級為一般")
if enemy_list == ["狼妖","狼妖","狼妖","狼妖","狼妖","狼妖","狼妖"] or enemy_list == ["鷹妖","鷹妖","鷹妖","鷹妖","鷹妖","鷹妖","鷹妖"]:
    if x=='一般':
        print("額外評價：給你機會你不中用啊")
        
        time.sleep(3)
        sys.exit()

time.sleep(3)

# V2更新日志：
# 修改了cure可以輸入負數而加錢的bug
# cure之後會打印一個cost

# 優化：guard_list是沒必要的
# 想一個不用每個兵都輸入名字的辦法
