from django.contrib import admin

from sistema.models import Users, Documents


# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display=("name","last_name","rut","dv","mail")
    search_fields=("name", "last_name","rut","mail")

class UsersDocument(admin.ModelAdmin):
    list_display=("title","author","description","publication_date","url")
    search_fields=("url","description","title","author","publication_date")


admin.site.register(Users, UsersAdmin)
admin.site.register(Documents, UsersDocument)
