import requests
import pytest


# POST /v1/customers
# GET /v1/customers/{customer_id}
# POST /v1/customers/{customer_id}
# DELETE /v1/customers/{customer_id}

# Позитивные тесты:
# Создание пользователя с минимально необходимыми данными (только обязательные поля).
# Создание пользователя с корректно заполненными всеми полями (обязательные и дополнительные).
# Создание пользователя с валидным email.
# Негативные тесты:
# Отправка запроса без обязательных полей.
# Использование невалидного email.
# Передача данных в некорректном формате (например, вместо JSON).
# Попытка создать пользователя с уже существующим email.
# Запрос без авторизационного токена.



ART_URL = "https://api.artic.edu/api/v1/artworks?id,title,artist_display"
BASE_URL = "https://api.stripe.com/v1/customers"
API_KEY = "sk_test_51QYo7jH2UvoV83PCPhxtd3PNyliQnPghuP372Jqc6k4CWWLD2VE8wzkiKhA8dLuIk2u5fdnfIYqv9ojOPDqmZPkT00brGWsHl1"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def test_create_customer_valid():
    data = {
        "email": "test_user@example.com",
        "description": "Test user creation"
    }
    response = requests.post(BASE_URL, headers=headers, data=data)
    assert response.status_code == 200, f"Expected 400 but got {response.status_code}"

def test_create_customer_missing_required_fields():
    data = {
        "emailll": "test_user@example.com",
        "descriptionnnn": "Test user creation"
    }
    response = requests.post(BASE_URL, headers=headers, data=data)
    assert response.status_code == 400, f"Expected 400 but got {response.status_code}"

def test_create_customer_invalid_email():
    data = {
        "email": "invalid-email",
        "description": "Invalid email test"
    }
    response = requests.post(BASE_URL, headers=headers, data=data)
    assert response.status_code == 400, f"Expected 400 but got {response.status_code}"
    print("Test Passed: Invalid email")


# -------------------------4

user_id = None

def test_create_users():
    global user_id
    user_data = {"email": "new_user@example.com"}
    create_response = requests.post(BASE_URL, headers=headers, data=user_data)
    assert create_response.status_code == 200
    created_user = create_response.json()
    assert created_user["email"] == user_data["email"]
    user_id = create_response.json()["id"]

def test_read_users():
    global user_id
    read_response = requests.get(f"{BASE_URL}/{user_id}", headers=headers)
    assert read_response.status_code == 200
    assert read_response.json()["email"] =="new_user@example.com"

def test_update_users():
    global user_id
    updated_data = {"email": "update_user@example.com"}
    update_response = requests.post(f"{BASE_URL}/{user_id}", headers=headers, data=updated_data)
    assert update_response.status_code == 200
    assert update_response.json()["email"] =="update_user@example.com"

def test_delete_users():
    global user_id
    delete_response = requests.delete(f"{BASE_URL}/{user_id}", headers=headers)
    assert delete_response.status_code == 200


# --------------------------5


def test_empty_request_body():
    json_data = {}
    response = requests.post(BASE_URL, headers=headers, data=json_data)
    assert response.status_code == 200

def test_invalid_data_format():
    json_data = {
        "email": 7214,
        "description": 89213
    }
    response = requests.post(BASE_URL, headers=headers, data=json_data)
    assert response.status_code == 400

def test_nonexistent_endpoint():
    response = requests.get(f"{BASE_URL}/felwkf", headers=headers)
    assert response.status_code == 404


# ----------------------------6

def test_access_without_token():
    response = requests.get(BASE_URL)
    assert response.status_code == 401

def test_access_with_invalid_token():
    response = requests.get(BASE_URL, headers={"Authorization": "Bearer fjkekjdnkj"})
    assert response.status_code == 401


# --------------------------------7

def test_invalid_long_string():
    data = {"email": "a" * 1000 + "@example.com"}
    response = requests.post(BASE_URL, headers=headers, data=data)
    assert response.status_code == 400

def test_required_field_missing():
    authorization = {
        "Authorization": f"Bearer"
    }
    response = requests.post(BASE_URL, headers=authorization)
    assert response.status_code == 401

# ---------------------------8
    
def test_pagination():
    response = requests.get(f"{ART_URL}&page=2&limit=5",)
    assert response.status_code == 200
    assert len(response.json()) <= 5

def test_pagination_out_of_range():
    response = requests.get(f"{ART_URL}&page=9&limit=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5