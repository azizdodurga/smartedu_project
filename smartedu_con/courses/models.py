from pickle import TRUE
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50, null=True)
    slug=models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name=models.CharField(max_length=200, unique=True, verbose_name="Kurs Adı", help_text="Kurs adını yazınız")
    category=models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to="courses/%y/%m/%d")
    date=models.DateField(auto_now=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name