from django.db import models

# Create your models here.



class Teacher(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    subject = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)

    class Meta:
        ordering = ['first_name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['first_name']),
        ]

   
    def __str__(self):
        return f'{self.first_name}'
