from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.sessions.models import Session
from hiring.models import Employee, Employer, Announcement, Resume, Comment, EmployeeComment, EmployerComment


class SessionAdmin(ModelAdmin):

    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Employee)
admin.site.register(Announcement)
admin.site.register(Session, SessionAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Comment)
admin.site.register(EmployeeComment)
admin.site.register(EmployerComment)
admin.site.register(Resume)
