# Generated by Django 4.1.5 on 2023-03-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0025_alter_booking_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]