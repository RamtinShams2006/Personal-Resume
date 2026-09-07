from django.db import models


class Education(models.Model):
    univ = models.CharField()
    certificate = models.TextField()
    major = models.TextField()
    score = models.CharField()
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.univ