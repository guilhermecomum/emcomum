from django.contrib import admin
from django.utils.timezone import now
from emcomum.core.models import Meeting

class MeetingModelAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'guest1_name', 'guest2_name')
    date_hierarchy = 'created_at'

admin.site.register(Meeting, MeetingModelAdmin)
