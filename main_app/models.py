from django.db import models


class Cocktail(models.Model):
    name=models.CharField(max_length=50)
    image=models.CharField(max_length=250)
    description=models.TextField(max_length=600)
    recipe=models.TextField(max_length=700)
    created_at=models.DateTimeField(auto_now_add=True)

class MockTail(models.Model):
    name=models.CharField(max_length=50)
    image=models.CharField(max_length=250)
    description=models.TextField(max_length=600)
    recipe=models.TextField(max_length=700)
    created_at=models.DateTimeField(auto_now_add=True)

class Shooter(models.Model):
    name=models.CharField(max_length=50)
    image=models.CharField(max_length=250)
    description=models.TextField(max_length=600)
    recipe=models.TextField(max_length=700)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
# Create your models here.
