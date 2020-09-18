from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(default='def_av.jpg', upload_to='profile_pics')
    bio_desc = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'
