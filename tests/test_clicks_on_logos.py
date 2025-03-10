
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from links import *


class TestClicksOnLogos(MainPage):

    @allure.title("Нажатие на логотип сайта")
    @allure.description("Проверка перехода на основную страницу при клике на логотип сайта")
    @allure.link(ORDER_URL, name='https://qa-scooter.praktikum-services.ru/order')
    def test_click_scooter_logo(self, driver_start):
        self.verify_logo_click(BasePageLocators.scooter_logo, BASE_URL, driver_start)

    @allure.title("Нажатие на логотип яндекса")
    @allure.description("Проверка перехода на yandex dzen при клике на логотип yandex")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_click_yandex_logo(self, driver_start):
        self.click_to_element(BasePageLocators.yandex_logo, driver_start)
        driver_start.switch_to.window(driver_start.window_handles[1])
        self.verify_url_contains("dzen.ru/", driver_start)

    def verify_logo_click(self, logo_locator, expected_url, driver):
        """Общая функция для проверки кликов на лого."""
        self.click_to_element(logo_locator, driver)
        assert expected_url == driver.current_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"

    def verify_url_contains(self, expected_partial_url, driver):
        """Функция для ожидания и проверки части URL."""
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(BasePageLocators.yandex_dzen_find_button)
        )
        assert expected_partial_url in driver.current_url, f"Expected URL to contain: {expected_partial_url}, but got: {driver.current_url}"