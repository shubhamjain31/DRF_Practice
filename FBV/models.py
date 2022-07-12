from django.db import models

# Create your models here.

class Employee(models.Model):
    name            = models.CharField(max_length=30)
    email           = models.EmailField()
    password        = models.CharField(max_length=40)
    phone           = models.CharField(max_length=40)

    def __str__(self):
        return self.name