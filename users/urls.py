from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('register/done/', views.register_done, name="register_done"),
    
    path('profile/', views.ProfileUser.as_view(), name="profile"),
    
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', views.UserPasswordChangeDone.as_view(), name='password_change_done'),
    
    path('password-reset/', views.UserPasswordReset.as_view(), name="password_reset"),
    path('password-reset/done/', views.UserPasswordResetDone.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', views.UserPasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', views.UserPasswordResetComplete.as_view(), name="password_reset_complete"),
]