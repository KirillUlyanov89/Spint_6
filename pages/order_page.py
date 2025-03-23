import allure
import locators.order_page_locators as locators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Ожидание появления формы "Для кого самокат"')
    def wait_user_info_form(self):
        self.find_element(locators.USER_INFO_FORM)

    @allure.step('Получение заголовка формы "Для кого самокат"')
    def get_user_info_header(self):
        return self.find_element(locators.USER_INFO_HEADER)

    @allure.step('Выбор станции метро в форме "Для кого самокат"')
    def select_metro_station(self, station_name):
        self.click_to_element(locators.UserForm.METRO_STATION)
        self.find_element(locators.UserForm.METRO_STATION_LIST)
        station_button_locator = (
            locators.UserForm.METRO_STATION_BUTTON[0],
            locators.UserForm.METRO_STATION_BUTTON[1].format(station_name)
        )
        self.click_to_element(station_button_locator)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_user_info_form(self, user_info):
        self.text_input_to_element(locators.UserForm.FIRST_NAME, user_info['first_name'])
        self.text_input_to_element(locators.UserForm.LAST_NAME, user_info['last_name'])
        self.text_input_to_element(locators.UserForm.ADDRESS, user_info['address'])
        self.text_input_to_element(locators.UserForm.PHONE_NUMBER, user_info['phone_number'])
        self.select_metro_station(user_info['metro_station'])
        self.click_to_element(locators.UserForm.NEXT_BUTTON)

    @allure.step('Получаем заголовок формы "Про аренду"')
    def get_rent_info_header(self):
        return self.find_element(locators.RENT_INFO_HEADER)

    @allure.step('Выбор периода аренды')
    def select_rent_period(self, rent_period):
        self.click_to_element(locators.RentForm.RENT_PERIOD)
        self.click_to_element(self.format_locator(locators.RentForm.RENT_PERIOD_ITEM, rent_period))

    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_info_form(self, rent_info):
        self.text_input_to_element(locators.RentForm.START_DATE, rent_info['start_date'])
        self.select_rent_period(rent_info['rent_period'])
        if rent_info['color'] == 'black':
            self.click_to_element(locators.RentForm.BLACK_COLOR)
            self.click_to_element(locators.RentForm.GREY_COLOR)
        self.text_input_to_element(locators.RentForm.COMMENT, rent_info['comment'])

    @allure.step('Клик по кнопке "Заказать" на форме "Про аренду"')
    def click_order_finish_button(self):
        self.click_to_element(locators.RentForm.ORDER_BUTTON)

    @allure.step('Клик по кнопке "Да" в диалоге подтверждения заказа')
    def confirm_rent(self):
        self.click_to_element(locators.RENT_CONFIRMATION_BUTTON)

    @allure.step('Получение заголовка диалога с информацией о заказе')
    def get_order_info_header(self):
        return self.find_element(locators.ORDER_DONE_HEADER)