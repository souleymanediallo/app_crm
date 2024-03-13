from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Service, Invoice
from .forms import ServiceForm, InvoiceForm
# Create your views here.


class ServiceListView(ListView):
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/service_detail.html"
    context_object_name = "service"

    def get_object(self):
        uuid = self.kwargs.get("pk") # pk is the name of the url parameter
        return get_object_or_404(Service, uuid=uuid)


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


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "services/invoice_detail.html"
    context_object_name = "invoice"
    # slug_field = "uuid"
    # slug_url_kwarg = "uuid"

    def get_object(self):
        uuid = self.kwargs.get("pk") # pk is the name of the url parameter
        return get_object_or_404(Invoice, uuid=uuid)


class InvoiceCreateView(CreateView):
    form_class = InvoiceForm
    template_name = "services/invoice_form.html"
    context_object_name = "form"
    print(context_object_name)
    success_url = "/services/invoices"


class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = "__all__"
    template_name = "services/invoice_form.html"
    success_url = "/invoices"


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = "services/invoice_confirm_delete.html"
    success_url = "/invoices"
