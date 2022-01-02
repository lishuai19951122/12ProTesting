# 代码
import pytest
import allure


class Test_Allure_Severity():

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_with_trivial_severity(self):
        pass

    @allure.severity(allure.severity_level.MINOR)
    def test_with_minor_severity(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    def test_with_normal_severity(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_with_critical_severity(self):
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    def test_with_blocker_severity(self):
        pass


@allure.severity(allure.severity_level.NORMAL)
class Test_Allure_Severity1():
    def test_add(self):
        pass


if __name__ == '__main__':
    pytest.main()
