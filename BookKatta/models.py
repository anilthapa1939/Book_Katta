from django.db import models
from django.urls import reverse
# Create your models here.
class Pricing(models.Model):
    off = models.IntegerField()
    price =models.IntegerField()
    field = models.CharField(max_length=100)
    sub1 = models.CharField(max_length=100)
    sub2 = models.CharField(max_length=100)
    sub3 = models.CharField(max_length=100)
    sub4 = models.CharField(max_length=100)
    sub5 = models.CharField(max_length=100)

class Items(models.Model):
    img=models.ImageField(upload_to ='pics')
    name =models.CharField(max_length=100)
    desc =models.TextField()
    price =models.IntegerField()


    def get_absolute_url(self):
        return reverse('items')


class Ditems(models.Model):
    img=models.ImageField(upload_to ='pics')
    name =models.CharField(max_length=100)
    desc =models.TextField()
    price =models.IntegerField()


    def get_absolute_url(self):
        return reverse('ditems')

class AgriItems(models.Model):
    img=models.ImageField(upload_to ='pics')
    name =models.CharField(max_length=100)
    desc =models.TextField()
    price =models.IntegerField()


    def get_absolute_url(self):
        return reverse('agriItems')


class ArchItems(models.Model):
    img=models.ImageField(upload_to ='pics')
    name =models.CharField(max_length=100)
    desc =models.TextField()
    price =models.IntegerField()


    def get_absolute_url(self):
        return reverse('archItems')

