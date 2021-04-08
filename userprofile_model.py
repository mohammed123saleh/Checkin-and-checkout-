
'''
Esraa please note that to use CountryField
 you will do the following:
1-pip install django-countries
2- you will add 'django_countries' to you settings' installed apps,
may you do not need it but it's simple to setup and adds value to your app


*and note that it's better to read django signals docs and it's very concise, ten mins read
or watch this video for one of the best instructors in django
https://www.youtube.com/watch?v=rEX50LJrFuU
'''

from django_countries.fields import CountryField
from django.db.models.signals import post_save 
from django.conf import settings



School_roles = (
	('S','Student'),
	('T','Teacher'),
	('M', 'Managerial'),
	)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(choices=School_roles, max_length=20, blank=True)#max_length could be 1 but it doesn't matter so keep 20
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = CountryField(multiple=False)
    image = models.ImageField(blank=True, upload_to='images/users/')
    def __str__(self):
        return self.user.username



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
