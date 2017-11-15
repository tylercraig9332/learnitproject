from django.db import models
from django.contrib.auth import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


    post_save.connect(create_user_profile, sender=User)
