import pytest
import src.data as data
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='function')
def driver():
    browser_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser_driver.maximize_window()
    browser_driver.get(data.main_page_url)
    yield browser_driver
    browser_driver.quit()