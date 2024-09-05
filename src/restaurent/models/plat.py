from django.db import models

class Plat(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.name