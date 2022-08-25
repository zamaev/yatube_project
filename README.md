# Социальная сеть для блогеров
### Описание
Социальная сеть тех, кто любит критиковать и получать критику для достижения истины.
### Технологии
Python 3.7
Django 2.2.19
### Запуск проекта в dev-режиме
- установите python3.7 (инструкция ниже для Fedora)
```sh
sudo dnf install python3.7
```
- установите и активируйте вируальное окружение
```sh
python3.7 -m venv venv
source venv/bin/activate
```
- установите зависимости из файла requirements.txt
```sh
pip install -r requirements.txt
```
- в папке с файлом `manage.py` выполните команду
```sh
python manage.py runserver
```
### Авторы
Айдрус