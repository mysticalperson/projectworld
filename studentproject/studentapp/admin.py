from django.contrib import admin

# Register your models here.
from .models import places
admin.site.register(places)
from.models import member
admin.site.register(member)