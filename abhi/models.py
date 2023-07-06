from django.db import models


# Create your models here.
class BlogContent(models.Model):
    title =models.CharField(max_length=250)
    description= models.CharField(max_length =100)
    author=models.CharField(max_length=100)
    no_of_lines = models.IntegerField()

    def __str__(self):
        return self.title