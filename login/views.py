from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView
from.forms import LoginForm
import requests
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from core import settings



@login_required
def home(request):
    return render(request, 'home.html')


def dash(request):
    return render(request, 'dashboard.html')



class LoginView(FormView):
    template_name = 'log/login.html'
    form_class = LoginForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form): 

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        response = requests.post('http://127.0.0.1:8000/api/',json={'username': username, 'password': password},auth=(username, password))
        if response.status_code == 200:
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return HttpResponseRedirect(self.success_url)

            return redirect('login')
        else :
            return render(self.request, 'log/login.html')



class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)








