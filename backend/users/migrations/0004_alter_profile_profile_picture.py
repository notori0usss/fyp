# Generated by Django 4.1.5 on 2023-02-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='user.png', upload_to='profile_pictures/%Y/%m/%d'),
        ),
    ]
