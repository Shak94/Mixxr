from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from. models import Cocktail,MockTail,Shooter
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"
      
    
class CocktailMenu(TemplateView):
    template_name= 'cocktail_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cocktails"] = Cocktail.objects.all()
        return context
class CocktailCreate(CreateView):
    model=Cocktail
    fields =['name', 'img','info',]
    template_name = "cocktail_create.html"
    def get_success_url(self):
        return reverse ('cocktail_detail', kwargs ={'pk':self.object.pk})

class CocktailDetail(DetailView):
    model= Cocktail
    template_name ='cocktail_detail.html'

class CocktailUpdate(UpdateView):
     model=Cocktail
     fields =['name', 'img','info',]
     template_name = "cocktail_update.html"
     def get_success_url(self):
        return reverse ('cocktail_detail', kwargs ={'pk':self.object.pk})
     
class CocktailDelete(DeleteView):
     model=Cocktail
     fields =['name', 'img','info',]
     template_name = "cocktail_delete.html"
     def get_success_url(self):
        return reverse('cocktail_list')

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
