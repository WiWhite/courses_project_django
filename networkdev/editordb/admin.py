from django.contrib import admin

from .models import *


admin.site.register(Devices)
admin.site.register(ID_connection_type)
admin.site.register(ID_production)
admin.site.register(Crontab)
admin.site.register(Minutes)
admin.site.register(Hours)
admin.site.register(Days)
