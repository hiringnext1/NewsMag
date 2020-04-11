from django.shortcuts import render, get_object_or_404
from .models import Main
from  news.models import News

# Create your views here.


def home(request):
    sitename = "MagNews"
    news = News.objects.all()

    return render(request, 'front/index.html', {'sitename': sitename, 'news': news})


def about(request):
    return render(request, 'front/about.html')


def panel(request):

    return render(request, 'back/admin_index.html')