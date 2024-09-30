from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('authors/', views.authors_list, name='authors_list'),
    path('authors/<int:author_id>/news/', views.author_news, name='author_news'),
]