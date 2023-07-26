from django.contrib import admin
from .models import UsdModel,EthModel,Wallet

admin.site.register(UsdModel)
admin.site.register(EthModel)
admin.site.register(Wallet)
# Register your models here.
