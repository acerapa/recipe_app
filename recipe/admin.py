from atexit import register
from django.contrib import admin
from .models import AdminFiles, Recipe, AdminProcedures, AdminBookmarks, AdminComments, MasterFile

# Register your models here.
admin.site.register(Recipe) 
admin.site.register(AdminFiles)
admin.site.register(AdminComments)
admin.site.register(AdminBookmarks)
admin.site.register(AdminProcedures)
