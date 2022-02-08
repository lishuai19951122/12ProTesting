import yaml

env = {
    'default': 'env',
    'testing-studio': {
        'test': '127.0.0.1',
        'dev': '127.0.0.2'
    }
}

req = {
        'method': 'get',
        'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        'params': {
            'corpid': 'wwc51a4d24e4d21b53',
            'corpsecret': 'HiS_zwS7MXKTMl-Mc-qTcuCdH3lGtscVNIJWzvvs9rQ'
        }
    }

def test_yaml():
    with open('data/get_token.yaml', mode='w') as f:
        yaml.safe_dump(data=req, stream=f)

    print(yaml.safe_load(open('data/get_token.yaml')))
