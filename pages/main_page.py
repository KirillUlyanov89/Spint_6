import allure
import locators.main_page_locators as locators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие форму заказа по кнопке в верхнем меню сайта')
    def open_user_info_form_by_header_button(self):
        self.click_to_element(locators.HEADER_ORDER_BUTTON)

    @allure.step('Открытие формы заказа по кнопке в секции "Как это работает"')
    def open_user_info_form_by_content_button(self):
        self.scroll_to_element(locators.SECTION_ORDER_BUTTON)
        self.click_to_element(locators.SECTION_ORDER_BUTTON)

    @allure.step('Получение текста ответа по номеру вопроса')
    def get_answer_text(self, num):
        question_locator = self.format_locator(locators.QUESTION, num)
        answer_locator = self.format_locator(locators.ANSWER, num)
        self.scroll_to_element(question_locator)
        self.click_to_element(question_locator)
        return self.get_text_from_element(answer_locator)

    @allure.step('Получаем текст заголовка на главной странице')
    def get_main_header_text(self):
        return self.find_element(locators.MAIN_PAGE_HEADER).text

    @allure.step('Переход к форме заказа')
    def go_to_order_page(self):
        self.click_to_element(locators.HEADER_ORDER_BUTTON)
