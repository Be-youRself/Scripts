# Coding: utf8
# 从下载到的词典中爬取词语列表

import re

dictname = "dict1.txt"
dict_file = open(dictname, "r", encoding="utf8")
word_list = []
while True:
    line = dict_file.readline()
    if len(line) == 0:
        break
    if 'a' <= line[0] <= 'z' or 'A' <= line[0] <= 'Z':
        word = line[:line.find(" ")]
        processed_word = word.replace("-", "")
        if re.search(r"^[A-Za-z]+$", processed_word):
            word_list.append(word)
dict_file.close()
wordRepository_file = open("word_list1.txt", "w", encoding="utf8")
wordRepository_file.write(str(word_list))
wordRepository_file.close()
print(len(word_list))