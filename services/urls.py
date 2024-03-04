from django.urls import path
from . import views

urlpatterns = [
    # Services
    path("", views.ServiceListView.as_view(), name="service_list"),
    path("<int:pk>/", views.ServiceDetailView.as_view(), name="service_detail"),
    path("create/", views.ServiceCreateView.as_view(), name="service_create"),
    path("<int:pk>/update/", views.ServiceUpdateView.as_view(), name="service_update"),
    path("<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="service_delete"),
    # Invoices
    path("invoices/", views.InvoiceListView.as_view(), name="invoice_list"),
    path("invoices/<int:pk>/", views.InvoiceDetailView.as_view(), name="invoice_detail"),
    path("invoices/create/", views.InvoiceCreateView.as_view(), name="invoice_create"),
    path("invoices/<int:pk>/update/", views.InvoiceUpdateView.as_view(), name="invoice_update"),
    path("invoices/<int:pk>/delete/", views.InvoiceDeleteView.as_view(), name="invoice_delete"),
]