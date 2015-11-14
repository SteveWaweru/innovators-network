from django.contrib import admin
from .models import Mail


class MailAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp']


admin.site.register(Mail, MailAdmin)
