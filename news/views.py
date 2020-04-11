from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import News

# Create your views here.


def news_detail(request, word):
    news = News.objects.filter(name=word)

    return render(request, 'front/news-details.html', {'news': news})


