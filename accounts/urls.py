from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('login/', user_login, name='login'),
    # path('rest_p/', rest_p, name='rest_p'),

    path('register/', UserRegisterView, name='register'),
    path('profile/', profile, name='profile'),


  


    path('logout/', logout1, name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
    # path('social_auth1/', include('social_django.urls', namespace='social1')),


]