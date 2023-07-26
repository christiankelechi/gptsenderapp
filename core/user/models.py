from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
import uuid

class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        # if username is None:
        #     raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)


        return user

    def create_superuser(self, username, email, password, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True,blank=True,null=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)

    email = models.EmailField(db_index=True, unique=True,blank=True)
    is_active = models.BooleanField(default=True,blank=True)
    is_superuser = models.BooleanField(default=False,blank=True)
    is_staff = models.BooleanField(default=False,blank=True)  # Add this line

    created = models.DateTimeField(auto_now=True,blank=True)
    updated = models.DateTimeField(auto_now_add=True,null=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    # open_ai_key=models.TextField(blank=True,null=True)
    # current_token=models.CharField(null=True,blank=True,max_length=50000)

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

class CurrentUserToken(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    token=models.TextField(max_length=2000)
    time_of_generation=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} token {self.token} stored successfully'

