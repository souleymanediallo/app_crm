# Generated by Django 5.0.2 on 2024-03-03 18:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="service",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="service",
            name="start_date",
        ),
        migrations.RemoveField(
            model_name="service",
            name="start_time",
        ),
    ]
