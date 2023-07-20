from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('<int:pk>/', views.forum_detail, name='forum_detail'),
    path('category/<str:category>/', views.forum_category, name='forum_category'),
    path('search/', views.search_results, name='search_results')
]