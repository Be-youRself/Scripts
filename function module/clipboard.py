# Coding: utf8

import win32clipboard
import win32con

# 获取剪切板内容
def gettext():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text

# 写入内容到剪切板
def settext(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

settext("123")
print(gettext())


'''
也可以使用 pyperclip 库

import pyperclip

pyperclip.copy("想输入到剪切板的内容")  # 输入
pyperclip.paste() # 粘贴
'''