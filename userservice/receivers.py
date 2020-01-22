from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created=False, **kwargs):
    if not instance.is_staff:
        if created :
            Profile.objects.create(user=instance)
            Token.objects.create(user=instance)
        instance.profile.save()

# @receiver(post_delete, sender=User)
# def delete_user_profile(sender, instance=None, **kwargs):
#     instance.profile.delete(user=instance)


