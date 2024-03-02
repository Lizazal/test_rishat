# Задание

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price) 
- API с двумя методами:
    - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Дополнительные задачи: 
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели

# Запуск проекта

Клонировать репозиторий:
```
git clone https://github.com/Lizazal/test_rishat.git
```
Открыть папку проекта:
```
cd test_rishat
```
Выполнить запуск проекта с помощью Bash-скрипта:
```
run.sh
```
Открыть приложение по адресу:
```
http://localhost:8000/
```
В таком формате запуска в качестве секретных ключей используются тестовые ключи.
Для добавления своих ключей, в папке проекта стоит создать файл .env, в который записать Django-ключ и Public и Secret Stripe ключи:
```
SECRET_KEY = 
STRIPE_PUBLIC_KEY = 
STRIPE_SECRET_KEY = 
```
Для получения Stripe ключей необходимо зарегистрироваться на сайте:
```
https://dashboard.stripe.com/register
```
Возможен запуск через Docker:
```
docker-compose up -d --build
```
Для создания superuser и использования Django Admin панели:
```
python manage.py createsuperuser
```
Возможно всё запустить вручную (требует добавления .env с ключами):
```
git clone https://github.com/Lizazal/test_rishat.git
cd test_rishat
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Существующие страницы

- http://localhost:8000/ список товаров
- admin/ Django Admin панель
- /buy/{id} - session.id
- /item/{id} - страница товара с возможностью покупки
- /success - заглушка при успешной оплате
- /cancel - заглушка при отмене оплаты
