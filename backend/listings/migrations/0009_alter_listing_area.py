# Generated by Django 4.1.5 on 2023-01-30 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_rename_borough_listing_municipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(blank=True, choices=[('Kathmandu', 'Kathmandu'), ('Bhaktapur', 'Bhaktapur')], max_length=20, null=True),
        ),
    ]
