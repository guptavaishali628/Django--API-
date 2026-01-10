from django.db import models

# Create your models here.

class movie(models.Model):
    name=models.CharField(max_length=40)
    dis=models.TextField(max_length=50)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name    

