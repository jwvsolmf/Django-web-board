from django.contrib import admin

# Register your models here.

from .models import Bd, Rubric

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'rubric', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)
