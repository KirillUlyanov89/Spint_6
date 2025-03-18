from selenium.webdriver.common.by import By

class BasePageLocators:
    order_button_header = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    order_button_footer = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')
    scooter_logo = (By.XPATH, './/a[contains(@class, "Header_LogoScooter")]')
    yandex_logo = (By.XPATH, './/a[contains(@class, "Header_LogoYandex")]')
    yandex_dzen_find_button = (By.XPATH, './/button[text()="Найти"]')

# ПОСМОТРИТЕ ВИДЕО РАБОТЫ КОДА https://drive.google.com/file/d/1lmrM793x4B73Nygb18GYq5QZZ5IjA24E/view?usp=sharing