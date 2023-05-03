from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    #path('packageinfo/', views.home, name= "p_info"),
]