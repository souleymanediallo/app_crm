from django.contrib import admin
from .models import Service, Invoice
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "type_service",
        "car",
        "price",
        "created_at",
    ]
    search_fields = [
        "type_service",
        "price",
        "created_at",
    ]
    list_filter = [
        "type_service",
        "price",
        "created_at",
    ]


admin.site.register(Service, ServiceAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "uuid",
        "name",
        "client",
        "start_city",
        "end_city",
        "date_start",
        "time_start",
        "date_end",
        "time_end",
        "duration",
    ]
    search_fields = [
        "client",
        "start_city",
        "end_city",
        "date_start",
        "time_start",
        "date_end",
        "time_end",
        "duration",
    ]
    list_filter = [
        "client",
        "start_city",
        "end_city",
        "date_start",
        "time_start",
        "date_end",
        "time_end",
        "duration",
    ]

    def get_total_price(self, obj):
        return sum([service.price for service in obj.services.all()])

    def get_total_duration(self, obj):
        return sum([service.duration for service in obj.services.all()])

    get_total_price.short_description = "Total Price"
    get_total_duration.short_description = "Total Duration"
    readonly_fields = ["get_total_price", "get_total_duration"]
    fields = ["name", "client", "services", "start_city", "end_city", "date_start", "time_start", "date_end", "time_end", "duration", "description", "get_total_price", "get_total_duration"]


admin.site.register(Invoice, InvoiceAdmin)
# TODO : CRUD for services and invoices
# TODO : Add a filter for the services and invoices
# TODO : Add a search bar for the services and invoices
# TODO : Add a pagination for the services and invoices