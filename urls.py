from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='home-page'),
    path('home/', views.home, name='home-page'),
    path('home/alice/', views.alice, name='customer-page')


]