# Coding: utf8
# 翻译模块，可以通过有道网页进行查词、翻译等

import requests
import re



def preprocess(text):
    text = text.replace("\t", "")  # 消除制表符
    text = text.replace("\n", "")  # 消除回车符
    text = text.strip()  # 消除首尾空格
    return text


def en2chs(text):
    text = preprocess(text)  # 预处理
    # 判断单词还是句子
    trans_text = text.replace("-", "")  # 处理破折号用于判断
    if re.search(r"^[A-Za-z]+$", trans_text):  # 不能用 isalpha() 判断，因为中文也返回 True
        # 单词
        trans_result = en2chs_repository(text)
        if trans_result != "":
            return trans_result
        else:
            return en2chs_Yd_word(text)
    else:
        # 句子
        return en2chs_Yd_sentence(text)


def en2chs_Yd_word(text):
    # 通过爬取分析有道网页查询单词释义
    trans_result = ""
    trans_url = "http://www.youdao.com/w/" + text  # 将空格全部替换，方便网页搜索
    try:
        trans_page = requests.get(trans_url)  # 这里爬取时可能出现连接失败的异常
    except Exception as e:
        return "无法连接网络！"
    trans_source = str(trans_page.content, encoding="utf-8")
    trans_flag0 = '<div class="trans-container">'  # 定位释义区间
    if trans_source.find(trans_flag0) != -1:
        # 常用词
        # 普通释义
        trans_source = trans_source[trans_source.find(trans_flag0):]
        trans_flag1 = '<ul>'
        trans_flag2 = '</ul>'
        trans_source = trans_source[trans_source.find(trans_flag1): trans_source.find(trans_flag2)]
        trans_flag3 = '<li>'
        trans_flag4 = '</li>'
        trans_num = len(trans_source.split(trans_flag3)) - 1  # 获取词义数量
        trans_list = []
        for i in range(trans_num):
            trans_source = trans_source[trans_source.find(trans_flag3):]
            trans_list.append(trans_source[len(trans_flag3): trans_source.find(trans_flag4)].strip())
            trans_source = trans_source[trans_source.find(trans_flag4):]
            trans_result = "|".join(trans_list)
    else:
        # 特殊词
        trans_flag0 = '<ul id="tPETrans-all-trans" class="all-trans">'
        if trans_source.find(trans_flag0) != -1:
            # 专业释义
            trans_flag1 = '<span class="title">'
            trans_flag2 = '</span>'
            trans_num = len(trans_source.split(trans_flag1)) - 1  # 获取词义数量
            trans_list = []
            for i in range(trans_num):
                trans_source = trans_source[trans_source.find(trans_flag1):]
                trans_list.append(trans_source[len(trans_flag1): trans_source.find(trans_flag2)].strip())
                trans_source = trans_source[trans_source.find(trans_flag2):]
            trans_result = "|".join(trans_list)
        else:
            # 网络释义
            trans_flag2 = '<a href="#" title="详细释义" rel="#rw1" class="sp do-detail">&nbsp;</a>'
            trans_flag3 = '<span>'
            trans_flag4 = '</span>'
            trans_num = len(trans_source.split(trans_flag2)) - 1  # 获取词义数量
            trans_list = []
            for i in range(trans_num):
                trans_source = trans_source[trans_source.find(trans_flag2):]
                trans_list.append(trans_source[trans_source.find(trans_flag3) + len(trans_flag3): trans_source.find(
                    trans_flag4)].strip())
                trans_source = trans_source[trans_source.find(trans_flag4):]
            trans_result = "|".join(trans_list)
    if trans_result == "":
        return "未查询到该词义！"
    else:
        return trans_result


def en2chs_Yd_sentence(text):
    # 通过爬取分析有道网页翻译句子
    trans_url = "http://www.youdao.com/w/" + text.replace(" ", "%20")  # 将空格全部替换，方便网页搜索
    try:
        trans_page = requests.get(trans_url)  # 这里爬取时可能出现连接失败的异常
    except Exception as e:
        return "无法连接网络！"
    trans_source = str(trans_page.content, encoding="utf-8")
    # 夹杂了中文单词翻译，需要判断
    trans_flag0 = '<div class="trans-container">'  # 定位释义区间
    if trans_source.find(trans_flag0) == -1:
        return "无法翻译该内容！"
    else:
        trans_source = trans_source[trans_source.find(trans_flag0):]
        trans_flag3 = '<p class="wordGroup">'
        if trans_source.find(trans_flag3) == -1:
            # 句子翻译(英译汉、汉译英)
            trans_flag1 = "<p>"
            trans_source = trans_source[trans_source.find(trans_flag1) + 1:]  # 定位到输入，加1防止不变化
            trans_source = trans_source[trans_source.find(trans_flag1):]  # 定位到结果
            trans_flag2 = '</p>'
            trans_result = trans_source[len(trans_flag1):trans_source.find(trans_flag2)].strip()  # 结果
        else:
            # 汉译英词语翻译
            trans_source = trans_source[trans_source.find(trans_flag3):]
            trans_flag4 = "</a>"
            trans_source = trans_source[:trans_source.find(trans_flag4)]
            trans_flag5 = '">'
            trans_result = trans_source[trans_source.rfind(trans_flag5) + len(trans_flag5):].strip()
    if trans_result == "":
        return "无法翻译该内容！"
    else:
        return trans_result


def en2chs_repository(text):
    # 通过访问本地仓库来查询单词释义
    return ""


if __name__ == "__main__":
    while True:
        print(en2chs(input()))
