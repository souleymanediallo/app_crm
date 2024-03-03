from django import forms
from .models import Client, Address


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "type_clients",
            "title_social",
            "first_name",
            "last_name",
            "email",
            "phone",
            "message",
        ]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})