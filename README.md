[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=FastAPI)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/-MongoDB-464646?style=flat-square&logo=MongoDB)](https://www.mongodb.com/)

## Проект

Небольшое API для магазина, позволяет создать товар и получить список товаров.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/A-A-Tyurin/simple_shop
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:

```
python3 app/main.py
```

## MongoDB 

В качестве СУБД проект использует MongoDB.
1. Сервер MongoDB может быть установлен локально, следуя инструкции
https://docs.mongodb.com/manual/installation/
2. Или через Docker
```
docker pull mongo
```
```
docker run -d -p 27017:27017 mongo
```
** для процессоров, не поддерживающих AVX необходимо использовать версию не выше 4.4

## cURL

Создание нового товаров:
```
curl -H "Content-Type: application/json" http://localhost:5000/product/ -d "{\"name\":\"product_1\",\"description\":\"description_1\"}"
```
```
curl -H "Content-Type: application/json" http://localhost:5000/product/ -d "{\"name\":\"product_2\",\"description\":\"description_2\",\"params\":{\"param_1\":\"some_param\"}}" 
```

Получение списка товаров:
```
curl http://localhost:5000/product/
```

Получение списка товаров c фильтром:
```
curl "http://localhost:5000/product/?name=product_1&param_1=some_param"
```

Получение товара:
```
curl http://localhost:5000/product/{product_id}/
```
** где {product_id} - идентификатор ранее созданного товара
