from sender_stand_request import (post_new_user,
                                  post_new_kit)
from data import kit_body


def get_kit_body(kit_name: str) -> dict:
    """
    Функция для изменения значения ключа 'name'
    :param kit_name:
    :return: dict
    """
    # Копируется словарь с телом запроса из файла data
    current_body = kit_body.copy()
    # Изменение значения в поле name
    current_body["name"] = kit_name
    # Возвращается новый словарь с нужным значением name
    return current_body


def positive_assert(kit_name: str) -> None:
    """
    Функция для позитивной проверки
    :param kit_name:
    :return: None
    """
    request_body = get_kit_body(kit_name)
    kit_response = post_new_kit(request_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name


def negative_assert(kit_name: str) -> None:
    """
    # Функция для негативной проверки
    :param kit_name:
    :return: None
    """
    request_body = get_kit_body(kit_name)
    kit_response = post_new_kit(request_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["message"] == 'Не все необходимые параметры были переданы'


def test_kit_1_letter_in_name_get_success_response() -> None:
    """
    Тест 1. Успешное создание набора

    Параметр name состоит из 1 символа
    :return: None
    """
    positive_assert(kit_name="a")


def test_kit_511_letters_in_name_get_success_response() -> None:
    """
    Тест 2. Успешное создание набора

    Параметр name состоит из 511 символов
    :return: None
    """
    positive_assert(kit_name="Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_kit_0_letter_in_name_get_failed_response() -> None:
    """
    Тест 3. Не успешное создание набора

    Параметр name состоит из пустой строки
    :return: None
    """
    negative_assert(kit_name="")


def test_kit_512_letters_in_name_get_failed_response() -> None:
    """
    Тест 4. Не успешное создание набора

    Параметр name состоит из 512 символов
    :return: None
    """
    negative_assert(kit_name="Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_kit_english_letters_in_name_get_success_response() -> None:
    """
    Тест 5. Успешное создание набора

    Параметр name состоит из латинских символов
    :return: None
    """
    positive_assert(kit_name="QWErty")


def test_kit_russian_letters_in_name_get_success_response() -> None:
    """
    Тест 6. Успешное создание набора

    Параметр name состоит из кириллических символов
    :return: None
    """
    positive_assert(kit_name="Мария")


def test_kit_special_symbols_in_name_get_success_response() -> None:
    """
    Тест 7. Успешное создание набора

    Параметр name состоит из специальных символов
    :return: None
    """
    positive_assert(kit_name="№%@")


def test_kit_has_spaces_in_name_get_success_response() -> None:
    """
    Тест 8. Успешное создание набора

    Параметр name содержит пробелы
    :return: None
    """
    positive_assert(kit_name="Человек и КО ")


def test_kit_numbers_in_name_get_success_response() -> None:
    """
    Тест 9. Успешное создание набора

    Параметр name состоит из строки содержащую цифры
    :return: None
    """
    positive_assert(kit_name="123")


def test_kit_with_empty_dict_get_failed_response() -> None:
    """
    Тест 10. Не успешное создание набора

    Передаем в body пустой словарь
    :return: None
    """
    request_body = dict()
    kit_response = post_new_kit(request_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["message"] == 'Не все необходимые параметры были переданы'


def test_kit_integer_in_name_get_failed_response() -> None:
    """
    Тест 11. Не успешное создание набора

    Параметр name является типом integer
    :return: None
    """
    negative_assert(kit_name=123)
