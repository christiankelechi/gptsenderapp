from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, StudentUser
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError,force_str
from django.views.generic import View
from .utils import generate_token
import django.contrib.auth.forms
from django.shortcuts import render
import random
import requests
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, StudentUser
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError,force_str
from django.core.mail import EmailMessage
from django.conf import settings

from django.views.generic import View
import threading


# profile update import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponse
from core.user.models import User

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'account activated successfully')
            return redirect('login')
        return render(request, 'accoun/activate_failed.html', status=401)
