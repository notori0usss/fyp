# Generated by Django 4.1.5 on 2023-01-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_spread_area_alter_listing_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='spread_area',
            new_name='property_area',
        ),
    ]
