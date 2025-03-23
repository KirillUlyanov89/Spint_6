from selenium.webdriver.common.by import By

# Локатор для верхнего меню на главной странице сайта
MAIN_PAGE_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header")]')

# Локатор для кнопки "Заказать" в верхнем меню сайта
HEADER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')

# Локатор для кнопки "Заказать" в секции "Как это работает"
SECTION_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')

# Локатор для вопросов в секции "Вопросы о важном"
QUESTION = (By.ID, 'accordion__heading-{}')

# Локатор для ответов в секции "Вопросы о важном"
ANSWER = (By.XPATH, '//div[@id="accordion__panel-{}"]/p')