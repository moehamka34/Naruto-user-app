from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Jitsu(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name} {self.type}'
    
    def get_absolute_url(self):
        return reverse('jitsus_detail', kwargs={'pk': self.id})

class Ninja(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'ninja_id': self.id})
    
    #ninja = models.ForeignKey(Ninja, on_delete=models.CASCADE)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  ninja = models.ForeignKey(Ninja, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for ninja_id: {self.ninja_id} @{self.url}"
