from django.db import models

# Create your models here.

class Experience(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    date =models.CharField(max_length=100 , default='2026-Present')

    def __str__(self):
        return self.title