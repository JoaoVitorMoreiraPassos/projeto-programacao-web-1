from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    image_pattern = models.ImageField("/category/", blank=True, null=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="notice/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10]


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="recipe/", blank=True, null=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    recipe = models.ManyToManyField(Recipe, related_name="ingredients")

    def __str__(self):
        return self.name
