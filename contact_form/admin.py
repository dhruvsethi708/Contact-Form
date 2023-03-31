from django.contrib import admin

# Register your models here.
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)