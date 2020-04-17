from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # Import Image From Pillow Library. To Grab The Image and Resize It.

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # One-To-One Relationship With The Existing User Model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')   # upload_to means directory, which will create to store profile images.


    def __str__(self):
        return f'{self.user.username} Profile'   # It's Called f'{}' string

 # Resize Image Automatically
    def save(self):
        super().save()  # Run The Save Method Of Our Parent Class.

        img = Image.open(self.image.path)  # self.image.path will open image of current instance.

        if img.height > 300 or img.width > 300:  # Resize The Image.
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) # overwrite the large image
