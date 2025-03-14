import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import BasePage
from locators.base_page_locators import BasePageLocators
from links import *

class TestClicksOnLogos:

    @allure.title("Нажатие на логотип сайта")
    @allure.description("Проверка перехода на основную страницу при клике на логотип сайта")
    @allure.link(ORDER_URL, name='https://qa-scooter.praktikum-services.ru/order')
    def test_click_scooter_logo(self, driver_start):
        main_page = MainPage(driver_start)
        main_page.click_to_element(BasePageLocators.scooter_logo)
        assert driver_start.current_url == BASE_URL, f"Expected URL: {BASE_URL}, but got: {driver_start.current_url}"

    @allure.title("Нажатие на логотип яндекса")
    @allure.description("Проверка перехода на Yandex Dzen при клике на логотип Yandex")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_click_yandex_logo(self, driver_start):
        main_page = MainPage(driver_start)
        main_page.click_to_element(BasePageLocators.yandex_logo)
        driver_start.switch_to.window(driver_start.window_handles[1])  # Переход на новую вкладку
        main_page.verify_url_contains("dzen.ru/")  # Проверка URL

# В классе MainPage добавляем метод verify_url_contains для проверки URL
class MainPage(BasePage):

    @allure.step('Проверяем, что URL содержит {expected_partial_url}')
    def verify_url_contains(self, expected_partial_url):
        """Функция для ожидания и проверки части URL."""
        # Ожидание, что текущий URL содержит ожидаемую часть
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_partial_url)
        )
        assert expected_partial_url in self.driver.current_url, f"Expected URL to contain: {expected_partial_url}, but got: {self.driver.current_url}"