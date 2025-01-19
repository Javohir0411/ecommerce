from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class CustomUser(AbstractUser):
    birthdate = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=300)
    login = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=50)
    password_confirm = models.CharField(max_length=50)
    scientific_degree = models.CharField(max_length=200)
    another_info = models.TextField(blank=True, null=True)
    is_reviewer = models.BooleanField(default=False)
    # Modify the related_name for 'groups' and 'user_permissions'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this name to avoid conflict
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Change this name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'
        indexes = [
            models.Index(fields=['user', 'created_at'])]
