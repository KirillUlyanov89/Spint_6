from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_field = (By.CSS_SELECTOR, "[placeholder = '* Имя']")
    surname_field = (By.CSS_SELECTOR, "[placeholder = '* Фамилия']")
    address_field = (By.CSS_SELECTOR, "[placeholder = '* Адрес: куда привезти заказ']")
    metro_field = (By.CSS_SELECTOR, "[placeholder = '* Станция метро']")
    phone_field = (By.CSS_SELECTOR, "[placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[text()='Далее']")
    date_when_to_bring_a_scooter_field = (By.CSS_SELECTOR, "[placeholder = '* Когда привезти самокат']")
    rental_period_dropdown_menu = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    one_day_in_rental_period_menu = (By.XPATH, ".//div[@class='Dropdown-option' and text()='сутки']")
    checkbox_select_black_color_of_the_scooter = (By.XPATH, ".//input[@id='grey']")
    checkbox_select_grey_color_of_the_scooter = (By.XPATH, ".//input[@id='grey']")
    comment_field = (By.CSS_SELECTOR, "[placeholder = 'Комментарий для курьера']")
    order_button_for_complete_the_order = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    order_button_for_yes_the_order = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Да']")
    modal_of_successful_order = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")