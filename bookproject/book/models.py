from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20, null=True)
    author = models.CharField(max_length=20)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=10, null=True)
    pdf = models.FileField(upload_to='books/pdf')
    cover = models.ImageField(upload_to='books/cover')


    def __str__(self):
        return self.title







