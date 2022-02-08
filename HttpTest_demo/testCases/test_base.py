# 通用测试用例的封装
from HttpTest_demo.api import get_access_token


class TestBase:
    def setup(self):
        self.gct = get_access_token.GetAccessToken()
