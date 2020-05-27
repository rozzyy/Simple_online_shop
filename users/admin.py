from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')

# Register your models here.
admin.site.register(Account, AccountAdmin)