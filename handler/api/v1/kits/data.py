from faker import Faker
from random import randint
import configuration

# Создаем экземпляр класса Faker, для дальнейшей генерации фейковых данных клиента
fake = Faker('ru_RU')


user_data = dict(firstName=fake.first_name_nonbinary(),
                 phone='+7910' + str(randint(1000000, 9999999)),
                 address="г. Москва, ул. Пушкина, д. " + str(randint(0, 999)))

headers = dict({"Authorization": configuration.USER_TOKEN})

kit_body = dict({"name": "a"})
