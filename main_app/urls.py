from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('cocktail/',views.CocktailMenu.as_view(), name="cocktail_menu"),
  path('mocktail/',views.MocktailMenu.as_view(), name="cocktail_menu"),
  path('shooter/',views.ShooterMenu.as_view(), name="cocktail_menu"),

 
]