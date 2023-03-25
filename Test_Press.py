import pytest


@pytest.mark.usefixtures("setup")
class TestPress:
    def test_03(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.foodpanda.com/press/']").click()
        if 'All Countries' in self.driver.find_element_by_xpath("//*[@class='select-box__input-text']").text:
            assert True
        else:
            assert False

