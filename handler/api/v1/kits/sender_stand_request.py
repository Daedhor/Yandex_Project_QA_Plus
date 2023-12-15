import requests
import configuration
import data
import os


def post_new_user():
    """
    Функция для создания нового тестового клиента с уникальными данными.

    Делает каждый тест-раны не зависимыми друг от друга и исключает ошибки в создании нового юзера.
    :return: authToken юзера
    """
    result = (requests.post(configuration.BASE_URL + configuration.CREATE_USER_PATH,
                            json=data.user_data).json())
    os.environ["USER_TOKEN"] = "Authorization: Bearer " + result['authToken']


def post_new_kit(kit_body) -> requests.Response:
    """
    Функция для создания нового набора пользователя
    :return: Response in JSON format
    """
    return requests.post(configuration.BASE_URL + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=data.headers)
