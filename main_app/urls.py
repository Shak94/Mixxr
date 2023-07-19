from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('cocktail/',views.CocktailMenu.as_view(), name="cocktail_menu"),
  path('cocktail/new/', views.CocktailCreate.as_view(), name ="cocktail_create"),
  path('cocktail/<int:pk>/', views.CocktailDetail.as_view(), name='cocktail_detail'),
  path('cocktail/<int:pk>/update/',views.CocktailUpdate.as_view(), name ="cocktail_update"),
  path('cocktail/<int:pk>/delete/',views.CocktailDelete.as_view(), name ="cocktail_delete"),
  path('mocktail/',views.MocktailMenu.as_view(), name="mocktail_menu"),
  path('mocktail/new/', views.MocktailCreate.as_view(), name ="mocktail_create"),
  path('mocktail/<int:pk>/', views.MocktailDetail.as_view(), name='mocktail_detail'),
  path('mocktail/<int:pk>/update/',views.MocktailUpdate.as_view(), name ="mocktail_update"),
  path('mocktail/<int:pk>/delete/',views.MocktailDelete.as_view(), name ="mocktail_delete"),
  path('shooter/',views.ShooterMenu.as_view(), name="shooter_menu"),
  path('shooter/new/', views.ShooterCreate.as_view(), name ="shooter_create"),
  path('shooter/<int:pk>/', views.ShooterDetail.as_view(), name='shooter_detail'),
  path('shooter/<int:pk>/update/',views.ShooterUpdate.as_view(), name ="shooter_update"),
  path('shooter/<int:pk>/delete/',views.ShooterDelete.as_view(), name ="shooter_delete"),

 
]