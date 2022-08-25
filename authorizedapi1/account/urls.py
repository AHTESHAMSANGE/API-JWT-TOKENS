from django.urls import path
from account.views import SendPasswordResetEmailView, UserPasswordResetView, UserRegistrationView
from account.views import UserLoginView
from account.views import UserProfileView
from account.views import UserChangePasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),
    name='register'),

    path('login/', UserLoginView.as_view(),
    name='login'),

    path('profile/', UserProfileView.as_view(),
    name='profile'),

    path('ChangePassword/', UserChangePasswordView.as_view(),
    name='ChangePassword'),
    
    path('SendPasswordResetEmail/', SendPasswordResetEmailView.as_view(),
    name='SendPasswordResetEmail'),
    
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),
    name='reset-password'),

]