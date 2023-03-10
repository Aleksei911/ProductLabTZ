## Базовые технологии проекта

- Python 3.11
- Django 4.1.7
- Aiohttp 3.8.4
- Postgres 15
- Psycopg2 2.9.5
- Pydantic 1.10.5
- Openpyxl 3.1.1
- Docker
- Docker-Compose

## Инструкция по развертыванию тестового проекта

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

#### Создание миграций:

```bash
docker-compose run --rm web-app sh -c "python manage.py makemigrations"
```

#### Применение миграций:

```bash
docker-compose run --rm web-app sh -c "python manage.py migrate"
```

#### Создание суперпользователя

```bash
docker-compose run --rm web-app sh -c "python manage.py createsuperuser"
```

#### Внешние порты

- 5432:5432 - БД
- 8000:8000 - API

#### Описание задания

Часть No2

1. Изначально необходимо отследить трафик с www.wildberries.ru и найти HTTP
запрос, который в JSON формате присылает данные о бренде и название
артикула.

2. Далее необходимо реализовать API принимающее файл формата xlsx с
артикулами (артикулы должны вводиться построчно в первой колонке) или
один артикул (не в файле, а исключительно одно значение). В API должно быть
два инпута: файл или одно значение, передаваться должно что-то одно.

3. API должно асинхронно взаимодействовать с найденным HTTP запросом в
первом пункте и получать данные о карточке товара. Из полученных данных
необходимо сделать PyDantic объект.

4. Успешным результатом работы API является возврат данных о бренде и
названии артикула в JSON формате. Пример: информация об одном артикуле -
{"article": 123, "brand": "brand", "title": "Title"}; артикулы из файла - [{"article": 1,
"brand": "Brand1", "title": "Title1"}, {"article": 2, "brand": "Brand2", "title": "Title2"}]
