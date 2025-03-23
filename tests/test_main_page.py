import pytest
import allure
import src.data as data
from pages.main_page import MainPage

@allure.suite('Тесты главной страницы сервиса "Яндекс Самокат"')
class TestMainPage:

    @allure.title('Проверка соответствия текста ответа вопросу в секции "Как это работает"')
    @pytest.mark.parametrize('num, answer_text',
        [
            (0, data.question_1_answer_text),
            (1, data.question_2_answer_text),
            (2, data.question_3_answer_text),
            (3, data.question_4_answer_text),
            (4, data.question_5_answer_text),
            (5, data.question_6_answer_text),
            (6, data.question_7_answer_text),
            (7, data.question_8_answer_text)
        ])
    def test_valid_answers_to_question_in_how_it_works_section(self, driver, num, answer_text):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == answer_text