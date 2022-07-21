from django.db import models

# Create your models here.

class Instructor(models.Model):
    name        = models.CharField(max_length=30)
    email       = models.EmailField()

    def __str__(self):
        return self.email

class Subject(models.Model):
    title        = models.CharField(max_length=50)
    rating       = models.IntegerField()
    instructor   = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="subject")

    def __str__(self):
        return self.title

class Course(models.Model):
    name        = models.CharField(max_length=30)
    author      = models.CharField(max_length=40)
    price       = models.IntegerField()
    discount    = models.IntegerField(default=0)
    duration    = models.FloatField()

    def __str__(self):
        return self.name