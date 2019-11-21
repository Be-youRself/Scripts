# Coding: utf8

import tkinter as tk
from tkinter import filedialog

# 打开选择对话框
root = tk.Tk()
root.withdraw()

# 获得选择好的文件夹
folderpath = filedialog.askdirectory()
# 获得选择好的文件
filepath = filedialog.askopenfilename()

print("Folderpath: ", folderpath)
print("Filepath: ", filepath)
