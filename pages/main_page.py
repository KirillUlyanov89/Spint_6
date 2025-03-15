import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем экземпляр driver

    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator):
        """Находим элемент с ожиданием видимости."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator):
        """Клик по элементу."""
        self.find_element_with_wait(locator).click()

    @allure.step('Скролим до элемента {locator}')
    def scroll_to_element(self, locator):
        """Скролим до элемента."""
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст элемента {locator}')
    def get_text_from_element(self, locator):
        """Получаем текст элемента."""
        return self.find_element_with_wait(locator).text

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Смотрим ответ на вопрос "Что такое цена?"')
    def check_price_answer(self):
        """Смотрим ответ на вопрос "Что такое цена?"."""
        self.scroll_to_element(MainPageLocators.what_is_the_price)
        self.click_to_element(MainPageLocators.what_is_the_price)
        return self.get_text_from_element(MainPageLocators.what_is_the_price_answer)

