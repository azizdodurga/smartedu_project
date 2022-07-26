# Generated by Django 4.0.1 on 2022-07-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs adını yazınız', max_length=200, unique=True, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='courses/%y/%m/&d')),
                ('date', models.DateField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
