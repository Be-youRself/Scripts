# Coding: utf8
# 将多个单词列表文件合成一个单词列表文件

import os


file_first_num = input("输入序号：")
file_num_list = []
file_list = os.listdir()
for i in file_list:
    if i.find("word_list" + str(file_first_num)) != -1:
        file_num_list.append(i[len("word_list" + str(file_first_num)):i.find(".")])
result = []
finishedFile_list = []
for file_num_i in file_num_list:
    # 输入文件
    file_num = file_num_i # file_num = input("文件序号：")
    wordList_filename = "word_list" + file_first_num + file_num +".txt"
    # 读取列表
    wordList_file = open(wordList_filename, "r", encoding="utf8")
    word_list = eval(wordList_file.read())
    wordList_file.close()
    result +=  word_list
    finishedFile_list.append(wordList_filename)
# 新建文件
wordRepository_file = open("word_list" + file_first_num +".txt", "w", encoding="utf8")
wordRepository_file.write(str(result))
wordRepository_file.close()
for i in finishedFile_list:
    os.remove(i)