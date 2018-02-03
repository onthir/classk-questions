from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250, default=None, null=True)
    email = models.EmailField(max_length=100, default=None, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8, default=None, null=True)
    bio = models.TextField(max_length=500, default=None, null=True)
    location = models.CharField(max_length=30, default=None, null=True)
    birth_date = models.DateField(null=True, default=None)
    points = models.IntegerField(default=0)
    viewes = models.IntegerField(default=0)
 
    def __str__(self):
        return self.full_name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()