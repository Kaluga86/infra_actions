from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Добавим инфы для проверки1111')


def second_page(request):
    return HttpResponse('А это вторая страница!')
