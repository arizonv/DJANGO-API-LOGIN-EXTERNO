from django.urls import path
from .views import LoginView,UserLogout


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]