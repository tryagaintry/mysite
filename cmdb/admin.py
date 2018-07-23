from django.contrib import admin

# Register your models here.


from . import models

admin.site.register(models.user_info)

admin.site.register(models.server_info)