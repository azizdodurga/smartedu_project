from django.db import models

# Create your models here.

class Courses(models.Model):
    name=models.CharField(max_length=200, unique=True, verbose_name="Kurs Adı", help_text="Kurs adını yazınız")
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to="courses/%y/%m/&d")
    date=models.DateField(auto_now=True)
    available=models.BooleanField(default=True)
