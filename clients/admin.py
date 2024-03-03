from django.contrib import admin
from .models import Client, Address
# Register your models here.


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class ClientAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('first_name', 'last_name', 'email', 'phone', 'type_clients', 'title_social', 'created_at')
    list_filter = ('type_clients', 'title_social', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'type_clients', 'title_social')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('client', 'company', 'address_1', 'address_2', 'zip_code', 'city', 'country', 'created_at')
    list_filter = ('city', 'country', 'created_at', 'updated_at')
    search_fields = ('client', 'company', 'address_1', 'address_2', 'zip_code', 'city', 'country')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Address, AddressAdmin)
