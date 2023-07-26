from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
    
    # path('logout',auth_views.LogoutView.as_view(template_name="logout.html"),name='logout'),
    # path('login',student_login,name='login'),
    # path('dashboardhome',dashboardhome,name='dashboardhome'),
    path('login/',auth_views.LoginView.as_view(template_name="account/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="account/logout.html"),name='logout'),
    path('password-change/',
    auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),
    name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
#     path('edit/', edit, name='edit'),
    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate'),
    
]