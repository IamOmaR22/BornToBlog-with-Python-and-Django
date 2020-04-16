from django.db.models.signals import post_save  # This is a Signal That get to fired after an object is saved.
from django.contrib.auth.models import User  # Built In User Model. It is going to send the signal.
from django.dispatch import receiver  # It is a function that gets this signal and then perform some task.
from .models import Profile  # Profile model


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()