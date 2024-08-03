from django.contrib import admin

# Register your models here.
from .models import Category,Student



admin.site.register(Category)
admin.site.register(Student)