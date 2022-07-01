from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=e2b88956dc67458fba2f0fdf463ecfe3")
    jsonResponse = response.json()
    articles = jsonResponse['articles']
    return render(request, 'blog/index.html', {'articles': articles})

def singleArticle(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.POST.get('image')
    return render(request, 'blog/single_article.html', {'title': title, 'content': content, 'image': image})

def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')