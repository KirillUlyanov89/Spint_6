from selenium.webdriver.common.by import By

# Локаторы для формы заполнения пользователя
USER_INFO_FORM = (By.XPATH, '//div[contains(@class, "Order_Form")]')
USER_INFO_HEADER = (By.XPATH, '//div[contains(@class, "Order_Header") and text()="Для кого самокат"]')

# Локаторы для полей заполнения формы пользователя
class UserForm:
    FIRST_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_LIST = (By.XPATH, '//div[@class="select-search__select"]')
    METRO_STATION_BUTTON = (By.XPATH, '//button[contains(@class, "select-search__option")]//div[text()="{}"]')
    PHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button')

# Локатор для формы заполнения деталей аренды
RENT_INFO_HEADER = (By.XPATH, '//div[contains(@class, "Order_Header") and text()="Про аренду"]')

# Локаторы для полей заполнения формы данных аренды
class RentForm:
    START_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_PERIOD = (By.XPATH, '//span[@class="Dropdown-arrow"]')
    RENT_PERIOD_ITEM = (By.XPATH, '//div[contains(@class, "Dropdown-option") and text()="{}"]')
    BLACK_COLOR = (By.ID, 'black')
    GREY_COLOR = (By.ID, 'grey')
    COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')

# Локатор кнопки подтверждения заказа в окне "Хотите оформить заказ?"
RENT_CONFIRMATION_BUTTON = (By.XPATH, '//button[text()="Да"]')

# Локатор для заголовка с окна "Заказ оформлен"
ORDER_DONE_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]')