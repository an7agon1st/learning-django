from django.db import models
from django.contrib.auth.models import User		#import user model

from PIL import Image 		# importing pillows lib


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)		# on delete, deletes the profile
	image = models.ImageField(default='default.jpeg', upload_to = 'profile_pics')		#images upload to profile_pics dir, default image = default.jpeg

	def __str__(self):
		return f'{self.user.username} Profile'		# tells django how to print the profile
	
	def save(self):	# runs automatically to save (present in parent class, function is overridden)
		super().save()		# runs parent class's save method

		img = Image.open(self.image.path)		# open self image

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)		#tuple
			img.thumbnail(output_size)		# resizes image
			img.save(self.image.path)		# saves smaller image



