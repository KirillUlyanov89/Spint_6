import src.helpers as helpers

# URL главной страница сервиса
main_page_url = 'https://qa-scooter.praktikum-services.ru/'

# Информация для проверки функциональности заказа самоката
order_form_user_info_header_text = 'Для кого самокат'
order_form_rent_info_header_text = 'Про аренду'
order_form_finish_header_text = 'Заказ оформлен'

# Информация для проверки редиректа между страницами
scooter_header = 'Самокат'
dzen_header = 'Новости'

user_info_1 = {
    'first_name': helpers.generate_first_name(),
    'last_name': helpers.generate_last_name(),
    'address': 'Маяковского, 1',
    'metro_station': 'ВДНХ',
    'phone_number': helpers.generate_phone_number()
}

rent_info_1 = {
    'start_date': helpers.generate_rent_date(2),
    'rent_period': 'двое суток',
    'color': 'grey',
    'comment': 'Нужен чистый'
}

user_info_2 = {
    'first_name': helpers.generate_first_name(),
    'last_name': helpers.generate_last_name(),
    'address': 'Ленина, 14',
    'metro_station': 'Лубянка',
    'phone_number': helpers.generate_phone_number()
}

rent_info_2 = {
    'start_date': helpers.generate_rent_date(3),
    'rent_period': 'трое суток',
    'color': 'black',
    'comment': 'Не звонить'
}

# Информация об ответах на вопросы в разделе "Вопросы о важном"
question_1_answer_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
question_2_answer_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
question_3_answer_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
question_4_answer_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
question_5_answer_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
question_6_answer_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
question_7_answer_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
question_8_answer_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'