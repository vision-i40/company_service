from django.contrib import admin
from .models import Company
from users.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.views.main import ChangeList

class CustomCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'modified')
    list_filter = ('is_active', 'name')
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('name', 'slug')}),
        (_('Permissions'), {'fields': ('is_active', 'users',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'slug', 'is_active')}),
    )

admin.site.register(Company, CustomCompanyAdmin)
