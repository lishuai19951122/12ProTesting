# 封装对于不同算法的处理方法
import requests
import json
import base64


class DecodeCommon:

    def send(self, data: dict):
        res = requests.request(data['method'], data['url'], headers=data['headers'])
        if data['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.text))
        # 把加密过后的响应值发送给第三方服务，让第三方解密后返回解密后信息
        elif ['encoding'] == 'private':
            return requests.post('url', data=res.text)
