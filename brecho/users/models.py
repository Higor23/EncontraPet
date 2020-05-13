from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    telefone = models.CharField(max_length=11, blank=True)
    email =models.EmailField(max_length=244, blank=False, null=False, unique=True)

    def __str__(self):
        return self.username


