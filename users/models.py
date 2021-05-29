from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

#obj.date_modified = datetime.now()

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	discordName = models.TextField(max_length=80, blank=True)
	creation_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		instance.profile.creation_date = date.today()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()