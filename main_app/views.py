from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"
      
    
class CocktailMenu(TemplateView):
    template_name= 'cocktails_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cocktails"] = CocktailMenu.objects.all()
        return context
