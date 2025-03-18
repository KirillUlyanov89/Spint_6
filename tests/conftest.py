import pytest
from selenium import webdriver
from links import *

@pytest.fixture(scope="function")
def driver_start():
    driver = webdriver.Firefox()
    driver.maximize_window()  # Устанавливаем максимальное разрешение окна
    driver.get(BASE_URL)
    yield driver
    driver.quit()

    # ПОСМОТРИТЕ ВИДЕО РАБОТЫ КОДА https://drive.google.com/file/d/1lmrM793x4B73Nygb18GYq5QZZ5IjA24E/view?usp=sharing