"""CoreRoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from email_msg_generator.viewsets import EmailGeneratorViewSet
# from core.wallet.views import BTCAmountView

router = DefaultRouter()
router.register(r'email-generator', EmailGeneratorViewSet, basename='email-generator')
from email_msg_generator.viewsets import EmailMessageViewsets
router.register(r'emailmessagesending',EmailMessageViewsets,basename='emailmessagesending')
# router.register(r'')
from core.wallet import views
from django.urls import path
from core.wallet import viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('core.routers', 'core'), namespace="core-api")),
    path('', include(router.urls)),
    path('api/auth/check-authorization/', views.check_authorization, name='check-authorization'),
    path('wallet/topup',viewsets.topup,name='topup'),
    
    # path('generate-emails/', EmailGeneratorView.as_view(), name='generate-emails'),
]

