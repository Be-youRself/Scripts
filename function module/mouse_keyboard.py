# Coding: utf8
# pynput库: https://www.cnblogs.com/botoo/p/8302531.html



# 键盘按键的监听
from pynput import keyboard

'''
def on_press(key):
    try:
        print('alphanumeric key  {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
'''
 
flag = False
def on_press(key):
    global flag
    if str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r":
        flag = True
    if str(key) == "Key.esc":
        pass
    if str(key) == "'c'":
        if flag:
            print("复制")

def on_release(key):
    global flag
    if str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r":
        flag = False

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

