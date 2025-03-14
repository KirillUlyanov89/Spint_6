import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestQuestions:

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
    @allure.title("Проверка ответов на вопросы")
    @allure.description("Проверка отображения ответа на вопрос на главной странице")
    def test_clicking_questions_displays_correct_answers(self, dict_questions, driver_start):
        main_page = MainPage(driver_start)

        allure.dynamic.title(dict_questions["allure"])

        # Прокручиваем к самому низу страницы
        driver_start.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Прокручиваем к элементу и ждем его появления
        main_page.scroll_to_element(dict_questions["main_locator"])
        WebDriverWait(driver_start, 10).until(
            EC.element_to_be_clickable(dict_questions["main_locator"])
        )

        # Нажимаем на вопрос
        main_page.click_to_element(dict_questions["main_locator"])

        # Ожидаем отображения ответа и получаем текст
        WebDriverWait(driver_start, 10).until(
            EC.visibility_of_element_located(dict_questions["answer_text_locator"])
        )
        answer_text = main_page.get_text_from_element(dict_questions["answer_text_locator"])

        assert dict_questions["questions_text"] in answer_text, (
            f"Expected answer text: '{dict_questions['questions_text']}', but got: '{answer_text}'"
        )