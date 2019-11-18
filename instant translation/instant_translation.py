# Coding: utf8

import win32clipboard
import win32con
import translation
import os

repository_file_name = "word_repository.txt"

# 获取剪切板内容
def gettext():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text

def make_newWordBook(address="new word book.txt"):
    if not os.path.exists(repository_file_name): # 不存在则新建
        repository_file = open(repository_file_name, "w", encoding="utf-8")
        repository_file.write("{}")
        repository_file.close()
    else:
        repository_file = open(repository_file_name, "r", encoding="utf8")
        word_dict = repository_file.read()
        repository_file.close()
    newWordBook = ""
    try:
        word_dict = eval(word_dict)
        for i in word_dict:
            newWordBook += i
            for j in range(30 - len(i)):
                newWordBook += " "
            newWordBook += word_dict[i] + "\n"
        newWordBook_file = open(address, "w", encoding="utf8")
        newWordBook_file.write(newWordBook)
        newWordBook_file.close()
    except Exception as e:
        print(e)

make_newWordBook("../test.txt")
# print(translation.en2chs(gettext()))
