from django.db import models
import uuid


# Create your models here.
class Client(models.Model):
    TITLE_SOCIAL = [
        ('Monsieur', 'Monsieur'),
        ('Madame', 'Madame'),
    ]

    TYPE_CLIENTS = [
        ('Particulier', 'Particulier'),
        ('Professionnel', 'Professionnel'),
    ]

    type_clients = models.CharField(max_length=100, choices=TYPE_CLIENTS, default='Particulier')
    title_social = models.CharField(max_length=100, choices=TITLE_SOCIAL, default='Monsieur')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.first_name


class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=True, null=True)
    address_1 = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.client.first_name
