from django.urls import path , include
from django.conf import settings
from login import views
from .views import LoginView,LogoutView



urlpatterns = [
    path('home', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('', LoginView.as_view(), name='login'),
    path('out', LogoutView.as_view(), name='logout'),

]
  


  