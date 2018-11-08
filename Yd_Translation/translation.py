# Filename: translation.py
# Coding: utf8
# Dealing with the json str from api

import Yd_Translation
import json
import re

def preprocess(text):
    text = text.strip() # eliminate space in the beginning and end
    return (text)

def en2chs(text):
    text = preprocess(text)
    # dealing with dcit and convert list to str to print
    # judge word or sentence
    # word
    if text.find(" ") == -1:
        if not re.search(r"\b[a-zA-Z]+\b", text):
            return("Input is illegal!")
        else:
            try:
                result_json = Yd_Translation.en2chs(text)
                result_dict = json.loads(result_json)
                word_list = result_dict["basic"]["explains"]
                word_expl = ";".join(word_list)
                return (word_expl)
            except Exception:
                return("Can't find the explaination of this word!")
    # sentence
    else:
        if text == "":
            return("Input is illegal!") # actually it is not needed
        else:
            result_json = Yd_Translation.en2chs(text)
            result_dict = json.loads(result_json)
            sen_list = result_dict["translation"]
            sen_tran = "。".join(sen_list)
            return (sen_tran)


if __name__ == "__main__":
    text = input("Input the word or sentence that you want to translate: ")
    print(en2chs(text))


