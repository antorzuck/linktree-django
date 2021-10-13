from django.db import models
from django.contrib.auth.models import User
import datetime
from django.dispatch import receiver 
from django.db.models.signals import post_save 

# Create your models here.
class Links(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
	date = models.DateField(("Date"), default=datetime.date.today)
	title = models.CharField(max_length=50)
	url = models.URLField(max_length=300)
	
	def __str__(self):
		return self.title
		
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE, default="")
	img = models.FileField(upload_to='photos', default='bal.jpg',null=True, blank=True)
	bio = models.TextField(default="")
	
	@property
	def imgurl(self):
	   if self.img and hasattr(self.img, 'url'):
	   	return self.img.url
	   else:
	   	return 'media/bal.jpg'
	   
    
                      		
	
	@receiver(post_save, sender=User) 
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User) 
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
	
	


