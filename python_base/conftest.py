import pytest


# 作用域：module是在模块之前执行，模块之后执行
@pytest.fixture()
def login():
    print('这是一个登录方法')


# 解决自定义标记是waring问题
def pytest_configure(config):
    mark_list = ['search', 'login']
    for markers in mark_list:

        config.addinivalue_line('markers', markers)
