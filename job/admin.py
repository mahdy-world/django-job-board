from django.contrib import admin

#imports models app 
from .models import job,Category,Apply

# Register your models here.

admin.site.register(job)
admin.site.register(Category)
admin.site.register(Apply)


