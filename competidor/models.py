from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class Competidor(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    birthday = models.DateField(null=False, max_length=50)
    avatar = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    hobbies = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    class Meta:
        ordering = ['first_name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['first_name']),
        ]

   
    def __str__(self):
        return f'{self.first_name}'
