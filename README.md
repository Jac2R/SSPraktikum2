# SimbirSoft-Praktikum2: Задание API PyTest+Requests+Pydantic

---

## Описание проекта | Project Description

Данный репозиторий содержит 5 автотестов для тестирования API. Тестируются позитивные кейсы.

Реализовано с использованием PyTest, модуля Requests и модуля Pydantic.

---

## Требования | Pre-requisites:

* Python 3.10
* Склонированный и развернутый проект API при помощи Docker: https://github.com/sun6r0/test-service#

---

### Объект тестирования | Tested API

[Сервис API](https://github.com/sun6r0/test-service#)

---

## Содержание

- [Описание проекта | Project Description](#описание-проекта--project-description)
- [Требования | Pre-requisites](#требования--pre-requisites)
- [Объект тестирования | Tested Website](#объект-тестирования--tested-website)
- [Технологии | Tech Stack](#технологии--tech-stack)
- [Как запустить автотесты? | How to run Tests?](#как-запустить-автотесты--how-to-run-tests)
  - [Локальная установка проекта | Local Installation Guide](#локальная-установка-проекта--local-installation-guide)
- [Тестовая документация | Test Documentation](#тестовая-документация--test-documentation)
  - [Тест-кейсы | Test Cases](#тест-кейсы--test-cases)
    - [TC01 - Создание сущности POST](#tc01---создание-сущности-post)
    - [TC02 - Получение списка сущностей GET All](#tc02---получение-списка-сущностей-get-all)
    - [TC03 - Получение сущности по ID GET by id](#tc03---получение-сущности-по-id-get-by-id)
    - [TC04 - Обновление сущности и её дополнений PATCH](#tc04---обновление-сущности-и-её-дополнений-patch)
    - [TC05 - Удаление сущности и её дополнений DELETE](#tc05---удаление-сущности-и-её-дополнений-delete)
- [Allure Report](#allure-report)

---

## Технологии | Tech Stack

Проект реализован с использованием следующих инструментов:

* Python 3.10
* Requests 2.33.1
* PyTest 9.0.3
* Pydantic 2.13.3
* Allure Reports 2.15.3

Необходимые версии модулей для установки указаны в файле проекта [requirements.txt](requirements.txt)

---

## Как запустить автотесты? | How to run Tests?

### Локальная установка проекта | Local Installation Guide

Перед загрузкой репозитория убедись, что у тебя установлена версия Python 3.10. Инструкция по установке версии 3.10 находится тут.

1. Клонируй репозиторий с проектом в свою любимую папку с проектами:
```
    git clone git@github.com:Jac2R/SSPraktikum2.git
```
2. Установи модули, использовав команду:
```
    pip install -r requirements.txt
```
3. Запусти тесты:
```
    pytest -v -s
```
4. Запусти Allure report:
```
    pytest --alluredir=allure-results
    allure serve allure-results
```

---

# Тестовая документация | Test Documentation

## Тест-кейсы | Test Cases

### TC01 - Создание сущности POST

**Метод**: POST /api/create

**Предусловие**: Сервис запущен

**Шаги**

1. Отправить POST-запрос с валидным JSON:


    {
        "addition": {
            "additional_info": "Дополнительные сведения",
            "additional_number": 123
        },
        "important_numbers": [
            42,
            87,
            15
        ],
        "title": "Основная сущность в Python",
        "verified": True
    }

2. Посмотреть на response

**Ожидаемый результат**

* Статус код: 200 Created
* В ответе присутствует id созданной сущности

---

### TC02 - Получение списка сущностей GET All

**Метод**: GET /api/getAll

**Предусловие**: В системе есть хотя бы 1 сущность

**Шаги**

1. Отправить GET-запрос
2. Посмотреть на response

**Ожидаемый результат**

* Статус код: 200 OK
* В ответе представлен список сущностей entity

---

### TC03 - Получение сущности по ID GET by id

**Метод**: GET /api/get/{id}

**Предусловие**: В системе существует сущность с id = X

**Шаги**

1. Отправить GET-запрос с валидным id
2. Посмотреть на response

**Ожидаемый результат**

* Статус код: 200 OK
* В ответе id = X
* Представлены корректные поля сущности

---

### TC04 - Обновление сущности и её дополнений PATCH

**Метод**: PATCH /api/patch/{id}

**Предусловие**: В системе существует сущность с id = X

**Шаги**

1. Отправить PATCH-запрос с измененными сведениями в JSON:
    

    {
        "addition": {
            "additional_info": "Иные сведения",
            "additional_number": 356
        },
        "important_numbers": [
            4,
            8,
            1
        ],
        "title": "Измененная сущность в Python",
        "verified": False
    }

2. Получить статус код ответа 204 No Content
3. Проверить наличие внесенных изменений для сущности id = X в системе запросом GET by id

**Ожидаемый результат**

* Статус код: 204 No Content
* Данные сущности изменены в системе

---

### TC05 - Удаление сущности и её дополнений DELETE

**Метод**: DELETE /api/delete/{id}

**Предусловие**: В системе существует сущность с id = Y

**Шаги**

1. Отправить DELETE-запрос с id = Y
2. Получить статус код ответа 204 No Content
3. Проверить удаление сущности в системе запросом GET by id

**Ожидаемый результат**

* Статус код: 204 No Content
* Сущность удалена из системы -> 500 Internal Server Error (особенность работы данного API)

---


## Allure Report
