import pytest
import allure
import src.data as data
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.suite('Тесты страниц заказа аренды сервиса "Яндекс Самокат"')
class TestOrderPage:
    @allure.title('Создание заказа через кнопку "Заказать" в верхнем меню сайта')
    @pytest.mark.parametrize('user_info, rent_info',
        [
            (data.user_info_1, data.rent_info_1),
            (data.user_info_1, data.rent_info_2)
        ])
    
    def test_make_order_from_header(self, driver, user_info, rent_info):
        main_page = MainPage(driver)
        main_page.open_user_info_form_by_header_button()

        order_page = OrderPage(driver)
        order_page.wait_user_info_form()
        order_page.fill_user_info_form(user_info)
        assert order_page.get_rent_info_header().text == data.order_form_rent_info_header_text

        order_page.fill_rent_info_form(rent_info)
        order_page.click_order_finish_button()
        order_page.confirm_rent()
        assert data.order_form_finish_header_text in order_page.get_order_info_header().text

    @allure.title('Создание заказа через кнопку "Заказать" после секции "Как это работает"')
    @pytest.mark.parametrize('user_info, rent_info',
        [
            (data.user_info_1, data.rent_info_1),
            (data.user_info_1, data.rent_info_2)
        ])
    
    def test_make_order_from_how_it_works_section(self, driver, user_info, rent_info):
        main_page = MainPage(driver)
        main_page.open_user_info_form_by_content_button()
        
        order_page = OrderPage(driver)
        order_page.wait_user_info_form()
        order_page.fill_user_info_form(user_info)
        assert order_page.get_rent_info_header().text == data.order_form_rent_info_header_text

        order_page.fill_rent_info_form(rent_info)
        order_page.click_order_finish_button()
        order_page.confirm_rent()
        assert data.order_form_finish_header_text in order_page.get_order_info_header().text