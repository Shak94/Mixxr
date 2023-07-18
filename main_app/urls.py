from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('cocktail/',views.CocktailMenu.as_view(), name="cocktail_menu"),
  path('cocktail/new/', views.CocktailCreate.as_view(), name ="cocktail_create"),
  path('cocktail/<int:pk>/', views.CocktailDetail.as_view(), name='cocktail_detail'),
  path('cocktail/<int:pk>/update/',views.CocktailUpdate.as_view(), name ="cocktail_update"),
  path('cocktail/<int:pk>/delete/',views.CocktailDelete.as_view(), name ="cocktail_delete"),
  path('mocktail/',views.MocktailMenu.as_view(), name="cocktail_menu"),
  path('shooter/',views.ShooterMenu.as_view(), name="cocktail_menu"),

 
]