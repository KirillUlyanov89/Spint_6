import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage
from links import BASE_URL
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from .test_data import test_data
# ПОСМОТРИТЕ ВИДЕО РАБОТЫ КОДА https://drive.google.com/file/d/1lmrM793x4B73Nygb18GYq5QZZ5IjA24E/view?usp=sharing

class TestOrder:
    dict_locator = {
        "name": OrderPageLocators.name_field,
        "surname": OrderPageLocators.surname_field,
        "address": OrderPageLocators.address_field,
        "metro": OrderPageLocators.metro_field,
        "phone": OrderPageLocators.phone_field,
        "date": OrderPageLocators.date_when_to_bring_a_scooter_field,
        "rent": OrderPageLocators.rental_period_dropdown_menu,
        "duration": OrderPageLocators.one_day_in_rental_period_menu,
        "color": OrderPageLocators.checkbox_select_black_color_of_the_scooter,
        "comment": OrderPageLocators.comment_field,
        "button_order": OrderPageLocators.order_button_for_complete_the_order,
        "button_yes": OrderPageLocators.order_button_for_yes_the_order,
        "modal": OrderPageLocators.modal_of_successful_order,
    }

    @pytest.mark.parametrize("dict_data", test_data)  # Используем данные из test_data
    @allure.title("Оформление заказа")
    @allure.description("Создаем заказ и проверяем, что отображается модальное окно 'Заказ оформлен'")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_make_an_order(self, dict_data, driver_start):
        order_page = OrderPage(driver_start)
        driver_start.get(BASE_URL)

        # Ожидание загрузки кнопки заказа в заголовке
        WebDriverWait(driver_start, 10).until(
            EC.element_to_be_clickable(BasePageLocators.order_button_header)
        ).click()

        # Заполнение полей о заказе
        order_page.add_fields_in_who_is_the_scooter_for(
            self.dict_locator["name"], dict_data["name"],
            self.dict_locator["surname"], dict_data["surname"],
            self.dict_locator["address"], dict_data["address"],
            self.dict_locator["metro"], dict_data["metro"],
            self.dict_locator["phone"], dict_data["phone"]
        )

        # Заполнение полей о прокате
        order_page.add_fields_in_about_rent(
            self.dict_locator["date"], dict_data["date"],
            self.dict_locator["rent"], self.dict_locator["duration"],
            self.dict_locator["color"],
            self.dict_locator["comment"], dict_data["comment"],
            self.dict_locator["button_order"],
            self.dict_locator["button_yes"]
        )

        # Ожидание модального окна успешного заказа
        modal_message = WebDriverWait(driver_start, 10).until(
            EC.visibility_of_element_located(self.dict_locator["modal"])
        )

        # Проверка на успех оформления заказа
        assert "Заказ оформлен" in modal_message.text

        # ПОСМОТРИТЕ ВИДЕО РАБОТЫ КОДА https://drive.google.com/file/d/1lmrM793x4B73Nygb18GYq5QZZ5IjA24E/view?usp=sharing