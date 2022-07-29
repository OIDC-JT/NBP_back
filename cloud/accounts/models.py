from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from .autosql import autosql


class CustomUserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password, **extra_fields):
        if username is None:
            raise TypeError('Users must have a username.')

        if first_name is None:
            raise TypeError('Users must have a first_name address.')

        if last_name is None:
            raise TypeError('Users must have a last_name address.')

        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name, 
            **extra_fields
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, first_name, last_name, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name'
    ]

    objects = CustomUserManager()
    

    # def __str__(self):
    #     return self.email

class Autosql(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(max_length=200)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Autosql.objects.create(user=instance)
        username = instance.username
        autosql(username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.autosql.save()