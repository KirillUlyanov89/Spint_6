import allure
import locators.redirect_page_locators as locators
from pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('Переходим на главную страницу через логотип "Самокат"')
    def go_to_main_page_by_scooter_logo(self):
        self.click_to_element(locators.SCOOTER_LOGO)

    @allure.step('Переход на "Дзен" через логотип "Яндекс"')
    def go_to_dzen_by_yandex_logo(self):
        self.click_to_element(locators.YANDEX_LOGO)
        self.change_browser_tab(-1)

    @allure.step('Получаем заголовок раздела со страницы "Дзен"')
    def get_dzen_news_text(self):
        return self.find_element(locators.DZEN_NEWS_TEXT).text