from django.contrib import admin
from .models import Responsavel

# Register your models here.

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato')

