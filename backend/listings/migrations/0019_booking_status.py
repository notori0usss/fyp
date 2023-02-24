# Generated by Django 4.1.5 on 2023-02-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_remove_listing_booking_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50),
        ),
    ]
