# Filename: Yd_Translation.py
# Coding: utf8
#

import http.client # python 2 对应 httplib
from hashlib import md5
import urllib.request # python 2 对应 urllib
import random


def en2chs(text):
    '''
    :param : text (which need to be translated)
    :return: json string as a result
    '''
    appKey = "应用ID"
    secretKey = "应用密钥"

    httpClient = None
    myurl = '/api'
    q = text
    fromLang = 'EN'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)

    sign = appKey + q + str(salt) + secretKey
    m1 = md5()
    m1.update(sign.encode("utf8")) # python 3 中必须要编码后进行 update
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.request.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()

        #print("type:" + type(response.read()))
        print(response.read())
        #result = str(response.read())
        #print("type(str):" + type(result))
        #print(result)

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":
    en2chs("good")