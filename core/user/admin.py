from django.contrib import admin
from .models import User,CurrentUserToken
# Register your models here.
admin.site.register(User)
admin.site.register(CurrentUserToken)