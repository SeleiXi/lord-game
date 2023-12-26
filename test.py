
import pygame
from pynput.keyboard import KeyCode,Listener
 
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出游戏
            global running
            global listener
            running = False
            listener.stop()
            return
 
# 创建 pygame 窗口和游戏循环
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Example")
 
# 定义一个处理键盘输入的回调函数
def on_press(key):
    # 鼠标不在窗口时不处理
    print(KeyCode)
    if not pygame.mouse.get_focused():
        return 
    if isinstance(key, KeyCode):
        print(key.char)
        if key.char == 'w':
            # 向上移动
            print("向上移动")
        elif key.char == 's':
            # 向下移动
            print("向下移动")
        elif key.char == 'a':
            # 向左移动
            print("向左移动")
        elif key.char == 'd':
            # 向右移动
            print("向右移动")
# 监听键盘输入事件
listener = Listener(on_press=on_press)
listener.start()
# 游戏主循环
running = True
while running:
    handle_events()
    pygame.display.update()
 
# 退出游戏
pygame.quit()