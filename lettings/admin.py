from django.contrib import admin
from lettings.models import Address, Letting

# Register your models here.
admin.site.register(Letting)
admin.site.register(Address)