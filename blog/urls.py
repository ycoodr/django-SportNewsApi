from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('singleArticle', views.singleArticle, name="singleArticle"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about")
]