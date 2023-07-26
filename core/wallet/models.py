from django.db import models
# from core.wallet.models import BtcModel,EthModel
from core.user.models import User
class UsdModel(models.Model):
    wallet_address=models.CharField(max_length=10,null=True,blank=True)
    user=models.ForeignKey('core_user.User',on_delete=models.CASCADE,blank=True,null=True)
    amount=models.FloatField(default=0,blank=True,null=True)
    # def fund_btc(self,amount,user):
    #     btc_fund = self.model(user=user, amount=amount)
    #     return user
    def __str__(self):
        return str(self.user)+f'Account created and toped up with usd{self.amount}'

class BtcInvoice(models.Model):
    STATUS_CHOICES=((-1,"Not Started"),(0,"Unconfirmed"),(1,"Partially Confirmed"),(2,"Confirmed"))

    btc=models.ForeignKey(UsdModel,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=250,blank=True,null=True)
    address=models.CharField(max_length=250,blank=True,null=True)
    btcvalue=models.IntegerField(blank=True,null=True)
    received=models.IntegerField(null=True,blank=True)
    txid=models.CharField(max_length=250,blank=True,null=True)
    rbf=models.IntegerField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now=True)
    
class EthModel(models.Model):
    wallet_id=models.CharField(max_length=300,null=True,blank=True)
    wallet_address=models.TextField(null=True,blank=True)

    user=models.ForeignKey('core_user.User',on_delete=models.CASCADE,blank=True,null=True)
    # created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    # address=models.CharField(max_length=100)
    # public_key=models.CharField(max_length=1000)
    # private_key=models.CharField(max_length=100)
    amount=models.FloatField(default=0,blank=True,null=True)

    def __str__(self):
        return f'{self.user} top up his account with {self.amount}'
    


    
    
class Wallet(models.Model):
    user=models.ForeignKey('core_user.User',on_delete=models.CASCADE,blank=True,null=True)
    btc_model=models.ForeignKey(UsdModel,on_delete=models.CASCADE)
    eth_model=models.ForeignKey(EthModel,on_delete=models.CASCADE)


