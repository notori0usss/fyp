from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=10, null=True, blank=True)
    l_name = models.CharField(max_length=10, null=True, blank=True)
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/%Y/%m/%d', default="user.png")
    subscribed = models.BooleanField(default=False, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    facebook_link = models.CharField(
        max_length=100, default="https://www.facebook.com/", blank=True)
    youtube_link = models.CharField(
        max_length=100, default="https://www.youtube.com/", blank=True)
    tiktok_link = models.CharField(
        max_length=100, default="https://www.tiktok.com/", blank=True)

    def __str__(self):
        return f"Profile of {self.seller.username}"


class OnlineUser(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
