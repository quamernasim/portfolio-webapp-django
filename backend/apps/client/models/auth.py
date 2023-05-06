from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='auth_users', 
        blank=True, 
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', 
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='auth_users', 
        blank=True, 
        help_text='Specific permissions for this user.', 
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = 'q'
        super().save(*args, **kwargs)