from pickle import GLOBAL
from re import A
import time
import sys
import random
from typing import final
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

def display_guard():
    if len(guard_dict) == 0:
            print("士兵已耗尽，游戏失败！")
            time.sleep(3)
            sys.exit()
    for GN,Guard in guard_dict.items():
        if Guard.fighting_ability == 0:
            guard_type = "弓箭手"
        else:
            guard_type = "斧头兵"
        print(f"你拥有的士兵有:{GN}({guard_type}) 血量尚存: {Guard.HP};")
        
# 初始金额1000
cost = 800
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


你拥有 800 灵石，你可以根据自己记忆的 妖怪种类和数量，选择 雇佣 多少个 弓箭兵 和 斧头兵。

每次通过森林后，玩家可以选择是否用灵石给 战士补养；

如果选择补养，消耗1个灵石可以为生命值加1，但是不可能超过最大生命值


这个游戏最后，一定要通过7座森林，才算通关，并且系统显示玩家剩余灵石。

最后 剩余灵石 越多越好，越有机会当选国王。


若是所有己方士兵和所有敌人同时死亡，判定己方失败


【挑战模式】仅有2.5秒缓冲时间给予玩家观看对战面板
【挑战模式】超过25秒自动判定失败
【挑战模式】通关评级分为【极其完美】 / 【完美】 /【优秀】/ 【不错】/ 【一般】，评级受时间和金钱耗费影响

""")
import time 
try:
    input("\n\n\n阅读完成后请输入任意字符：")
except:
    pass
# 随机选择1-7关的敌人是什么类型的
round_count = 10
for random_enemy_frequency in range(round_count):
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
for enemy in enemy_list:
    frequency +=1
    print(f'第{frequency}关敌人：{enemy}')
print("请注意...对战列表将在2.5秒后消失")
time.sleep(2.5)
for i in range(40):
    print("\n")
i = 0
guard_bow = 0
guard_ax = 0
guard_list =[]
guard_dict = {}
auto_bow_name_list = ['a1','a2','a3','a4','a5','a6','a7','a8','a9']
auto_ax_name_list = ['1','2','3','4','5','6','7','8',"9"]

# 自动起名模式
choose_name_model = "1"

timeStart = time.time()
if choose_name_model =="1":
    while True:
        try:
            bow_num = int(input("请输入弓箭手数目："))
            ax_num = int(input("请输入斧头人数目："))
            if bow_num*100 + ax_num*120 >cost:
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
if not choose_name_model =="1":
    cho_guard_count = int(input("请选择要雇佣士兵的数量（包括弓箭手和斧头兵）："))

while guard_bow+guard_ax < cho_guard_count:
    if choose_name_model =="1":
        break
    print(f'你尚有${cost}')
    if cost<100:
        break
    guard_choose = input("请选择你想征用的士兵( 弓箭兵(1) | 斧头兵(2) )：")
    if guard_choose == '1' :
        guard_name = input("请输入弓箭手名字:")
# 如果名字已经在列表中出现
        if guard_name+'(斧头兵)' in guard_list or guard_name+'(弓箭手)' in guard_list:
            print("不能重复起名")
            continue
        guard_list.append(f'{guard_name}(弓箭手)')
        guard_dict[guard_name]  =  guard(guard_name,100,0)
        cost -=100
        guard_bow += 1
        continue
            
    elif guard_choose == '2' :  
        if cost <120:
            continue
        guard_name = input("请输入斧头兵名字:")
        if guard_name+'(斧头兵)' in guard_list or guard_name+'(弓箭手)' in guard_list:
            print("不能重复起名")
            continue
        guard_list.append(f'{guard_name}(斧头兵)')
        guard_dict[guard_name]  =  guard(guard_name,120,1)
        guard_name = guard(guard_name,120,1)
        cost -=120
        guard_ax += 1
        continue
    else:
        print("请输入士兵的序号以选择士兵")
        continue
round = 0
for round_enemy in enemy_list:
    print(f'\n你目前拥有${cost}')
    round +=1
    Cho_guard = None
    # 改成while true不是不可以,总不会真有人这么闲吧
    while x<50:
        try:
            if time.time()-timeStart<25:
                pass
            else:
                print("已到时限,自动判负")
                time.sleep(5)
                sys.exit()
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
                print(f"你目前拥有${cost}")
                continue
            print("士兵并不存在/已死亡(cure用法如：cure10)")
            display_guard()
            x = x+1
            continue
    fighting_army.showdetails()
    print(Cho_guard ,"vs",round_enemy)
    # FA为0，代表self是弓箭手
    round_fight(fighting_army.fighting_ability,round_enemy)
print("\n恭喜通关！")
print(f"你尚存的金币：${cost}")
x=0

# 1斧头兵打7狼，打死5狼时需要+21滴血。1000-（120+21）=859
# 1弓箭手打7鹰，打死4鹰时需要+41滴血，1000-（100+41）=859
# 欧皇评价前置条件是需要一定的运气，匹配到余钱上限高的敌军组合
import math
time_spend = ""
module_end = 0
overall_time = str(time.time()-timeStart)
for i in overall_time:
    if i==".":
        module_end = 1
    time_spend = time_spend+ i
    if module_end==2:
        break
    if module_end==1:
        module_end+=1
print(f"用时为{time_spend}秒")
time_spend = float(time_spend)
if time_spend <6.5:
    time_score = 4
elif time_spend <10:
    time_score = 3
elif time_spend <15:
    time_score = 2
elif time_spend <20:
    time_score = 1

# 1 26.8
# 2 17.99
# 3 10


# if cost >=859:
#     print("你的评级为极其完美!")
#     x='完美'
#     print("额外评价：欧皇在世！")
# # 再其次为7鹰1狼，2弓箭手交替使用,最后余钱800,
# elif cost >=800:
#     print("你的评级为极其完美!")
#     x='完美'
#     print("额外评价：二等欧皇！")
# # 再其次为7狼1鹰，1个斧头兵倒数第二轮cure81,最后余钱799 
# elif cost >=799:
#     print("你的评级为极其完美!")
#     x='完美'
#     print("额外评价：三等欧皇！")

# 除去欧皇情况，其他所有情况的完美上限都只能是779-780
if cost>=799:
    # 10狼/10鹰
    spending_score=8
    print("额外评价：欧皇在世！")
if cost>=700:
    spending_score=6
# 貌似上限是698，需多经测试（购买3个同类兵，轮换着用，前期到了血量斩杀线就加到81，到了后期介于溢出机制可以随便送）
elif cost>=679:
    spending_score=3

# 一个兵一直cure到斩杀线以上（要先看狼多还是鹰多，选克的多的兵种）
elif cost >=619:
    spending_score=2
else:
    spending_score=1
# if enemy_list == ["狼妖","狼妖","狼妖","狼妖","狼妖","狼妖","狼妖"] or enemy_list == ["鹰妖","鹰妖","鹰妖","鹰妖","鹰妖","鹰妖","鹰妖"]:
#     if spending_score=='一般':
#         print("额外评价：给你机会你不中用啊")
        
        # time.sleep(3)
        # sys.exit()
final_score = (spending_score+time_score)//2
if spending_score == 8:
    print("额外评价：欧皇在世！")
if final_score>3:
    print("你的评级为【完美】")
elif final_score>2:
    print("你的评级为【优秀】")
elif final_score>1:
    print("你的评级为【不错】")
else:
    print("你的评级为【一般】")

time.sleep(100)

# V2更新日志：
# 修改了cure可以输入负数而加钱的bug
# cure之后会打印一个cost

# 挑战版更新：
# 可以设为十个对手


# 待优化：
# 出一个新兵种/新对手
