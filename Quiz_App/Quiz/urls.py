from django.urls import path, include
from Quiz import views

urlpatterns = [
    path('',views.main,name="home"),
]
