from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='fish_photoes')

    def __str__(self):
        return self.photo.name