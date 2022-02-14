from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', views.register_page, name="register"),
    path('inicio/', views.index, name="inicio"),
    path('login/', views.login_page, name="login")
    
]
