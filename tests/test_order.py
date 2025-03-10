import pytest
import allure
import time  # Импортируем модуль time
from pages.order_page import OrderPage
from links import BASE_URL
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators

class TestOrder(OrderPage):
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
        "modal": OrderPageLocators.modal_of_successful_order
    }

    @pytest.mark.parametrize("dict_data", [
        (
         {"name": "Иван",
          "surname": "Иванов",
          "address": "Улица Мира, дом 15",
          "metro": "Черкизовская",
          "phone": "+79999999999",
          "date": "15.03.2025",
          "comment": "Нужен чистый"}),
        (
         {"name": "Петр",
          "surname": "Петров",
          "address": "Улица Мира, дом 21",
          "metro": "Сокольники",
          "phone": "+79999999999",
          "date": "12.11.2024",
          "comment": "Быстрее"}),
    ])
    @allure.title("Оформление заказа")
    @allure.description("Создаем заказ и проверяем, что отображается модальное окно 'Заказ оформлен'")
    @allure.link(BASE_URL, name='https://qa-scooter.praktikum-services.ru/')
    def test_make_an_order(self, dict_data, driver_start):
        driver_start.get(BASE_URL)
        time.sleep(1)  # Задержка перед нажатием кнопки заказа
        self.click_to_element(BasePageLocators.order_button, driver_start)

        # Заполнение полей о заказе
        self.add_fields_in_who_is_the_scooter_for(
            self.dict_locator["name"], dict_data["name"],
            self.dict_locator["surname"], dict_data["surname"],
            self.dict_locator["address"], dict_data["address"],
            self.dict_locator["metro"], dict_data["metro"],
            self.dict_locator["phone"], dict_data["phone"], driver_start
        )
        time.sleep(1)  # Задержка после ввода данных о пользователе

        self.add_fields_in_about_rent(
            self.dict_locator["date"], dict_data["date"],
            self.dict_locator["rent"],
            self.dict_locator["duration"],
            self.dict_locator["color"],
            self.dict_locator["comment"], dict_data["comment"],
            self.dict_locator["button_order"],
            self.dict_locator["button_yes"], driver_start
        )
        time.sleep(1)  # Задержка после ввода данных о заказе

        assert "Заказ оформлен" in self.get_text_from_element(self.dict_locator["modal"], driver_start)

