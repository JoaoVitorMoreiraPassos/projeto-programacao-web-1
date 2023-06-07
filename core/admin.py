from django.contrib import admin
from .models import Profile, Category, Notice, Comment, Recipe, Ingredient

# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Notice)
admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Ingredient)
