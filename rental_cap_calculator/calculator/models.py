from django.db import models

# Create your models here.


class ImmobilienScout(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
