# 样例
import allure
import pytest


@allure.feature("登录模块")
class TestLogin():
    @allure.story('登录成功')
    def test_login_success(self):
        with allure.step('输入账号'):
            print('输入账号')

        with allure.step('输入密码'):
            print('输入密码')

        with allure.step('账号密码正确，登录成功'):
            assert 1 == 1
            print('账号密码正确，登录成功')

    @allure.story('登录失败')
    def test_login_failure(self):
        pass

    # 代码
    @allure.link('http://www.baidu.com', name='链接')
    def test_allure_link(self):
        pass

    Test_Case_Link = 'http://icafe.linkdoc.com/index.php?m=bug&f=browse&productid=54&branch=0&browseType=openedbyme&param=0'

    @allure.testcase(Test_Case_Link, '登录用例')
    def test_allure_testcase(self):
        pass

    # --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
    @allure.issue('140', '这是一个issue')
    def test_allure_issue(self):
        pass


if __name__ == '__main__':
    pytest.main()
