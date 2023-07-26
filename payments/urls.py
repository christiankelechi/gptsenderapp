from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home_view, name='home'),
    path('success/', views.success_view, name='payments-success'), # new
    path('cancel/', views.cancel_view, name='payments-cancel'),
]