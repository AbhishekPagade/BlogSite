from django.db import models


# Create your models here.
class BlogContent(models.Model):
    title =models.CharField(max_length=250)
    description= models.CharField(max_length =100)
    author=models.CharField(max_length=100)
    no_of_lines = models.IntegerField()
    image=models.ImageField(upload_to='images/',default='images/default_blog.png')

    def __str__(self):
        return self.title