from selenium.webdriver.common.by import By

# Локатор для лого сервиса "Яндекс Самокат" - слово "Самокат" 
SCOOTER_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')

# Локатор для лого сервиса "Яндекс Самокат" - слово "Яндекс"
YANDEX_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')

# Локатор для теста "Новости" в Дзен
DZEN_NEWS_TEXT = (By.XPATH, '//div[@data-testid="floor-title-text" and text()="Новости"]')
