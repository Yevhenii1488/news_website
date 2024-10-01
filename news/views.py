from django.shortcuts import render, get_object_or_404
from .models import News, Author

def home(request):
    latest_news = News.objects.order_by('-pub_date')[:10]
    return render(request, 'home.html', {'latest_news': latest_news})

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_news(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_news.html', {'author': author})
