from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    adress = models.TextField(max_length=128, blank=True, default='')
    AboutMe = models.TextField(max_length=256, blank=True, default='')
    data = models.DateField()
    gender=models.IntegerField(choices=((1,'Man'),(2, 'Woman'),(3,'Other')))
    photo = models.ImageField(upload_to='media/',default='default/defaultPhoto.png',blank=True)

    def __str__(self):
        return self.user.username


class ContactAndLinks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='contact_and_links')
    title = models.CharField(max_length=32, blank=True, default='')
    link = models.CharField(max_length=1024, blank=True, default='')

    def __str__(self):
        return self.title