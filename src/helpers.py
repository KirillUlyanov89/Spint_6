import random
from datetime import date, timedelta
from faker import Faker

fake = Faker(['ru_RU'])

def generate_first_name():
    return fake.first_name()

def generate_last_name():
    return fake.last_name()

def generate_phone_number():
    phone_number = f'89{"".join([str(random.randint(0, 9)) for _ in range(9)])}'
    return phone_number

def generate_rent_date(days_from_today):
    future_date = date.today() + timedelta(days=days_from_today)
    return future_date.strftime('%d.%m.%Y')