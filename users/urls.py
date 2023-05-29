from django.urls import path

import users.views as user_views

app_name = 'users'

urlpatterns = [
    path('registration/', user_views.RegistrationCreateView.as_view(), name='registration'),
    path('login/', user_views.LoginView.as_view(), name='login'),
    path('logout/', user_views.LogoutView.as_view(), name='logout'),

    path('<slug:slug>/', user_views.ProfileView.as_view(), name='profile'),
    path('<slug:slug>/password', user_views.ProfilePasswordView.as_view(), name='profile-password'),
    path('<slug:slug>/email', user_views.ProfileEmailView.as_view(), name='profile-email'),

    path('verification/send/<str:email>/', user_views.SendVerificationEmailView.as_view(),
         name='send-verification-email'),
    path('verify/<str:email>/<uuid:code>/', user_views.EmailVerificationView.as_view(), name='email-verification'),
]
