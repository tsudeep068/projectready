from django.contrib import admin
from .models import Task, Category, Comment

# Register your models here.

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Comment)
