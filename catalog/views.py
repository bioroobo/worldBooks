from django.http import HttpResponse
from django.shortcuts import render
from . models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    # Генерация "количуств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус = "На складе"). Здесь метод all() применен по умолчанию
    num_instanses_available = BookInstance.objects.filter(status__exact=2).count()

    # Авторы книг
    num_authors = Author.objects.count()

    # Отрисовка HTML-шаблона index.html с данными внутри переменной context
    return render(request, 'index.html',
                  context={
                      'num_books':num_books,
                      'num_instances':num_instances,
                      'num_instanses_available':num_instanses_available,
                      'num_authors':num_authors,
                      #'num_visits':num_visits,
    })


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    """
    Обобщенное представление выполнит запрос к базе данных,
    получит все записи заданной модели (вооk), а затем заполнит соответствующий
    шаблон для выдачи списка книг ( файл book_list.html), который будет располагаться
    в каталоге ..../WebBooks/templates/catalog/.
    Внутри этого шаблона можно будет получить доступ к списку книг при помощи
    переменной шаблона object_list (в нашем случае- book_list, поскольку имя этой
    переменной формируется по шаблону: model_name_list).
    ПРИМЕЧАНИЕ
    На первый взгляд приведенный у нас путь к файлу шаблона: ..../WebBooks/templates
    /catalog/book_list.html Содержит опечатку. Ведь по факту шаблон должен находиться по
    пути: ..../WebBooks/templates/book_list.htm/.
    Однако обобщенное представление ищет файл шаблона по пути: /application_name/the_model_name_list.html
    (в нашем случае: catalog/book_list.html), т. е. внутри каталога приложения
    /application_name/templates/ (в нашем примере это WebBooks/templates/catalog/book_list.html).
    """


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
