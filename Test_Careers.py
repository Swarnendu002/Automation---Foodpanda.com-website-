import pytest


@pytest.mark.usefixtures("setup")
class TestCareers:
    def test_02(self):
        self.driver.find_element_by_xpath("//a[@href='http://careers.foodpanda.com/']").click()
        if 'Teams' in self.driver.find_element_by_xpath("//a[@href='https://careers.foodpanda.com/teams/']").text:
            assert True
        else:
            assert False
