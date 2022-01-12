from django.contrib import admin
from django.db import models
from .models import Contacts,Article
# Register your models here.

admin.site.register(Contacts)
admin.site.register(Article)
