from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _




# Create your models here.

class Profile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today)
    

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
