from django.views import View
from django.views.generic import FormView
from django.shortcuts import  redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms
# Create your views here.

class LoginView(FormView):
    
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")
    
    def form_valid(self,form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request,username=email,password=password)
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name":"Jun",
        "last_name":"admin",
        "email":"gus12@naver.com",
    }
    
    def form_invalid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request,username=email,password=password)
        if user is not None:
            login(self.request,user)
        return super().form_invalid(form)