from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from. models import Cocktail,MockTail,Shooter
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"
      
    
class CocktailMenu(TemplateView):
    template_name= 'cocktail_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cocktails"] = Cocktail.objects.all()
        return context

class MocktailMenu(TemplateView):
    template_name= 'mocktail_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mocktails"] = MockTail.objects.all()
        return context

class ShooterMenu(TemplateView):
    template_name= 'shooter_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shooters"] = Shooter.objects.all()
        return context
