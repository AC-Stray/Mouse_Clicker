from pymouse import PyMouse
import time
import keyboard
tutorial = """
使用教程：
此程序开始运行后，首先，你可以输入连点间隔。
随后，程序进入连点模式，按住p，程序就会开始连点。
按下Q可以退出连点模式，并重新设置连点间隔。
需要注意的是，实际连点间隔最终取决于系统性能，可能会与设定值有一定差距。
Powered by AbsoCube
"""
print(tutorial)
mouse = PyMouse()


def GetInterval():
    while True:
        inter = input("输入连点间隔：")
        try:
            inter = float(inter)
        except ValueError:
            print("连点间隔需要是浮点数")
        else:
            print("成功设置连点间隔")
            break
    return inter


press = False
interval = GetInterval()
point = time.time()


def key(x):
    global press, interval, point
    p = keyboard.KeyboardEvent('down', 28, 'p')
    q = keyboard.KeyboardEvent('down', 28, 'q')
    if x.event_type == 'down' and x.name == p.name:
        press = True
    elif x.name == p.name:
        press = False
    if x.event_type == 'down' and x.name == q.name:
        interval = GetInterval()
    if press and time.time()-point >= interval:
        mouse.click(mouse.position()[0], mouse.position()[1], 1)
        point = time.time()


keyboard.hook(key)
keyboard.wait()
