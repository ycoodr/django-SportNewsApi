from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=e2b88956dc67458fba2f0fdf463ecfe3")
    jsonResponse = response.json()
    articles = jsonResponse['articles']
    return render(request, 'blog/index.html', {'articles': articles})
