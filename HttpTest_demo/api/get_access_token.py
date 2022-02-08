# 调用baseapi实现获取token接口
import yaml
import pytest
from string import Template
from HttpTest_demo.api.base_api import BaseApi


class GetAccessToken(BaseApi):
    _corpid = 'wwc51a4d24e4d21b53'
    _corpsecret = 'HiS_zwS7MXKTMl-Mc-qTcuCdH3lGtscVNIJWzvvs9rQ'

    def template(self):
        with open('../data/get_token.yaml') as f:
            data = {
                'corpid': self._corpid,
                'corpsecret': self._corpsecret
            }
            rt = Template(f.read()).substitute(data)
            return yaml.safe_load(rt)

    def get_access_token(self):
        return self.requests_http(self.template()).json()
