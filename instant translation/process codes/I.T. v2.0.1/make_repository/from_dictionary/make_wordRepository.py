# Coding: utf8
# 根据输入的单词列表来查找各个单词的意思，并形成词库文件

import datetime
import sys
import os

import IT_translationModule


def save_file(word_and_meaning):
    wordRepository_file = open(wordRepository_filename, "r", encoding="utf8")
    repository_dict = eval(wordRepository_file.read())
    wordRepository_file.close()
    wordRepository_file = open(wordRepository_filename, "w", encoding="utf8")
    wordRepository_file.write(str(dict(repository_dict, **word_and_meaning)))
    wordRepository_file.close()

file_num_list = []
file_list = os.listdir()
for i in file_list:
    if i.find("word_list") != -1:
        file_num_list.append(i[len("word_list"):i.find(".")])
for file_num_i in file_num_list:
    # 输入文件
    file_num = file_num_i # file_num = input("文件序号：")
    wordList_filename = "word_list" + file_num +".txt"
    wordRepository_filename = "word_repository" + file_num +".txt"
    # 读取列表
    wordList_file = open(wordList_filename, "r", encoding="utf8")
    word_list = eval(wordList_file.read())
    wordList_file.close()
    # 新建文件
    wordRepository_file = open(wordRepository_filename, "w", encoding="utf8")
    wordRepository_file.write("{}")
    wordRepository_file.close()
    # 输入开始与结束坐标
    start = 0 # start = int(input("开始坐标："))
    end = -1 # end = int(input("结束坐标："))
    # 处理输入
    if end < 0:
        end += len(word_list)
    circul_num = end - start + 1
    # 设置保存频率
    frequency = 10000
    # 开始处理
    # 开始时间
    start_time = datetime.datetime.now()
    # 进度条
    n = circul_num
    sys.stdout.write("  0%|                                                  | {0}/{1}".format(0, n))
    sys.stdout.flush()
    word_and_meaning = {}
    try:
        for i in range(circul_num):
            text = word_list[start + i].lower()
            result = IT_translationModule.en2chs_Yd_word(text)
            if result != "未查询到该词义！":
                word_and_meaning[text] = result
            if i % frequency == 0:
                save_file(word_and_meaning)
                word_and_meaning = {}
            # 刷新进度条
            sys.stdout.write('   \r')
            sys.stdout.flush()
            percent_num = (i + 1) * 100 // n
            if percent_num < 10:
                sys.stdout.write("  ")
            elif percent_num < 100:
                sys.stdout.write(" ")
            else:
                pass
            sys.stdout.write('{0}%|'.format(percent_num))
            for j in range(percent_num // 4):
                sys.stdout.write("█")
            for k in range(25 - percent_num // 4):
                sys.stdout.write("  ")
            sys.stdout.write("| {0}/{1}".format(i + 1, n))
            sys.stdout.flush()
        save_file(word_and_meaning)
        print("任务完成！")
        # os.remove(wordList_filename)
        # print("起始坐标：" + str(start))
        # print("终止坐标：" + str(end))
        # 结束时间
        end_time = datetime.datetime.now()
        # 给出结果
        second = end_time.second - start_time.second
        minute = end_time.minute - start_time.minute
        hour = end_time.hour - start_time.hour
        if second < 0:
            second += 60
            minute -= 1
        if minute < 0:
            minute += 60
            hour -= 1
        if hour < 0:
            hour += 24
        print("用时:{0}时{1}分{2}秒".format(hour, minute, second))
    except Exception as e:
        print(e)
        # print("起始坐标：" + str(start))
        # print("终止坐标：" + str(end))
        # print("保存了 " + str(i//frequency) + " 次！") # 返回保存次数
        # print("每次扫描了 " + str(frequency) + " 个单词！")
        print("当前失败文件索引：" + file_num)