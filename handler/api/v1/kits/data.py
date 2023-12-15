from faker import Faker
from random import randint


# Создаем экземпляр класса Faker, для дальнейшей генерации фейковых данных клиента
fake = Faker('ru_RU')


user_data = dict(firstName=fake.first_name_nonbinary(),
                 phone='+7910' + str(randint(1000000, 9999999)),
                 address="г. Москва, ул. Пушкина, д. " + str(randint(0, 999)))

headers = dict({"Authorization": "Bearer 34b3bc2d-2e82-4b2f-bfa4-cafb327fd7c9"})

kit_body = dict({"name": "a"})
