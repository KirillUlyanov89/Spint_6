import allure
import src.data as data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage

@allure.suite('Тесты переходов по ссылкам в верхнем меню')
class TestTransitionPage:
    @allure.title('Переход на страницу главную страницу по логотипу "Самоката"')
    def test_transition_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_page()
        
        order_page = OrderPage(driver)
        assert order_page.get_user_info_header().text == data.order_form_user_info_header_text

        redirect_page = RedirectPage(driver)
        redirect_page.go_to_main_page_by_scooter_logo()
        assert data.scooter_header in main_page.get_main_header_text()

    @allure.title('Переход на страницу Дзен по логотипу "Яндекс"')
    def test_transition_by_yandex_logo(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.go_to_dzen_by_yandex_logo()
        assert redirect_page.get_dzen_news_text() == data.dzen_header