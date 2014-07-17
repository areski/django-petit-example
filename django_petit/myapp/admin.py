from django.contrib import admin
from myapp.models import Poll, Choice

admin.site.register(Poll)
admin.site.register(Choice)
