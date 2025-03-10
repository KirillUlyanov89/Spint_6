import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage:

    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator, driver):
        element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return element

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator, driver):
        self.find_element_with_wait(locator, driver).click()

    @allure.step('Скролим до элемента {locator}')
    def scroll_to_element(self, locator, driver):
        element = self.find_element_with_wait(locator, driver)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст элемента {locator}')
    def get_text_from_element(self, locator, driver):
        return self.find_element_with_wait(locator, driver).text
