from django.contrib import admin
from cruds.models import detail

class details(admin.ModelAdmin):
    data = ('name', 'branch', 'section', 'year', 'dob', 'email_id', 'password')

admin.site.register(detail, details)
