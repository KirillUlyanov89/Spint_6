from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self, locator, value):
        """Заполнение текстового поля."""
        input_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        input_element.clear()
        input_element.send_keys(value)

    def click_to_element(self, locator):
        """Клик на элемент."""
        # Здесь не требуется передача driver, так как он доступен как self.driver
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()