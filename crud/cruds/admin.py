from django.contrib import admin
from cruds.models import detail

class details:
    data = ('name', 'branch', 'section', 'year', 'dob', 'email_id', 'password')

admin.site.register(detail, details)
