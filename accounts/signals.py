from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import Profile, User


@receiver(post_save, sender=User)
def profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)