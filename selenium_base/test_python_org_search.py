from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest


class TestPythonOrgSearch():
    def setup(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        assert ("百度一下", driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    pos = TestPythonOrgSearch()
    pos.test_search_in_python_org()
