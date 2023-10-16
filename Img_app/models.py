from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(AbstractUser):
    PLAN_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    ]
    plan = models.CharField(choices=PLAN_CHOICES, default='Basic', max_length=50)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )



class AccountTier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.JSONField()  # List of thumbnail sizes
    original_link = models.BooleanField(default=False)
    expiring_link = models.BooleanField(default=False)
    expiring_link_duration = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(30000)],
        null=True,
        blank=True,
    )

class Image(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    account_tier = models.ForeignKey(AccountTier, null=True, blank=True, on_delete=models.SET_NULL)
