from django import forms
from .models import Service, Invoice


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'type_service', 'car', 'price', 'description']

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'client', 'services', 'start_city', 'end_city', 'date_start', 'time_start',
                  'date_end', 'time_end', 'duration', 'description']

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})