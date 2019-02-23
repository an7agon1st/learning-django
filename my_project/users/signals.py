from django.db.models.signals import post_save	# singal fired after object saved
from django.contrib.auth.models import User	# the sender for the signal
from django.dispatch import receiver 	# reciever recieves signal and performs some task
from .models import Profile

@receiver(post_save, sender=User)	# signal from User received
def create_profile(sender, instance, created, **kwargs):		#**kwargs accepts any add keyword arguments afterwards
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)	# to save profile when user is saved
def save_profile(sender, instance, **kwargs):		#**kwards accepts any add keyword arguments afterwards
	instance.profile.save()
