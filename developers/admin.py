from django.contrib import admin
from .models import Developer, Framework, Language

# Register your models here.
admin.site.register(Developer)
admin.site.register(Framework)
admin.site.register(Language)