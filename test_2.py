import requests
import logging
import pytest
from testpage import OperationsHelper


def test_authentication_and_user_profile(browser):
    logging.info("Test Authentication and User Profile Starting")
    testpage = OperationsHelper(browser)

    # Ваш код для получения токена авторизации

    # Пример:
    auth_data = {
        'username': 'bobot2040',
        'password': 'e37c848bc3'
    }

    # URL для авторизации (замените на реальный)
    auth_url = 'https://test-stand.gb.ru/api/auth/login'

    # Выполняем запрос на авторизацию
    response = requests.post(auth_url, data=auth_data)

    # Проверяем успешность запроса
    assert response.status_code == 200, f"Failed to authenticate. Status code: {response.status_code}"

    # Получаем токен из ответа
    auth_token = response.json().get('token')

    # Добавляем токен в заголовки запросов
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    # Пример запроса данных о текущем пользователе (замените на реальный)
    user_profile_url = 'https://test-stand.gb.ru/api/users/profile'

    # Выполняем запрос данных о пользователе
    user_profile_response = requests.get(user_profile_url, headers=headers)

    # Проверяем успешность запроса
    assert user_profile_response.status_code == 200, f"Failed to get user profile. Status code: {user_profile_response.status_code}"

    # Проверяем, что данные о пользователе соответствуют ожидаемым
    expected_username = 'bobot2040'  # Замените на ожидаемое имя пользователя
    actual_username = user_profile_response.json().get('username')

    assert actual_username == expected_username, f"Unexpected username. Expected: {expected_username}, Actual: {actual_username}"

    logging.info("Test Authentication and User Profile Passed")


if __name__ == "__main__":
    # Пример использования теста
    pytest.main(["-v", "test_2.py"])
