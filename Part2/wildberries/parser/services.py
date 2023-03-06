import asyncio
import aiohttp
import json
import openpyxl
from asgiref.sync import sync_to_async
from .models import Products
from pydantic import BaseModel


class Product(BaseModel):
    article: int
    brand: str
    title: str

    def __init__(self, **kwargs):
        kwargs['article'] = kwargs['data']['products'][0]['id']
        kwargs['brand'] = kwargs['data']['products'][0]['brand']
        kwargs['title'] = kwargs['data']['products'][0]['brand'] + ' / ' + kwargs['data']['products'][0]['name']
        super().__init__(**kwargs)


@sync_to_async()
def add_to_database(product):
    """Функция для записи данных в БД"""
    Products.objects.create(article=product.article, brand=product.brand, title=product.title)


async def get_data(article):
    """Функция делает http запрос, создает объект PyDantic и возвращает данные об артикле, бренде и наименовании
       в формате json"""
    url = f'https://card.wb.ru/cards/detail?nm={article}'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            response = await resp.text()
            temp = json.loads(response)
            product = Product.parse_obj(temp)
            await add_to_database(product)
            return product.json(ensure_ascii=False)


async def get_data_from_xlsx(request):
    """Функция парсит артикулы из переданного файла формата xlsx, и возвращает список с информацией по каждому
       артикулу"""
    excel_file = request.FILES['excel_file']
    data = openpyxl.load_workbook(excel_file)
    worksheet = data.active
    tasks = list()
    for row in worksheet.values:
        for cell in row:
            task = asyncio.create_task(get_data(cell))
            tasks.append(task)
    total = await asyncio.gather(*tasks)
    return total
