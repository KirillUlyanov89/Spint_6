import pytest
from selenium import webdriver
from links import *

@pytest.fixture(scope="module")
def driver_start():
    driver = webdriver.Firefox()
    driver.maximize_window()  # Устанавливаем максимальное разрешение окна
    driver.get(BASE_URL)
    yield driver
    driver.quit()