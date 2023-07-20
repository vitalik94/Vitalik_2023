from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.books_index, name='books_index'),
    path('<int:pk>', views.books_detail, name='book_detail')
]