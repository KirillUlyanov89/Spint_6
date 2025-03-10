import pytest
import time
from selenium import webdriver
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from links import *

class TestQuestions(MainPage):

    @pytest.mark.parametrize("dict_questions", [
        ({
            "main_locator": MainPageLocators.what_is_the_price,
            "answer_text_locator": MainPageLocators.what_is_the_price_answer,
            "questions_text": "400 рублей",
            "allure": "Сколько это стоит? И как оплатить?"
        }),
        ({
            "main_locator": MainPageLocators.is_it_possible_to_order_several_scooters,
            "answer_text_locator": MainPageLocators.is_it_possible_to_order_several_scooters_answer,
            "questions_text": "один заказ — один самокат",
            "allure": "Хочу сразу несколько самокатов! Так можно?"
        }),
        ({
            "main_locator": MainPageLocators.how_is_rental_time_calculated,
            "answer_text_locator": MainPageLocators.how_is_rental_time_calculated_answer,
            "questions_text": "Отсчёт времени аренды начинается с момента",
            "allure": "Как рассчитывается время аренды?"
        }),
        ({
            "main_locator": MainPageLocators.is_it_possible_to_order_a_scooter_for_today,
            "answer_text_locator": MainPageLocators.is_it_possible_to_order_a_scooter_for_today_answer,
            "questions_text": "Только начиная с завтрашнего дня",
            "allure": "Можно ли заказать самокат прямо на сегодня?"
        }),
        ({
            "main_locator": MainPageLocators.is_it_possible_to_extend_the_order,
            "answer_text_locator": MainPageLocators.is_it_possible_to_extend_the_order_answer,
            "questions_text": "Пока что нет!",
            "allure": "Можно ли продлить заказ или вернуть самокат раньше?"
        }),
        ({
            "main_locator": MainPageLocators.do_you_bring_a_charger,
            "answer_text_locator": MainPageLocators.do_you_bring_a_charger_answer,
            "questions_text": "не понадобится",
            "allure": "Вы привозите зарядку вместе с самокатом?"
        }),
        ({
            "main_locator": MainPageLocators.is_it_possible_to_cancel_an_order,
            "answer_text_locator": MainPageLocators.is_it_possible_to_cancel_an_order_answer,
            "questions_text": "Да, пока самокат не привезли",
            "allure": "Можно ли отменить заказ?"
        }),
        ({
            "main_locator": MainPageLocators.i_live_outside_the_MRR,
            "answer_text_locator": MainPageLocators.i_live_outside_the_MRR_answer,
            "questions_text": "Всем самокатов! И Москве, и Московской области",
            "allure": "Я жизу за МКАДом, привезёте?"
        }),
    ])
    def test_clicking_questions_displays_correct_answers(self, dict_questions, driver_start):
        allure.dynamic.title(dict_questions["allure"])
        allure.dynamic.description("Проверка отображения ответа на вопрос")

        # Задержка перед скроллом к элементу
        time.sleep(1)
        self.scroll_to_element(dict_questions["main_locator"], driver_start)

        # Задержка перед кликом на элемент
        time.sleep(1)
        self.click_to_element(dict_questions["main_locator"], driver_start)

        # Задержка перед получением текста элемента
        time.sleep(1)
        answer_text = self.get_text_from_element(dict_questions["answer_text_locator"], driver_start)

        assert dict_questions["questions_text"] in answer_text, f"Expected answer text: '{dict_questions['questions_text']}', but got: '{answer_text}'"