from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Represents a user profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
