from django.urls import path
from . import views
app_name = 'usersapp'
urlpatterns = [
     path('', views.home_page, name='home-page'),
    path('user-home', views.user_page, name='user-home'),
    path('user-login', views.login_user, name='user-login'),
    path('user-registration', views.register_user, name='user-registration'),
    path('logout', views.logout_user, name="logout-user"),
    path('usernameValidation', views.usernameValidation, name='usernameValidation'),
    
]
