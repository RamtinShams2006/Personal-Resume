from django.db import models


class About(models.Model):
    name = models.CharField(max_length=200, default='ramtin')
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    email = models.EmailField()
    description = models.TextField()
    linkdin_link = models.URLField()
    git_link = models.URLField()
    instagram_link = models.URLField()

    def __str__(self):
        return self.name
