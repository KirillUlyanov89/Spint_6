from selenium.webdriver.common.by import By


class BasePageLocators:
    order_button = [By.XPATH, ".//button[contains(@class, 'Button_Button') and text()='Заказать']"]
    second_order_button = [By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']"]
    scooter_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"]
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"]
    yandex_dzen_find_button = [By.XPATH, ".//button[text()='Найти']"]