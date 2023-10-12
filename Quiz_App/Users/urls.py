from django.urls import path
from django.contrib.auth import views as auth_views
from Users import views

app_name = 'Users'

urlpatterns = [
    path('login/',views.Login, name="login"),
    path('register/',views.Register, name="register"),
    path('logout/',views.Logout, name="logout"),
]