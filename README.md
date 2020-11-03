# rentacar
Тестовое задание для собеседования.

Рабочую версию можно проверит по адресу https://brainsite.ru
 
API сайта
 
Добавление пользователя: https://brainsite.ru/api/add_user/
Список пользователейс их машинами: https://brainsite.ru/api/users/
Просмотр и редактирование пользователя: https://brainsite.ru/api/users/<id>  где <id> это ID пользователя

# Задание
Python + Django

Разрабатываем систему обеспечивающую работу организации по сдаче автомобилей в аренду.
Пользователь может брать в аренду различные автомобили, и автомобиль может сдаваться различным пользователям.
У пользователя есть атрибуты email, имя, язык(en, ru). У машин есть атрибуты имя(задается на двух языках en, ru), год создания, и дата добавления машины в систему.
Нужно реализовать RestAPI со следующим функционалом:
- зарегистрировать пользователя
- получить машины пользователя
- изменить данные пользователя
- получить всех пользователей
Для api нужно использовать token based authentication.


Сайт должен предоставлять следующий функционал:
- зарегистрировать пользователя/войти
- добавить машину в систему
- добавить машину пользователю
- информация о пользователе
- изменить информацию о пользователе
- Неавторизованному пользователю доступна только страница зарегистрировать пользователя/войти, при открытии других страниц неавторизованным пользователем должен производиться редирект на страницу зарегистрировать пользователя/войти.
- При добавлении машины пользователю посылается письмо. 
- Для авторизации используется пара email-пароль.
- Для функционирования системы база данных наполняется тестовыми данными любым удобным способом.
