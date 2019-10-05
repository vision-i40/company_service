from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _

from .models import Group

class CustomGroupAdmin(GroupAdmin):
    list_display = ('name', 'default_company',)
    list_filter = ('name', 'default_company',)
    search_fields = ('name', 'default_company',)
    ordering = ('name',)

    filter_horizontal = (
        ('permissions'), ('users'),
    ) 
    fieldsets = (
        (None, {'fields': ('name', 'permissions', 'default_company', 'users',)}),
    ) 
    add_fieldsets = (
        None, {'fields': ('name', 'default_company',)}
    )

admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Permission)