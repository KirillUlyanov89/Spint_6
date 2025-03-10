from selenium.webdriver.common.by import By


class MainPageLocators:
    what_is_the_price = [By.ID, "accordion__heading-0"]
    what_is_the_price_answer = [By.XPATH, ".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]
    is_it_possible_to_order_several_scooters = [By.ID, "accordion__heading-1"]
    is_it_possible_to_order_several_scooters_answer = [By.XPATH, ".//p[text()='Пока что у нас так: один заказ — "
                                                                 "один самокат. Если хотите покататься с друзьями, "
                                                                 "можете просто сделать несколько заказов — "
                                                                 "один за другим.']"]
    how_is_rental_time_calculated = [By.ID, "accordion__heading-2"]
    how_is_rental_time_calculated_answer = [By.XPATH, ".//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим"
                                                      " самокат 8 мая в течение дня. "
                                                      "Отсчёт времени аренды начинается с момента,"
                                                      " когда вы оплатите заказ курьеру. "
                                                      "Если мы привезли самокат 8 мая в 20:30, "
                                                      "суточная аренда закончится 9 мая в 20:30.']"]
    is_it_possible_to_order_a_scooter_for_today = [By.ID, "accordion__heading-3"]
    is_it_possible_to_order_a_scooter_for_today_answer = [By.XPATH, ".//p[text()='Только начиная с завтрашнего дня. "
                                                                    "Но скоро станем расторопнее.']"]
    is_it_possible_to_extend_the_order =  [By.ID, "accordion__heading-4"]
    is_it_possible_to_extend_the_order_answer = [By.XPATH, ".//p[text()='Пока что нет! Но если что-то срочное — всегда "
                                                           "можно позвонить в поддержку по красивому номеру 1010.']"]
    do_you_bring_a_charger = [By.ID, "accordion__heading-5"]
    do_you_bring_a_charger_answer = [By.XPATH, ".//p[text()='Самокат приезжает к вам с полной зарядкой. "
                                               "Этого хватает на восемь суток — даже если будете кататься без передышек "
                                               "и во сне. Зарядка не понадобится.']"]
    is_it_possible_to_cancel_an_order = [By.ID, "accordion__heading-6"]
    is_it_possible_to_cancel_an_order_answer = [By.XPATH, ".//p[text()='Да, пока самокат не привезли. Штрафа не будет, "
                                                          "объяснительной записки тоже не попросим. Все же свои.']"]
    i_live_outside_the_MRR = [By.ID, "accordion__heading-7"]
    i_live_outside_the_MRR_answer = [By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! "
                                               "И Москве, и Московской области.']"]