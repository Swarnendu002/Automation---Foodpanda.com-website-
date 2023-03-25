import pytest


@pytest.mark.usefixtures("setup")
class TestAbout:
    def test_01(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.foodpanda.com/about/']").click()
        if 'Privacy' in self.driver.find_element_by_xpath(" // a[ @ href = '/privacy-policy']").text:
            assert True
        else:
            assert False


