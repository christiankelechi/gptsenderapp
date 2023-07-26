from django.db import models
from core.user.models import User
from django.utils import timezone
# Create your models here.
class EmailGeneratorModel(models.Model):
    number_of_mail=models.IntegerField()
    prompt=models.TextField(max_length=1000000)
    access_token=models.TextField(blank=True,null=True)
    generated_emails=models.FileField(upload_to='messages',null=True)
    swapped_emails = models.FileField(upload_to='swapped',null=True)
    


class OpenAiUserModel(models.Model):
    custom_user_key_id=models.IntegerField(null=True,blank=True)
    open_ai_key=models.CharField(null=True,blank=True,max_length=400)
    time_of_assigning=models.DateTimeField(blank=True,null=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"The {self.open_ai_key} have been assigned to {self.user}"

class OpenAiAdminModel(models.Model):
    custom_user_key_id=models.IntegerField(null=True,blank=True)
    open_ai_key=models.CharField(null=True,blank=True,max_length=400)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    assigned=models.BooleanField(default=False)

    def __str__(self):
        return f"The {self.open_ai_key} have been generated for {self.custom_user_key_id}"

class UserCredentials(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    token_stored=models.CharField(max_length=1000)
    request_id=models.TextField(max_length=4000)

class EmailMessageModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=400)
    message_body=models.TextField(blank=True,null=True)
    maillist=models.TextField(null=True,blank=True)
    site_url=models.CharField(max_length=400)
