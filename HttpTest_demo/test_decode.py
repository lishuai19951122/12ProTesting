# 1.调用python自带的base64， 直接对返回的响应做解密，即口得到解密后的响应。
import requests
import json
import base64


def test_decode():
    url = 'http://127.0.0.1:9999/demo1.txt'
    res = requests.get(url=url)
    # json.loads可以识别出字符串中的json格式:去掉引号,并变成通用的json
    print(json.loads(base64.b64decode(res.text)))
