from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Lockscreen(LoginRequiredMixin,TemplateView):
    template_name = "authentication/auth-lock-screen.html"
class Login(LoginRequiredMixin,TemplateView):
    template_name = "authentication/auth-login.html"
class Register(LoginRequiredMixin,TemplateView):
    template_name = "authentication/auth-register.html"