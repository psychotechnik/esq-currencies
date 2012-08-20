from django.contrib import admin
from core.models import Attachment

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Attachment, AttachmentAdmin)
