from django.db import models

class Drink(models.Model):
    image=models.CharField(max_length=250)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=700)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['image']
    
# Create your models here.
