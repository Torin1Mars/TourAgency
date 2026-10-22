
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .form import RegisterForm

# Views
def home(request):
    return render(request, "auth1_app/home.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            current_user:User = User.objects.create_user(username=username, password=password)
            login(request, current_user)

            return redirect("home")

        else:
            empty_form = RegisterForm()
            return render(request,"accounts/register.html", {"form":empty_form} )


def logging_view(request):
    if request.methoud == "POST":
        username = request.POST.get("username")
        password = request.POST.get("username")

        current_user = authenticate(request, username= username, password = password)

        if current_user is not None:
            login(request, current_user)

            next_url = request.POST.get('next') or request.Get.get('next') or "home"
            return redirect(next_url)

        else:
            error_message = "Invalid Credentials"

    return render(request, "accounts/logging.html", {"error":error_message})


def logout_view(request):
    if request.methoud == "POST":
        logout(request)
        return redirect("loging")
    else:
        return redirect("home")


#Home view
@login_required
def home_view (request):
    return render(request, 'auth1_app/home.html')

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'

    #next to redirect url
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')

