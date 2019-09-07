from django.contrib import admin
from . import models
from users.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.views.main import ChangeList


class CustomCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade_name', 'slug', 'cnpj', 'industrial_sector', 'size', 'created', 'modified')
    list_filter = ('is_active', 'trade_name')
    search_fields = ('trade_name',)
    ordering = ('trade_name',)

    fieldsets = (
        (None, {'fields': ('trade_name', 'slug', 'corporate_name', 'cnpj', 'email',
                           'phone', 'address', 'zip_code', 'neighborhood', 'city', 'state',
                           'country', 'industrial_sector', 'size')}),
        (_('Permissions'), {'fields': ('is_active', 'users',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('trade_name', 'slug', 'corporate_name', 'cnpj', 'email',
                       'phone', 'address', 'zip_code', 'neighborhood', 'city', 'state',
                       'country', 'industrial_sector', 'size', 'is_active')}),
    )


class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    list_filter = ('name', 'company')
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('name', 'company',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company')}),
    )


class CustomUnitOfMeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'is_default', 'conversion_factor',)
    list_filter = ('name', 'product', 'is_default',)
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('name', 'product', 'is_default', 'conversion_factor',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'product', 'is_default', 'conversion_factor',)}),
    )


class CustomTurnSchemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('name', 'company',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company'),}),
    )

class CustomTurnAdmin(admin.ModelAdmin):
    list_display = ('id', 'turn_scheme', 'name', 'start_time', 'end_time', 'days_of_week',)
    list_filter = ('name', 'turn_scheme',)
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('turn_scheme', 'name', 'start_time', 'end_time', 'days_of_week',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'turn_scheme', 'name', 'start_time', 'end_time', 'days_of_week',)}),
    )


admin.site.register(models.Company, CustomCompanyAdmin)
admin.site.register(models.Product, CustomProductAdmin)
admin.site.register(models.UnitOfMeasurement, CustomUnitOfMeasurementAdmin)
admin.site.register(models.TurnScheme, CustomTurnSchemeAdmin)
admin.site.register(models.Turn, CustomTurnAdmin)
