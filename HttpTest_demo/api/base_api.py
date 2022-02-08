# 封装basiapi
import requests


class BaseApi:

    def requests_http(self, req):
        return requests.request(**req)
