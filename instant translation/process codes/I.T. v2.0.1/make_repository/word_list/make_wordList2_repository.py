# Coding: utf8
# 分散运用两个单词列表文件文件去形成第三个文件，同时直接筛序生成词库文件而不是单词列表

import IT_translationModule
import datetime
import sys

def save_file(a, count):
    file = open("word_repository" + out_file_num + str(count) + ".txt", "w", encoding="utf8")
    file.write(str(a))
    file.close()


file_num1 = input("第一个文件序号：")
file_num2 = input("第二个文件序号：")

out_file_num = str(int(file_num1) + int(file_num2))


wordList_file = open("word_list" + file_num1 + ".txt", "r", encoding="utf8")
word_list1 = eval(wordList_file.read())
wordList_file.close()

wordList_file = open("word_list" + file_num2 + ".txt", "r", encoding="utf8")
word_list2 = eval(wordList_file.read())
wordList_file.close()


frequent = 10000
count = 0
# 开始时间
start_time = datetime.datetime.now()
# 进度条
n = len(word_list2) * len(word_list1)
sys.stdout.write("  0%|                                                  | {0}/{1}".format(0, n))
sys.stdout.flush()
word_and_meaning = {}
ii = 0
for i in word_list1:
    for j in word_list2:
        text = (i+j).lower()
        result = IT_translationModule.en2chs_Yd_word(text)
        if result != "未查询到该词义！":
            word_and_meaning[text] = result
            count += 1
        if count % frequent == 0:
            save_file(word_and_meaning, count//frequent)
            word_and_meaning = {}
        # 刷新进度条
        sys.stdout.write('   \r')
        sys.stdout.flush()
        percent_num = (ii + 1) * 100 // n
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
        sys.stdout.write("| {0}/{1}".format(ii + 1, n))
        sys.stdout.flush()
        ii = ii + 1
save_file(word_and_meaning, count//frequent + 1)
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