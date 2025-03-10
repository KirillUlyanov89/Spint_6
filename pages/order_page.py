from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage


class OrderPage(MainPage):

    def add_text_to_element(self, locator, text, driver):
        self.find_element_with_wait(locator, driver).send_keys(text)

    def add_metro_in_dropdown_menu(self, locator, metro, driver):
        element = self.find_element_with_wait(locator, driver)
        element.send_keys(metro)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def add_data_to_when_to_bring_a_scooter_field(self, locator, date, driver):
        element = self.find_element_with_wait(locator, driver)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def select_rental_period(self, field_locator, duration_locator, driver):
        self.find_element_with_wait(field_locator, driver).click()
        self.find_element_with_wait(duration_locator, driver).click()

    def add_fields_in_who_is_the_scooter_for(self, name_locator, name,
                                             surname_locator, surname,
                                             address_locator, address,
                                             metro_locator, metro,
                                             phone_locator, phone, driver):
        self.add_text_to_element(name_locator, name, driver)
        self.add_text_to_element(surname_locator, surname, driver)
        self.add_text_to_element(address_locator, address, driver)
        self.add_metro_in_dropdown_menu(metro_locator, metro, driver)
        self.add_text_to_element(phone_locator, phone, driver)
        self.click_to_element(OrderPageLocators.next_button, driver)

    def add_fields_in_about_rent(self, date_locator, date,
                                 rent_locator, duration_locator,
                                 color_locator,
                                 comment_locator, comment,
                                 complete_order_button_locator,
                                 yes_complete_order_button_locator, driver):
        self.add_data_to_when_to_bring_a_scooter_field(date_locator, date, driver)
        self.select_rental_period(rent_locator, duration_locator, driver)
        self.click_to_element(color_locator, driver)
        self.add_text_to_element(comment_locator, comment, driver)
        self.click_to_element(complete_order_button_locator, driver)
        self.click_to_element(yes_complete_order_button_locator, driver)