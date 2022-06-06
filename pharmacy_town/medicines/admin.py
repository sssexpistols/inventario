from atexit import register
from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Price)
admin.site.register(Provider)
admin.site.register(Provider_medicine)