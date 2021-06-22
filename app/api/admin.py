from django.contrib import admin
from app.api.models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    #solo lectura
    readonly_fields = ('votes',)
    #para que se vea en la movida del añadir del admin
    list_display = ['title', 'url']
