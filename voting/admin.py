from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Agentname)
admin.site.register(AnnouncedLgaResults)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)
admin.site.register(Lga)
admin.site.register(PollingUnit)
admin.site.register(Ward)

