# fixture的用法
import pytest


def test_01(login):
    print('这是test_01,需要登录')


def test_02():
    print('这是test_02,需要登录')


def test_03(login):
    print('这是test_03,需要登录')


if __name__ == '__main__':
    pytest.main()
