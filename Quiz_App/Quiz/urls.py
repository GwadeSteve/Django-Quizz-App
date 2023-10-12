from django.urls import path, include
from Quiz import views

app_name = "Quiz"

urlpatterns = [
    path('',views.main,name="home"),
]
