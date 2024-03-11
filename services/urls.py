from django.urls import path
from . import views

urlpatterns = [
    # Services
    path("", views.ServiceListView.as_view(), name="service_list"),
    path("<uuid:pk>/", views.ServiceDetailView.as_view(), name="service_detail"),
    path("create/", views.ServiceCreateView.as_view(), name="service_create"),
    path("<uuid:pk>/update/", views.ServiceUpdateView.as_view(), name="service_update"),
    path("<uuid:pk>/delete/", views.ServiceDeleteView.as_view(), name="service_delete"),
    # Invoices
    path("invoices/", views.InvoiceListView.as_view(), name="invoice_list"),
    path("invoices/<uuid:pk>/", views.InvoiceDetailView.as_view(), name="invoice_detail"),
    path("invoices/create/", views.InvoiceCreateView.as_view(), name="invoice_create"),
    path("invoices/<uuid:pk>/update/", views.InvoiceUpdateView.as_view(), name="invoice_update"),
    path("invoices/<uuid:pk>/delete/", views.InvoiceDeleteView.as_view(), name="invoice_delete"),
]