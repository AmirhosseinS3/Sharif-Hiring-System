from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.sessions.models import Session
from hiring.models import Employee, Employer


class SessionAdmin(ModelAdmin):

    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Session, SessionAdmin)
