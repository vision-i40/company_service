from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _

from .models import Group

class CustomGroupAdmin(GroupAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('name',)

    filter_horizontal = (
        ('permissions'), ('users'),
    )
    fieldsets = (
        (None, {'fields': ('name', 'permissions', 'users',)}),
    )
    add_fieldsets = (
        None, {'fields': ('name',)}
    )

admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Permission)
