### Hexlet tests and linter status:
[![Actions Status](https://github.com/u-shev/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/u-shev/python-project-52/actions)
![Tests&Coverage](https://github.com/u-shev/python-project-52/actions/workflows/tests-coverage.yml/badge.svg)
![Linter check](https://github.com/u-shev/python-project-52/actions/workflows/linter-check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/b6dec8c80cd1ee2878cf/maintainability)](https://codeclimate.com/github/u-shev/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b6dec8c80cd1ee2878cf/test_coverage)](https://codeclimate.com/github/u-shev/python-project-52/test_coverage)

### [Task Manager](https://task-manager-708m.onrender.com/) – система управления задачами. Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация:
![Авторизация](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjQ0YWQ5NmU4ODg4M2FmNjQzY2Q0NDk2ODdkY2IxNjA5LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=99f42fbf385e3edff99b0f369f561793478d8be02b0593707898d70ed406742a)
![Привет](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjZjZGE5NDgxMDBiYTdhYjYyNDY0NWVhMWI2MGI4ZWVhLnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=b0a97936e97fa31dfd06a5013a90effe20be352dd142ce9ddf53748842c221cc)
![Задачи](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjA1MGY1MTc5ZjJkMTJhZjk2N2E3OWMyYzhhYjg0N2Q5LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=39fa5674a2ef9c60338539540b36423cedf327f28b57c43c62ce7416513c10f4)

### Установка
Для корректной работы нужны версии python 3.8.1 и poetry 1.4.2, также нужно установить PostrgreSQL.
#### Клонирование репозитария
```
git clone git@github.com:u-shev/python-project-52.git
cd python-project-52
```  
#### Создание базы данных
```
whoami
{username}
sudo -u postgres createuser --createdb {username} 
createdb {databasename}
psql {databasename} < database.sql
```
Локально можно использовать SQLite
#### Секретные ключи
Создать в директории task_manager .env файл для переменных окружения со следующей информацией:  
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/{databasename}  
SECRET_KEY='{your secret key}'
#### Установка зависимостей
```make install```  
#### Подготовка базы данных
```make migrate```  
#### Запуск проекта
```
make run
```  
#### Команды для деплоя
```
make build    
make start
```  
