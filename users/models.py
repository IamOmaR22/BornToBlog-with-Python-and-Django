from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # One-To-One Relationship With The Existing User Model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')   # upload_to means directory, which will create to store profile images.


    def __str__(self):
        return f'{self.user.username} Profile'   # It's Called f'{}' string