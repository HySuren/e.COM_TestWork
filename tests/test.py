import datetime

import requests

BASE_URL = "http://127.0.0.1:8000"


valid_payload = {
  "user_name": "John Doe",
  "order_date": "12.12.2024",
  "lead_email": "test@example.com",
  "phone_number": "+7 123 456 78 20"
}



not_valid_payload = {
        "emaisl": "tesфтлффошфошф.com",
        "phone": "фшфофщшошфошщф"
    }


def test_register_user(payload: dict):
    response = requests.post(f"{BASE_URL}/get_form", json=payload)
    print("Register Response:", response.json())


if __name__ == "__main__":
    test_register_user(valid_payload)
    test_register_user(not_valid_payload)
