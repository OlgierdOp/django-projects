from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()
# Create your models here.

class UserProfile(models.Model):
    # user = models.OneToOneField(User)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    picture = models.ImageField(upload_to="users/pictures/", null=True, blank=True)