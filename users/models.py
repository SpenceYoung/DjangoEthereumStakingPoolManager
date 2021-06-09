from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
from datetime import date

fs = FileSystemStorage(location='/media/photos')

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	discordName = models.TextField(max_length=80, blank=True)
	creation_date = models.DateField(null=True, blank=True)


class PoolManager(models.Model):
	cryptoName = models.TextField(max_length=80, blank=True)
	total = models.FloatField(null=True, blank=True, default = 0)
	cryptoAddress = models.TextField(max_length=100, blank=True)

class ContributionManager(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pool = models.OneToOneField(PoolManager, on_delete=models.CASCADE)
	amount = models.FloatField(null=True, blank=True, default = 0)
	contribImage = models.ImageField(null=True, blank=True,storage=fs)
	contributions = models.FloatField(null=True, blank=True, default = 0)
	rewards = models.FloatField(null=True, blank=True, default = 0)

class Contribution(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pool = models.OneToOneField(PoolManager, on_delete=models.CASCADE)
	amount = models.FloatField(null=True, blank=True, default = 0)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		instance.profile.creation_date = date.today()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()