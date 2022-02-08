# 多环境替换实现类
import requests
import yaml


class EnvReplace:
    env = yaml.safe_load(open('data/env.yaml'))

    def env_replace(self, data: dict):
        data['url'] = str(data['url']).replace('testing-studio', self.env['testing-studio'][self.env['default']])
        return requests.request(method=data['method'], url=data['url'], headers=data['headers']).json()
