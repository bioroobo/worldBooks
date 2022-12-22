from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги',
                            verbose_name='Жанр книги')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text='Введите язык книги',
                            verbose_name='Язык книги')

    def __str__(self):
        return self.name



class Author(models.Model):

    first_name = models.CharField(max_length=100, help_text='Ведите имя автора',
                                  verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, help_text='Ведите фамилию автора',
                                 verbose_name='Фамилия автора')
    date_of_birth = models.DateField(help_text='Введите дату рождения',
                                     verbose_name='Дата рождения',
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text='Введите дату смерти',
                                     verbose_name='Дата смерти',
                                     null=True, blank=True)
    def __str__(self):
        return self.last_name

# Relationships:
# One  "Genre"    -To- Many "Book"
# One  "Language" -To- Many "Book"
# Many "Author"   -To- Many "Book"
class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Ведите название книги',
                             verbose_name='Название книги')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text='Выберите жанр книги',
                              verbose_name='Жанр книги', null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text='Выберите язык книги',
                                 verbose_name='Язык книги', null=True)
    author = models.ManyToManyField('Author', # null=True, <--  null has no effect on ManyToManyField
                              help_text='Выберите автора книги',
                              verbose_name='Автора книги')
    summary = models.TextField(max_length=1000, verbose_name='Аннотация книги',
                               help_text='Введите краткое описание книги')
    isbn = models.CharField(max_length=13, verbose_name='ISBN книги',
                            help_text='Должно содержать 13 символов')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает URL-адрес для доступа к определенному экземпляру книги
        return reverse('book-detail', args=[str(self.id)])



# Relationship:    Many "Book"  - "BookInstance" - Many "Status"
class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Статус экземпляра книги',
                            help_text='Введите статус экземпляра книги')
    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               verbose_name='Инвентарный номер',
                               help_text='Введите инвентарный номер экземпляра')
    imprint = models.CharField(max_length=200, verbose_name='Издательство',
                               help_text='Введите издательство и год выпуска')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True,
                               verbose_name='Статус экземпляра книги',
                               help_text='Изменить состояние экземпляра')
    due_back = models.DateField(null=True, blank=True,
                                verbose_name='Дата окончания статуса',
                                help_text='Введите конец срока статуса')
    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
