from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Service, Invoice
from .forms import ServiceForm, InvoiceForm
# Create your views here.


class ServiceListView(ListView):
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"


class ServiceDetailView(TemplateView):
    model = Service
    template_name = "services/service_detail.html"
    context_object_name = "service"


class ServiceCreateView(CreateView):
    form_class = ServiceForm
    template_name = "services/service_form.html"
    context_object_name = "form"
    success_url = "/services"


class ServiceUpdateView(UpdateView):
    model = Service
    fields = "__all__"
    template_name = "services/service_form.html"
    success_url = "/services"


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = "services/service_confirm_delete.html"
    success_url = "/services"


class InvoiceListView(ListView):
    model = Invoice
    template_name = "services/invoice_list.html"
    context_object_name = "invoices"


class InvoiceDetailView(TemplateView):
    model = Invoice
    template_name = "services/invoice_detail.html"
    context_object_name = "invoice"


class InvoiceCreateView(CreateView):
    form_class = InvoiceForm
    template_name = "services/invoice_form.html"
    context_object_name = "form"
    print(form_class)
    success_url = "/invoices"


class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = "__all__"
    template_name = "services/invoice_form.html"
    success_url = "/invoices"


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = "services/invoice_confirm_delete.html"
    success_url = "/invoices"
