# Coding: utf8
# Dealing with the json str from api

import Yd_Translation
import json
import re
import os

repository_file_name = "word_repository.txt"

def preprocess(text):
    text = text.replace("\t","") # 处理制表符
    text = text.replace("\n","") # 处理句末回车
    text = text.strip() # eliminate space in the beginning and end
    text = text.lower()
    return (text)

def en2chs(text):
    text = preprocess(text)
    # dealing with dcit and convert list to str to print
    # judge word or sentence
    ## word
    if text.find(" ") == -1:
        if not re.search(r"\b[a-zA-Z]+\b", text):
            return("Input is illegal!")
        else:
            if not os.path.exists(repository_file_name): # 不存在单词仓库文件就新建文件，并跳过访问仓库阶段
                repository_file = open(repository_file_name, "w", encoding="utf-8")
                repository_file.write("{}")
                repository_file.close()
            else:
                repository_file = open(repository_file_name, "r", encoding="utf-8")
                word_dict = repository_file.read()
                repository_file.close()
                try:
                    word_dict = eval(word_dict)
                    if text in word_dict:
                        return word_dict[text]
                except Exception:
                    print("文件存储受损，读取文件出错！")
            try:
                result_json = Yd_Translation.en2chs(text)
                result_dict = json.loads(result_json)
                word_list = result_dict["basic"]["explains"]
                word_expl = ";".join(word_list)
                postprocess(text, word_expl)
                print(1)
                return (word_expl)
            except Exception:
                return("Can't find the explanation of this word!")
    ## sentence
    else:
        if text == "":
            return("Input is illegal!") # actually it is not needed
        else:
            result_json = Yd_Translation.en2chs(text)
            result_dict = json.loads(result_json)
            sen_list = result_dict["translation"]
            sen_tran = "。".join(sen_list)
            return (sen_tran)

def postprocess(text, explanation):
    # 存储搜索过的单词
    repository_file = open(repository_file_name, "r", encoding="utf-8")
    word_dict = repository_file.read()
    repository_file.close()
    try:
        word_dict = eval(word_dict)
        word_dict[text] = explanation
        word_dict = str(word_dict)
    except Exception:
        print("文件存储受损，写入文件出错！")
    repository_file = open(repository_file_name, "w", encoding="utf-8")
    repository_file.write(word_dict)
    repository_file.close()    


if __name__ == "__main__":
    text = input("Input the word or sentence that you want to translate: ")
    print(en2chs(text))




