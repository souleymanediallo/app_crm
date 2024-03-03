from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Client, Address
from .forms import ClientForm
# Create your views here.


class ClientListView(ListView):
    model = Client
    template_name = "clients/client_list.html"
    context_object_name = "clients"


class ClientDetailView(TemplateView):
    model = Client
    template_name = "clients/client_detail.html"
    context_object_name = "client"


class ClientCreateView(CreateView):
    form_class = ClientForm
    template_name = "clients/client_form.html"
    context_object_name = "form"
    success_url = "/clients"


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "clients/client_form.html"
    fields = "__all__"
    success_url = "/clients"


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "clients/client_confirm_delete.html"
    success_url = "/clients"


