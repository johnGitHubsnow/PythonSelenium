import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(params = ["chrome"], scope='class')
def set_up(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = web_driver
    yield

    web_driver.quit()