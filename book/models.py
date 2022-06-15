from django.db import models
from user.models import CustomUser


class Book(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Book",null=True,blank=True)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True,blank=True)
    janr = models.ManyToManyField('Janr')
    published = models.CharField(max_length=4,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Janr(models.Model):
    janr = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Blog',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title[:20]

class Author(models.Model):
    fullname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Author',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=50,null=True, blank=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.fullname[:20]

class Readers(models.Model):
    status = (
        ('Read','Read'),
        ('Reading','Reading'),
        ('I am going to read','I am going to read'),
    )

    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20,choices=status)