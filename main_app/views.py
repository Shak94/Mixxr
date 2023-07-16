from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from. models import Drink
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"
      
    
class CocktailMenu(TemplateView):
    template_name= 'cocktail_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cocktails"] = Drink.objects.all()
        return context

class MocktailMenu(TemplateView):
    template_name= 'mocktail_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mocktails"] = Drink.objects.all()
        return context

class ShooterMenu(TemplateView):
    template_name= 'shooter_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shooters"] = Drink.objects.all()
        return context
