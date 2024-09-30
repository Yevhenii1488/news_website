from django.shortcuts import render, get_object_or_404
from .models import News, Author

def home(request):
    latest_news = News.objects.order_by('-pub_date')[:10]
    return render(request, 'home.html', {'latest_news': latest_news})

def news_list(request):
    all_news = News.objects.all().order_by('-pub_date')
    return render(request, 'news_list.html', {'all_news': all_news})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_news(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author_news_items = News.objects.filter(author=author).order_by('-pub_date')
    return render(request, 'author_news.html', {'author': author, 'author_news_items': author_news_items})