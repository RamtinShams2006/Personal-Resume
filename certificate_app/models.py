from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.title