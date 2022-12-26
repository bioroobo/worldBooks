"""worldBooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views
from django.conf.urls import url  #Django 3.2
#from django.template.defaulttags import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'), # http://127.0.0.1:8000/books/
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'), # http://127.0.0.1:8000/books/1
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'), # http://127.0.0.1:8000/authors/
]
