from django.db import models
import uuid

from clients.models import Client


# Create your models here.
class Service(models.Model):
    CARS = [
        ('4X4', '4X4'),
        ('CITADINE', 'CITADINE'),
        ('MINIBUS', 'MINIBUS'),
    ]

    TYPE_SERVICE = [
        ('TRANSFERT', 'TRANSFERT'),
        ('MISE-A-DISPOSITION', 'MISE-A-DISPOSITION'),
    ]

    CATEGORY_CHOICES = [
        ('Voyage-Professionnel', 'Voyage-Professionnel'),
        ('Tourisme', 'Tourisme'),
        ('Famille', 'Famille'),
        ('Resident', 'Resident'),
        ('Groupe', 'Groupe'),
        ('Evenement', 'Evenement'),
        ('Autres', 'Autres'),
    ]

    name = models.CharField(max_length=100)
    type_service = models.CharField(max_length=100, choices=TYPE_SERVICE)
    car = models.CharField(max_length=100, choices=CARS)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):

    NAME = [
        ('Devis', 'Devis'),
        ('Facture', 'Facture'),
        ('Avoir', 'Avoir'),
    ]

    name = models.CharField(max_length=100, choices=NAME, default='Devis')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name="invoices")
    start_city = models.CharField(max_length=100)
    end_city = models.CharField(max_length=100)
    date_start = models.DateField()
    time_start = models.TimeField()
    date_end = models.DateField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    duration = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.client.first_name

    def get_total_price(self):
        return sum([service.price * service.duration for service in self.services.all()])

    def get_total_ht(self):
        return sum(service.price * service.duration for service in self.services.all())

    def get_total_duration(self):
        return sum([service.duration for service in self.services.all()])

    def get_tva(self):  # rate est le taux de TVA applicable
        tva = 0
        return tva

    def get_net_a_payer(self):
        total_ht = self.get_total_ht()
        total_due = total_ht - self.advance_payment
        return max(total_due, 0)

