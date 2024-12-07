Здраствуйте e.Ком!
# Инструкция по запуску приложения
- ## 0 шаг
  Убедитесь что у вас установлен Docker и MongoDB, так же обратите внимание на .env
- ## 1 шаг - Клонирование репозитория
  Создайте проект, и клонируйте репозиторий
  ```
  git clone https://github.com/HySuren/e.COM_TestWork.git
  ```
- ## 2 шаг - Docker
  Соберем docker контейнер
  ```
  docker-compose up --build
  ```
- ## 3 шаг - Тестирование
  В проекте через консоль запустите test.py
  
  Windows
  ```
   python tests/test.py
  ```

  Linux
  ```
   python3 tests/test.py
  ```

  ### Шаблоны форм в MongoDB (коллекция form_templates)
  ```
  [
  {
    "name": "Order Form",
    "user_name": "text",
    "order_date": "date",
    "lead_email": "email",
    "phone_number": "phone"
  },
  {
    "name": "Registration Form",
    "first_name": "text",
    "last_name": "text",
    "email": "email",
    "phone": "phone"
  }
  ]
  ```

  ### Тестовые данные такие:

  ```
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
  ```

  Ответ будет такой:
  ```
  Register Response: {'template_name': 'Order Form'}
  Register Response: {'emaisl': 'text', 'phone': 'text'}
  ```
