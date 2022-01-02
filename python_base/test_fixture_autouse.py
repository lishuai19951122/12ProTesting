import pytest


@pytest.fixture(autouse='True')
def open():
    print('打开浏览器')


def test_search1():
    print('执行test_search1')


def test_search2():
    print('执行test_search2')


def test_search3():
    print('执行test_search3')


if __name__ == '__main__':
    pytest.main()
