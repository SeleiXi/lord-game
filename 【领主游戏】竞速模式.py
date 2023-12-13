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
                    print("不可输入负数")
                elif int(cure_cost) + self.HP <= 100:
                    self.HP += int(cure_cost)
                    return int(cure_cost)
                else:
                    print("血量不可超出100")
            elif self.fighting_ability ==1:
                if int(cure_cost)<0:
                    print("不可输入负数")
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
            guard_type = "斧头兵"
        print(f'''
士兵姓名：{self.name}
士兵生命值：{self.HP}
士兵类型：{guard_type}
''')
    def showname(self):
        return(self.name)
import math
def display_guard():
    if len(guard_dict) == 0:
            print("士兵已耗尽，游戏失败！")
            print(f"你完成的轮数为:{round}")
            print(f"你的耗时为{math.ceil(time.time()-Start_time)}")
            time.sleep(3)
            sys.exit()
    for GN,Guard in guard_dict.items():
        if Guard.fighting_ability == 0:
            guard_type = "弓箭手"
        else:
            guard_type = "斧头兵"
        print(f"你拥有的士兵有:{GN}({guard_type}) 血量尚存: {Guard.HP};")
        
# 初始金额1000
cost = 100000
enemy_list = []


eagle = 0
wolf = 0
def round_fight(FA,round_enemy): #FA=0 or 1 (弓箭手/斧头兵)
    if FA == 0:
        eagle = 20
        wolf = 80
    elif FA ==1:
        eagle =80
        wolf=20
    if round_enemy == "鹰妖":
            fighting_army.change_FA(eagle)
            print(f"{fighting_army.showname()}打赢了战斗！")
            fighting_army.fight()
            fighting_army.ifdeath()
            fighting_army.change_FA(FA)
            display_guard()

        # 弓箭手遇到鹰妖-80血
    elif round_enemy == "狼妖":
        fighting_army.change_FA(wolf)
        print(f"{fighting_army.showname()}打赢了战斗！")
        fighting_army.fight()
        fighting_army.ifdeath()
        fighting_army.change_FA(FA)
        display_guard()
AN = 0
army_cost = 0
# 自动列表名，士兵种类（0 or 1）,士兵数目
def auto_name(auto_name_list,guard_type,army_num):
    global cost,guard_bow,guard_ax,guard_name,guard_list,guard_dict
    if guard_type == 0:
        army_cost = 100
        army_name = "弓箭手"
        guard_bow += army_num
    elif guard_type ==1:
        army_cost =120
        army_name = "斧头人"
        guard_ax += army_num
    for armys_name in auto_name_list[:army_num]:
        guard_list.append(f'{armys_name}({army_name})')
        guard_dict[armys_name]  =  guard(armys_name,army_cost,int(guard_type))
        cost -=army_cost
from threading import Thread
def round_time_calculate(now_round):
    round_start = time.time()
    for i in range(5):
        time.sleep(1)
        if not now_round == round:
            break
    if time.time() - round_start > 5:
        print(f"\n你完成的轮数为：{round}")
        time.sleep(20)

# rules
print("""
欢迎来到领主游戏！
你将会前往都城参选国王。但是路途上有7座森林，每座森林里面可能会碰到一个妖怪： 鹰妖 和 狼妖。
所以你需要雇佣战士对付它们，可以雇佣 弓箭兵 或者 斧头兵
弓箭兵、 斧头兵、 狼妖、鹰妖 具有如下特征

弓箭兵：

    雇佣价： 100 灵石
    最大生命值： 100
    杀伤力 
        杀死鹰妖  ： 损耗生命值 20
        杀死狼妖  :  损耗生命值 80
斧头兵：

    雇佣价： 120 灵石
    最大生命值： 120
    杀伤力 
        杀死鹰妖  ： 损耗生命值 80
        杀死狼妖  :  损耗生命值 20


你拥有 1000 灵石，你可以根据自己记忆的 妖怪种类和数量，选择 雇佣 多少个 弓箭兵 和 斧头兵。

每次通过森林后，玩家可以选择是否用灵石给 战士补养；

如果选择补养，消耗1个灵石可以为生命值加1，但是不可能超过最大生命值


这个游戏最后，一定要通过7座森林，才算通关，并且系统显示玩家剩余灵石。

最后 剩余灵石 越多越好，越有机会当选国王。


若是所有己方士兵和所有敌人同时死亡，判定己方失败

通关评级分为【极其完美】 / 【完美】 / 【优秀】 / 【不错】 / 【一般】

无限模式：你将只能选择一个兵来作战，每轮作战只有5秒时间进行。成绩将由在60秒内通过多少关为准则进行评分。
""")
try:
    input("\n\n\n阅读完成后请输入任意字符：")
except:
    pass
# 随机选择1-7关的敌人是什么类型的
for random_enemy_frequency in range(1000):
    x = random.randint(1,2)
    if x == 1:
        enemy_list.append("鹰妖")
    else:
        enemy_list.append("狼妖")
frequency = 0


# 测试用！！！
# enemy_list = ["狼妖","狼妖","狼妖","狼妖","狼妖","狼妖","鹰妖"]
# enemy_list = ["鹰妖","鹰妖","鹰妖","鹰妖","鹰妖","鹰妖","狼妖"]
# 3w 1b 2w 1b
# 打印1-7关的敌人
for i in range(40):
    print("\n")
i = 0
guard_bow = 0
guard_ax = 0
guard_list =[]
guard_dict = {}
auto_bow_name_list = ['A0','A1','A2','A3','A4','A5','A6','A7','A8','A9']
auto_ax_name_list = ['B0','B1','B2','B3','B4','B5','B6','B7',]

# 自动起名模式
while True:
    User_ID = input("请输入你的ID，而后输入一个空格输入你选择斧头兵(代号1)/弓箭手(代号2) e.g. SeleiXi 1)：")
    User_Choosing = User_ID.split()
    choose_name_model = 3
    import time
    Start_time = time.time()
    try:
        if choose_name_model == 3:
            guard_name = User_Choosing[0]
            if User_Choosing[1] == "1":
                guard_name = guard(User_Choosing[0],100,1)
                guard_list.append(f'{User_Choosing[0]}(斧头兵)')
                guard_dict[User_Choosing[0]]  =  guard(User_Choosing[0],120,1)
                guard_name = guard(User_Choosing[0],120,1)
                break
            elif User_Choosing[1] == "2":
                guard_list.append(f'{guard_name}(弓箭手)')
                guard_dict[guard_name]  =  guard(guard_name,100,0)
                cost -=100
                guard_bow += 1
                break
            else:
                print("请输入正确的代号")
                continue
    except:
        continue


# 死亡后加一个完成轮数及时间
# 设定60秒后自动结束并统计轮数，设定评分。

if choose_name_model =="1":
    while True:
        try:
            bow_num = int(input("请输入弓箭手数目："))
            ax_num = int(input("请输入斧头人数目："))
            if bow_num*100 + ax_num*120 >1000:
                print("弓箭手*100+斧头人*120不可大于金额1000","\n","请重新输入：")
                continue
            if bow_num<0 or ax_num<0:
                print("不可输入负数")
                continue
            break
        except:
            print("输入的并非数字，请重新再试")
            continue
    # 自动列表名，士兵种类（0 or 1）,士兵数目
    auto_name(auto_bow_name_list,0,bow_num)
    auto_name(auto_ax_name_list,1,ax_num)
    display_guard()
cho_guard_count = 0

# 更改处
# if not choose_name_model =="1":
#     cho_guard_count = int(input("请选择要雇佣士兵的数量（包括弓箭手和斧头兵）："))

# while guard_bow+guard_ax < cho_guard_count:
#     if choose_name_model =="1":
#         break
#     print(f'你尚有${cost}')
#     if cost<100:
#         break
#     guard_choose = input("请选择你想征用的士兵( 弓箭兵(1) | 斧头兵(2) )：")
#     if guard_choose == '1' :
#         guard_name = input("请输入弓箭手名字:")
# # 如果名字已经在列表中出现
#         if guard_name+'(斧头兵)' in guard_list or guard_name+'(弓箭手)' in guard_list:
#             print("不能重复起名")
#             continue
#         guard_list.append(f'{guard_name}(弓箭手)')
#         guard_dict[guard_name]  =  guard(guard_name,100,0)
#         cost -=100
#         guard_bow += 1
#         continue
            
#     elif guard_choose == '2' :  
#         if cost <120:
#             continue
#         guard_name = input("请输入斧头兵名字:")
#         if guard_name+'(斧头兵)' in guard_list or guard_name+'(弓箭手)' in guard_list:
#             print("不能重复起名")
#             continue
#         guard_list.append(f'{guard_name}(斧头兵)')
#         guard_dict[guard_name]  =  guard(guard_name,120,1)
#         guard_name = guard(guard_name,120,1)
#         cost -=120
#         guard_ax += 1
#         continue
#     else:
#         print("请输入士兵的序号以选择士兵")
#         continue
round = 0
for round_enemy in enemy_list:
    round +=1
    Cho_guard = None
    # 改成while true不是不可以,总不会真有人这么闲吧
    while x<50:
        try:
            if time.time() - Start_time >60:
                print(f"你完成的轮数为：{round}")
                # 待完成
                # print(f"你的评分为:{}")
                time.sleep(20)
                sys.exit()
            cal = Thread(target=round_time_calculate,args =(round,))
            cal.start()
            Cho_guard = input(f"\n请选择第{round}轮出战士兵 / 是否治愈士兵(输入cure以及对应的治疗值)：")
            if Cho_guard[:4] == 'cure':
                Cho_guard_name = input("请输入要治愈的士兵:")
                # cost减去return回来的cure花费，而cure函数在计算花费时已经将受伤士兵治愈
                cost -= guard_dict[Cho_guard_name].cure(Cho_guard)
            fighting_army =  guard_dict[Cho_guard]
            break
        except :
            if Cho_guard[:4] == 'cure':
                display_guard()
                continue
            print("士兵并不存在/已死亡(cure用法如：cure10)")
            display_guard()
            x = x+1
            continue
    fighting_army.showdetails()
    print(Cho_guard ,"vs",round_enemy)
    # FA为0，代表self是弓箭手
    round_fight(fighting_army.fighting_ability,round_enemy)
print("恭喜通关！")
print(f"你尚存的金币：${cost}")
x=0

# 1斧头兵打7狼，打死5狼时需要+21滴血。1000-（120+21）=859
# 1弓箭手打7鹰，打死4鹰时需要+41滴血，1000-（100+41）=859
# 欧皇评价前置条件是需要一定的运气，匹配到余钱上限高的敌军组合
if cost >=859:
    print("你的评级为极其完美!")
    x='完美'
    print("额外评价：欧皇在世！")
# 再其次为7鹰1狼，2弓箭手交替使用,最后余钱800,
elif cost >=800:
    print("你的评级为极其完美!")
    x='完美'
    print("额外评价：二等欧皇！")
# 再其次为7狼1鹰，1个斧头兵倒数第二轮cure81,最后余钱799 
elif cost >=799:
    print("你的评级为极其完美!")
    x='完美'
    print("额外评价：三等欧皇！")

# 除去欧皇情况，其他所有情况的完美上限都只能是779-780
elif cost>=779:
    x='完美'
    print("你的评级为完美!")

# 貌似上限是698，需多经测试（购买3个同类兵，轮换着用，前期到了血量斩杀线就加到81，到了后期介于溢出机制可以随便送）
elif cost>=679:
    x='优秀'
    print("你的评级为优秀")

# 一个兵一直cure到斩杀线以上（要先看狼多还是鹰多，选克的多的兵种）
elif cost >=619:
    x='不错'
    print("你的评级为不错")
else:
    x='一般'
    print("你的评级为一般")
if enemy_list == ["狼妖","狼妖","狼妖","狼妖","狼妖","狼妖","狼妖"] or enemy_list == ["鹰妖","鹰妖","鹰妖","鹰妖","鹰妖","鹰妖","鹰妖"]:
    if x=='一般':
        print("额外评价：给你机会你不中用啊")
        
        time.sleep(3)
        sys.exit()

time.sleep(10)

# 死亡后加一个完成轮数及时间
# 设定60秒后自动结束并统计轮数，设定评分。
