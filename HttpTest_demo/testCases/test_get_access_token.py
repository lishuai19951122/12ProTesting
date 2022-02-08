# 调用获取token方法，断言测试用例
from HttpTest_demo.testCases.test_base import TestBase


class TestGetAccessToken(TestBase):

    def test_get_access_token(self):
        assert self.gct.get_access_token()['errcode'] == 0
