from django.contrib import admin

from sistema.models import  Documents


# Register your models here.



class UsersDocument(admin.ModelAdmin):
    list_display=("title","author","description","publication_date","url")
    search_fields=("url","description","title","author","publication_date")



admin.site.register(Documents, UsersDocument)
