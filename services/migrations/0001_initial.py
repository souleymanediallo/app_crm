# Generated by Django 5.0.2 on 2024-03-03 17:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type_service",
                    models.CharField(
                        choices=[
                            ("TRANSFERT", "TRANSFERT"),
                            ("MISE-A-DISPOSITION", "MISE-A-DISPOSITION"),
                        ],
                        max_length=100,
                    ),
                ),
                ("start_city", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("end_city", models.CharField(max_length=100)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
                ("duration", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
            ],
        ),
    ]
