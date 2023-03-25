import pytest


@pytest.mark.usefixtures("setup")
class TestNew:
    def test_04(self):
        self.driver.find_element_by_xpath("//a[@href='http://careers.foodpanda.com/']").click()
        self.driver.find_element_by_xpath("//a[@href='https://careers.foodpanda.com/teams/']").click()
        if 'Browse Jobs' in self.driver.find_element_by_xpath("//a[@href='https://careers.foodpanda.com/jobs/?country"
                                                              "=0&department=commercial']").text:
            assert True
        else:
            assert False
