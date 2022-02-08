# 封装对于不同算法的处理方法-测试用例
from HttpTest_demo import decode_common


class TestDecodeCommon:
    req_data = {
        'method': 'get',
        'url': 'http://127.0.0.1:9999/demo1.txt',
        'headers': None,
        'encoding': 'base64'
    }

    def test_send(self):
        dc = decode_common.DecodeCommon()
        print(dc.send(self.req_data))
