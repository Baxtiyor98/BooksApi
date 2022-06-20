from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='Users',null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_block = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


