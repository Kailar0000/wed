from django.shortcuts import render
from .models import News

def start_page(request):
    new_news = News.objects.order_by("-id")[:10]
    return render(request, 'news/news_page.html', {'new_news': new_news})

