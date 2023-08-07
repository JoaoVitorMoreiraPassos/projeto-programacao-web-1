from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


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
    image_pattern = models.ImageField(upload_to="category/", blank=True, null=True)

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
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Gera o slug apenas se ele não estiver definido
            slug = slugify(self.title)
            unique_slug = slug
            num = 1
            while Notice.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    def __str__(self):
        return self.content[:10]


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="recipe/", blank=True, null=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # ONE INGREDIENT CAN BE IN MANY RECIPES
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name


class RecipeDates(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()
    meal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.recipe} - {self.date} - {self.meal}"
