from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100000)

class Game(models.Model):  
    name = models.TextField(),
    description = models.TextField(),
    image = models.TextField(),
    category = models.ForeignKey(Category, on_delete=Category, blank=True, null=True),
    price = models.FloatField(),
    screenshots = models.TextField(),
    text = models.TextField()

