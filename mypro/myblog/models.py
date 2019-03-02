from django.db import models


class Management(models.Manager):
    def regulate(self, name, password):
        self.create(name=name, password=password)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    # man = Management()

    @classmethod
    def reg(cls, name, password):
        um = cls(name=name, password=password)
        return um


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    coutext = models.TextField()
    author = models.TextField(User)

    @classmethod
    def text(cls, title, coutext):
        T = cls(title=title, coutext=coutext)
        return T

# Create your models here.
