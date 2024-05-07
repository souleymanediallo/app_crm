from django import forms
from .models import Client, Address


class ClientForm(forms.ModelForm):
    company = forms.CharField(required=False)
    address_1 = forms.CharField(required=False)
    address_2 = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    city = forms.CharField(required=False)
    country = forms.CharField(required=False)

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

    def save(self, commit=True):
        client = super().save(commit=False)
        if commit:
            client.save()
            Address.objects.create(client=client, company=self.cleaned_data['company'],
                                   address_1=self.cleaned_data['address_1'],
                                   address_2=self.cleaned_data['address_2'],
                                   zip_code=self.cleaned_data['zip_code'],
                                   city=self.cleaned_data['city'],
                                   country=self.cleaned_data['country']
                                   )
        return client