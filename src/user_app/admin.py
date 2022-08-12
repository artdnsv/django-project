from django.contrib import admin
from user_app import models 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class AccountInLine(admin.StackedInline):
    model = models.Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustimizeUserAdmin (UserAdmin):
    inlines = (AccountInLine, )

admin.site.unregister(User)
admin.site.register(User, CustimizeUserAdmin)