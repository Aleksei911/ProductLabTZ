from django.shortcuts import render
from .forms import SearchForm, UpdateExcel
from .services import get_data, get_data_from_xlsx
from .models import Products


def search_story(request):
    """Функция для отображения истории запросов (из БД)"""
    products = Products.objects.all().order_by('-pk')
    return render(request, 'parser/main.html', {'products': products})


async def search_product(request):
    """Функция для обработки запроса по одному артикулу"""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = await get_data(form.cleaned_data['article'])
            return render(request, 'parser/one_product.html', {'form': form, 'data': data})
    else:
        form = SearchForm()

    return render(request, 'parser/one_product.html', {'form': form})


async def search_products_from_xlsx(request):
    """Функция для обработки запроса с переданным файлом формала xlsx"""
    if request.method == 'POST':
        form = UpdateExcel(request.POST, request.FILES)
        if form.is_valid():
            total = await get_data_from_xlsx(request)
            return render(request, 'parser/excel.html', {'form': form, 'total': total})
    else:
        form = UpdateExcel()
    return render(request, 'parser/excel.html', {'form': form})
