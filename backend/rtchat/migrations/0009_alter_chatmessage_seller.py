# Generated by Django 4.1.5 on 2023-03-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtchat', '0008_chatmessage_seller_alter_chatmessage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='seller',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
