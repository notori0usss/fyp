# Generated by Django 4.1.5 on 2023-02-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_alter_listing_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='booking',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
