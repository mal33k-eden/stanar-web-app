from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Provider
# Register your models here.

class ProviderAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name','last_name','username','is_active','last_login')
    list_filter = ()
    fieldsets = ()
    filter_horizontal = ()
admin.site.register(Provider,ProviderAdmin)