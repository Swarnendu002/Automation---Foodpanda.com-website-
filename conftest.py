import pytest
from selenium import webdriver

@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome("C:/Drivers/chromedriver_win32 (1)/chromedriver.exe")
    request.cls.driver.get("https://www.foodpanda.com/")
    yield
    request.cls.driver.quit()


