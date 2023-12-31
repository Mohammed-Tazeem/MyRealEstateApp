# Generated by Django 4.2.1 on 2023-05-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0007_remove_listings_location_listings_latitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="rental_frequency",
            field=models.CharField(
                blank=True,
                choices=[("Month", "Month"), ("Day", "Day"), ("Week", "Week")],
                max_length=20,
                null=True,
            ),
        ),
    ]
