from django.contrib import admin
from .models import Company
from users.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.views.main import ChangeList

class CustomCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade_name', 'slug', 'cnpj', 'industrial_sector', 'size', 'created', 'modified')
    list_filter = ('is_active', 'trade_name')
    search_fields = ('trade_name',)
    ordering = ('trade_name',)

    fieldsets = (
        (None, {'fields': ('trade_name', 'slug', 'corporate_name', 'cnpj','email',
                            'phone', 'address', 'zip_code', 'neighborhood', 'city', 'state',
                            'country', 'industrial_sector', 'size')}),
        (_('Permissions'), {'fields': ('is_active', 'users',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('trade_name', 'slug', 'corporate_name', 'cnpj','email',
                        'phone', 'address', 'zip_code', 'neighborhood', 'city', 'state',
                        'country', 'industrial_sector', 'size', 'is_active')}),
    )

admin.site.register(Company, CustomCompanyAdmin)
