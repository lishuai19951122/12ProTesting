import pytest
import sys
import yaml

from python_base.calc import Calc


def steps():
    with open('dates/steps.yaml') as f:
        return yaml.safe_load(f)


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('data1,data2,expect', yaml.safe_load(open('dates/add.yaml')))
    def test_add(self, data1, data2, expect):
        steps1 = steps()
        for step in steps1:
            if 'add' == step:
                result = self.calc.add(data1, data2)
                print(f'运行add方法的结果{result}')
            elif 'add1' == step:
                result = self.calc.add1(data1, data2)
                print(f'运行add1方法的结果{result}')
            assert result == expect

# 用法1：参数化，前面2个变量，后面是对应的数据
@pytest.mark.parametrize("input,expected", [('1+2', 3), ('2+5', 7), ('3+7', 9)])
def test_eval(input, expected):
    # eval 将字符串str当成有效的表达式来值，并返回相应的结果
    assert eval(input) == expected


# 用法1：参数化，前面2个变量，后面是对应的数据 把数据放到yaml文件中，实现数据和pytest的分离
@pytest.mark.parametrize("input,expected", yaml.safe_load(open('dates/data.yaml')))
def test_eval_01(input, expected):
    # eval 将字符串str当成有效的表达式来值，并返回相应的结果
    assert eval(input) == expected


# 用法2：组合参数
@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.parametrize('b', [3, 4, 5])
def test_foo(a, b):
    print(f'字符串组合a：{a},b:{b}')


test_user_data = ['lili', 'xiaoming']


# 用法3：将方法作为参数传入
@pytest.fixture(scope='module')
def login_user(request):
    # 接收并传入的参数
    user = request.param
    print(f'打开首页准备登录，登录用户：{user}')
    return user


# indirect=True 可以把传过来的参数当成函数来执行
# skip跳过某个方法
@pytest.mark.skip('不执行')
@pytest.mark.skipif(sys.platform == 'darwin', reason='不在macos上执行')
# xfail
@pytest.mark.xfail
@pytest.mark.parametrize('login_user', test_user_data, indirect=True)
def test_login(login_user):
    u = login_user
    print(f'用户为{u}')
    assert u != ''


if __name__ == '__main__':
    pytest.main()
