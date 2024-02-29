from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_staff', 'is_active')

admin.site.register(Account, CustomUserAdmin)



# Register your models here.
    