from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERTYPE_CHOICES = (
    ("SUPERUSER", "SUPERUSER"),
    ("SYSTEMUSER", "SYSTEMUSER"),
    ("NORMALUSERS", "NORMALUSERS"),
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_type = models.CharField(choices= USERTYPE_CHOICES, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "first_name", "last_name","user_type"

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
