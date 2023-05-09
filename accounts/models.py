from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "first_name", "last_name"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "User"

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="accounts/profile/profile_picture", default="accounts/profile/profile_picture/defaultuser.png")
    address = models.CharField(max_length=255, default="None")
    phone = models.PositiveBigIntegerField(default="9874561230")


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
