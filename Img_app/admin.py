from django.contrib import admin
from .models import CustomUser, AccountTier, Image

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'plan']

@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = ['name', 'original_link', 'expiring_link']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'uploaded_at']

