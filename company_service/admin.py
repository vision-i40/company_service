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


class CustomProductionLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name',)
    list_filter = ('name', 'company',)
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('company', 'name', 'is_active', 'discount_rework', 'discount_waste', 'stop_on_production_absence', 'time_to_consider_absence', 'reset_production_changing_order', 'micro_stop_seconds', 'turn_scheme',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company', 'name', 'is_active', 'discount_rework', 'discount_waste', 'stop_on_production_absence', 'time_to_consider_absence', 'reset_production_changing_order', 'micro_stop_seconds', 'turn_scheme',)}),
    )


class CustomCodeGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name', 'group_type',)
    list_filter = ('name', 'company',)
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('company', 'name', 'group_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company', 'name', 'group_type',)}),
    )


class CustomStopCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name', 'is_planned', 'code_group',)
    list_filter = ('name', 'company', 'is_planned', )
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('company', 'name', 'code_group', 'is_planned', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company', 'name', 'code_group', 'is_planned', )}),
    )


class CustomWasteCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name', 'code_group',)
    list_filter = ('name', 'company', )
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('company', 'name', 'code_group', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company', 'name', 'code_group', )}),
    )


class CustomReworkCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name', 'code_group',)
    list_filter = ('name', 'company', )
    search_fields = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('company', 'name', 'code_group', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company', 'code_group', )}),
    )

class CustomProductionOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'production_line', 'code', 'quantity', 'state')
    list_filter = ('production_line', 'product', )
    search_fields = ('production_line',)
    ordering = ('production_line',)

    fieldsets = (
        (None, {'fields': ('product', 'production_line', 'code', 'quantity', 'state', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('production_line', 'product', 'code', 'quantity', 'state', )}),
    )

class CustomProductionEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'product', 'production_line', 'production_order', 'quantity', 'event_type',)
    list_filter = ('production_line', 'product', )
    search_fields = ('production_line',)
    ordering = ('production_line',)

    fieldsets = (
        (None, {'fields': ('company', 'product', 'production_line', 'production_order', 'quantity', 'event_type', 'event_datetime', 'waste_code', 'rework_code', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company', 'product', 'production_line', 'production_order', 'quantity', 'event_type', 'event_datetime', 'waste_code', 'rework_code', )}),
    )

class CustomCollectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'collector_type', 'mac')
    list_filter = ('collector_type', 'mac',)
    search_fields = ('collector_type',)
    ordering = ('collector_type',)

    fieldsets = (
        (None, {'fields': ('company', 'collector_type', 'mac',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('company', 'collector_type', 'mac',)}),
    )

class CustomChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'collector', 'production_line', 'number', 'channel_type', 'inverse_state', 'is_cumulative')
    list_filter = ('production_line', 'channel_type', 'collector',)
    search_fields = ('channel_type', 'number',)
    ordering = ('channel_type',)

    fieldsets = (
        (None, {'fields': ('collector', 'production_line', 'number', 'channel_type', 'inverse_state', 'is_cumulative')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('collector', 'production_line', 'channel_type', 'number', 'inverse_state', 'is_cumulative')}),
    )

class CustomStateEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_order', 'production_line', 'channel', 'event_datetime', 'state')
    list_filter = ('production_order', 'production_line', 'channel', 'event_datetime', 'state',)
    search_fields = ('production_order', 'production_line', 'channel', 'event_datetime',)
    ordering = ('event_datetime',)

    fieldsets = (
        (None, {'fields': ('production_order', 'production_line', 'channel', 'event_datetime', 'state')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('production_order', 'production_line', 'channel', 'event_datetime', 'state')
        })
    )

class CustomManualStopAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_line', 'start_datetime', 'end_datetime',)
    list_filter = ('production_line', 'start_datetime', 'end_datetime',)
    search_fields = ('production_line', 'start_datetime', 'end_datetime',)
    ordering = ('start_datetime',)

    fieldsets = (
        (None, {'fields': ('production_line', 'start_datetime', 'end_datetime',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('production_line', 'start_datetime', 'end_datetime',)
        })
    )

admin.site.register(models.Company, CustomCompanyAdmin)
admin.site.register(models.Product, CustomProductAdmin)
admin.site.register(models.UnitOfMeasurement, CustomUnitOfMeasurementAdmin)
admin.site.register(models.TurnScheme, CustomTurnSchemeAdmin)
admin.site.register(models.Turn, CustomTurnAdmin)
admin.site.register(models.ProductionLine, CustomProductionLineAdmin)
admin.site.register(models.CodeGroup, CustomCodeGroupAdmin)
admin.site.register(models.StopCode, CustomStopCodeAdmin)
admin.site.register(models.ReworkCode, CustomReworkCodeAdmin)
admin.site.register(models.WasteCode, CustomWasteCodeAdmin)
admin.site.register(models.ProductionOrder, CustomProductionOrderAdmin)
admin.site.register(models.ProductionEvent, CustomProductionEventAdmin)
admin.site.register(models.Collector, CustomCollectorAdmin)
admin.site.register(models.Channel, CustomChannelAdmin)
admin.site.register(models.StateEvent, CustomStateEventAdmin)
admin.site.register(models.ManualStop, CustomManualStopAdmin)