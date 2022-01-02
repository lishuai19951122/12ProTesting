import pytest


@pytest.mark.search
def test_search_01():
    print('search_01')
    raise NameError


@pytest.mark.search
def test_search_02():
    print('search_02')


@pytest.mark.search
def test_search_03():
    print('search_03')


@pytest.mark.login
def test_login_01():
    print('login_01')


@pytest.mark.login
def test_login_02():
    print('login_02')


if __name__ == '__main__':
    pytest.main()
