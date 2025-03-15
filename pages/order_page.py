from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage

class OrderPage(MainPage):

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def add_metro_in_dropdown_menu(self, locator, metro):
        element = self.find_element_with_wait(locator)
        element.send_keys(metro)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def add_data_to_when_to_bring_a_scooter_field(self, locator, date):
        element = self.find_element_with_wait(locator)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def select_rental_period(self, field_locator, duration_locator):
        self.find_element_with_wait(field_locator).click()
        self.find_element_with_wait(duration_locator).click()

    def add_fields_in_who_is_the_scooter_for(self, name_locator, name,
                                             surname_locator, surname,
                                             address_locator, address,
                                             metro_locator, metro,
                                             phone_locator, phone):
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(surname_locator, surname)
        self.add_text_to_element(address_locator, address)
        self.add_metro_in_dropdown_menu(metro_locator, metro)
        self.add_text_to_element(phone_locator, phone)
        self.click_to_element(OrderPageLocators.next_button)

    def add_fields_in_about_rent(self, date_locator, date,
                                 rent_locator, duration_locator,
                                 color_locator,
                                 comment_locator, comment,
                                 complete_order_button_locator,
                                 yes_complete_order_button_locator):
        self.add_data_to_when_to_bring_a_scooter_field(date_locator, date)
        self.select_rental_period(rent_locator, duration_locator)
        self.click_to_element(color_locator)
        self.add_text_to_element(comment_locator, comment)
        self.click_to_element(complete_order_button_locator)
        self.click_to_element(yes_complete_order_button_locator)

    def click_to_element(self, locator):
        """Клик на элемент."""
        element = self.find_element_with_wait(locator)
        element.click()