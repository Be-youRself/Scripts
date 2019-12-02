# Coding: utf8
# 获得 1~4 位单词列表文件

def save_file(b,count):
    wordList_file = open("word_list"+str(count)+".txt", "w", encoding="utf8")
    wordList_file.write(str(b))
    wordList_file.close()


# 形成单词列表
alpha_list = []
for i in range(26):
    alpha_list.append(chr(i + 97))
# 确定组成位数
num = 19  # 即(num + 1)位
temp_list1 = []
temp_list2 = []
# 进行赋值
for i in alpha_list:
    temp_list1.append(i)
# 开始遍历
count = 1

for i in range(num):
    save_file(temp_list1, count)
    count+=1
    for j in alpha_list:
        for k in temp_list1:
            temp_list2.append(j + k)
    temp_list1 = []
    for j in temp_list2:
        temp_list1.append(j)
    temp_list2 = []

'''
word_num = 0
for i in range(num + 1):
    word_num += 26 ** i
print(len(result_list) == word_num)
'''
