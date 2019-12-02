# Coding: utf8
# 有道服务模块，从配置文件中获取账号密码

import http.client  # python 2 ----- httplib
from hashlib import md5
import urllib.request  # python 2 ----- urllib
import random


def en2chs(text, appKey, secretKey):
    '''
    English to Chinese
    :param text: text that you want to translate.
    :return: a json str includes translating informations
    '''
    httpClient = None
    myurl = '/api'
    q = text
    fromLang = 'EN'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)

    sign = appKey + q + str(salt) + secretKey
    m1 = md5()
    m1.update(sign.encode("utf8"))  # python 3 ----- update() needs to set encoding = ""
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.request.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()

        return (response.read())
    except Exception as e:
        return (e)
    finally:
        if httpClient:
            httpClient.close()
