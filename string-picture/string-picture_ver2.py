# Filename: string-picture.py
# getpixel((x,y)) 黑白图返回灰度值int
# getpixel((x,y)) 彩图返回元祖

from PIL import Image
import os

# 设定好的用于替换的字符集
ASCII_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. ")

def simple_pixel_to_char(grey):
    length = len(ASCII_char)
    # 区间
    unit = 257.0 / length
    index = int(grey / unit)
    # int 转字符
    return ASCII_char[length - index - 1]

def color_pixel_to_char(r, g, b, alpha = 256): # alpha 表示透明度
    # 透明
    if alpha == 0:
        return " "
    length = len(ASCII_char)
    # 灰度值 白 255 黑 0
    grey = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
    # 区间
    unit = 257.0 / length
    index = int(grey / unit)
    # int 转字符
    return ASCII_char[index]

def draw_picture(picture_path):
    img = Image.open(picture_path)
    # 将图片缩放成固定大小
    img = img.resize((76, 38), Image.NEAREST)
    text = ""
    for i in range(38):
        for j in range(76):
            if isinstance(img.getpixel((j, i)), tuple):
                text = text + color_pixel_to_char(*img.getpixel((j, i))) # * 将元祖打散成位置参数
            else:
                text = text + simple_pixel_to_char(img.getpixel((j, i)))
        text = text + "\n"

    file = open("string-picture.txt", "w", encoding = "utf-8")
    file.write(text)
    file.close()
    os.system("string-picture.txt")

picture = input("请输入想要转化的图片路径：")
draw_picture(picture)
    






